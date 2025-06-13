import json
import os
import asyncio
from checker.post_checker import login_and_get_latest_post
from checker.check_chrome import check_chrome_installation
from dotenv import load_dotenv
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utils.secure_storage import SecureStorage
from utils.secure_logging import setup_logging
from utils.error_handler import ErrorHandler, ErrorSeverity

# Set up secure logging
logger = setup_logging()

# Initialize error handler
error_handler = ErrorHandler(alert_threshold=ErrorSeverity.ERROR)

CONFIG_PATH = 'config/config.json'
CACHE_PATH = 'data/last_post.enc'
DIFF_PATH = 'data/new_diff.enc'

def load_config():
    """Load configuration from file and environment variables."""
    try:
        with open(CONFIG_PATH) as f:
            config = json.load(f)
        
        # Override sensitive data with environment variables
        config.update({
            "username": os.getenv("TRADE_USERNAME"),
            "password": os.getenv("TRADE_PASSWORD"),
            "from_email": os.getenv("FROM_EMAIL"),
            "gmail_app_password": os.getenv("GMAIL_APP_PASSWORD"),
            "to_number": os.getenv("TO_SMS_NUMBER"),
            "to_emails": os.getenv("TO_EMAILS"),
            "encryption_key": os.getenv("ENCRYPTION_KEY")
        })
        
        # Validate required environment variables
        required_vars = [
            "TRADE_USERNAME",
            "TRADE_PASSWORD",
            "FROM_EMAIL",
            "GMAIL_APP_PASSWORD",
            "TO_SMS_NUMBER",
            "TO_EMAILS",
            "ENCRYPTION_KEY"
        ]
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
        
        return config
    except Exception as e:
        error_handler.handle_error(
            e,
            severity=ErrorSeverity.ERROR,
            context={"function": "load_config"},
            reraise=True
        )

def send_alerts(msg):
    """Send alerts via email and SMS."""
    try:
        logger.info("Preparing to send alerts")
        
        sms_recipients = [os.getenv("TO_SMS_NUMBER") + "@vtext.com"]
        email_recipients = [email.strip() for email in os.getenv("TO_EMAILS", "").split(",") if email.strip()]
        
        message = "Value Trader NEW TRADE ALERT: \n" + msg
        auth = (os.getenv("FROM_EMAIL"), os.getenv("GMAIL_APP_PASSWORD"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(auth[0], auth[1])

        # Send SMS
        server.sendmail(auth[0], sms_recipients, message)
        logger.info("SMS alert sent successfully")

        # Create and send email
        email_message = MIMEMultipart()
        email_message["From"] = auth[0]
        email_message["To"] = ", ".join(email_recipients)
        email_message["Subject"] = "Value Trader NEW TRADE ALERT"
        email_message.attach(MIMEText(msg, "plain"))

        server.sendmail(auth[0], email_recipients, email_message.as_string())
        logger.info("Email alert sent successfully")

    except Exception as e:
        error_handler.handle_error(
            e,
            severity=ErrorSeverity.ERROR,
            context={
                "function": "send_alerts",
                "message": msg,
                "recipients": {
                    "sms": sms_recipients,
                    "email": email_recipients
                }
            },
            reraise=True
        )
    finally:
        if 'server' in locals():
            server.quit()

async def main():
    try:
        # Initialize secure storage
        logger.info(f"ENCRYPTION_KEY: {os.getenv('ENCRYPTION_KEY')}")
        storage = SecureStorage(os.getenv("ENCRYPTION_KEY"))
        
        # Create data directory if it doesn't exist
        os.makedirs('data', exist_ok=True)
        
        # Check Chrome installation first
        if not check_chrome_installation():
            error_msg = "Chrome browser not installed"
            error_handler.handle_error(
                Exception(error_msg),
                severity=ErrorSeverity.ERROR,
                context={"function": "main", "check": "chrome_installation"},
                reraise=False
            )
            return

        config = load_config()
        new_post = await login_and_get_latest_post(config)
        
        if not new_post:
            logger.info("No post found")
            return

        last_post = storage.load_encrypted(CACHE_PATH)
        
        if new_post != last_post:
            logger.info("New post detected, different from last post")
            
            # Generate and save encrypted diff
            diff_content = storage.save_diff(last_post, new_post, DIFF_PATH)
            logger.info("Difference saved securely")
            
            try:
                # Send notification with diff
                send_alerts(new_post)
                
                # Update last post only after successful notification
                storage.save_encrypted(new_post, CACHE_PATH)
                logger.info("Last post cache updated securely")
                
            except Exception as e:
                error_handler.handle_error(
                    e,
                    severity=ErrorSeverity.ERROR,
                    context={
                        "function": "main",
                        "action": "send_notification",
                        "new_post": new_post
                    },
                    reraise=True
                )
        else:
            logger.info("No changes detected in the post")
            
    except Exception as e:
        error_handler.handle_error(
            e,
            severity=ErrorSeverity.CRITICAL,
            context={"function": "main"},
            reraise=True
        )

if __name__ == "__main__":
    try:
        load_dotenv()
        logger.info("Environment variables loaded")
        asyncio.run(main())
    except Exception as e:
        error_handler.handle_error(
            e,
            severity=ErrorSeverity.CRITICAL,
            context={"function": "__main__"},
            reraise=True
        )

