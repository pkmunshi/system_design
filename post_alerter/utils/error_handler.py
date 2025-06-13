import logging
import traceback
import sys
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

class ErrorSeverity:
    """Error severity levels."""
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

class ErrorHandler:
    def __init__(self, alert_threshold: str = ErrorSeverity.ERROR):
        """
        Initialize error handler.
        
        Args:
            alert_threshold: Minimum severity level to trigger alerts
        """
        self.alert_threshold = alert_threshold
        self.error_log_file = 'logs/error_log.json'
        self._ensure_log_dir()
        
    def _ensure_log_dir(self):
        """Ensure logs directory exists."""
        os.makedirs('logs', exist_ok=True)
        
    def _get_severity_level(self, severity: str) -> int:
        """Get numeric level for severity."""
        levels = {
            ErrorSeverity.INFO: 0,
            ErrorSeverity.WARNING: 1,
            ErrorSeverity.ERROR: 2,
            ErrorSeverity.CRITICAL: 3
        }
        return levels.get(severity, 0)
        
    def _should_alert(self, severity: str) -> bool:
        """Check if error should trigger an alert."""
        return self._get_severity_level(severity) >= self._get_severity_level(self.alert_threshold)
        
    def _log_error(self, error: Exception, severity: str, context: Optional[Dict[str, Any]] = None):
        """Log error to file."""
        error_data = {
            'timestamp': datetime.now().isoformat(),
            'severity': severity,
            'error_type': type(error).__name__,
            'error_message': str(error),
            'traceback': traceback.format_exc(),
            'context': context or {}
        }
        
        try:
            # Append to error log file
            with open(self.error_log_file, 'a') as f:
                f.write(f"{error_data}\n")
        except Exception as e:
            logger.error(f"Failed to log error: {str(e)}")
            
    def _send_alert(self, error: Exception, severity: str, context: Optional[Dict[str, Any]] = None):
        """Send alert email for critical errors."""
        try:
            # Get email configuration from environment
            from_email = os.getenv("FROM_EMAIL")
            app_password = os.getenv("GMAIL_APP_PASSWORD")
            to_emails = os.getenv("TO_EMAILS", "").split(",")
            
            if not all([from_email, app_password, to_emails]):
                logger.error("Missing email configuration for alerts")
                return
                
            # Create email message
            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = ", ".join(to_emails)
            msg['Subject'] = f"Trade Alerter {severity} Alert"
            
            # Build email body
            body = f"""
            Trade Alerter Error Alert
            
            Severity: {severity}
            Time: {datetime.now().isoformat()}
            Error Type: {type(error).__name__}
            Error Message: {str(error)}
            
            Traceback:
            {traceback.format_exc()}
            
            Context:
            {context or 'No additional context'}
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Send email
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(from_email, app_password)
                server.send_message(msg)
                
            logger.info(f"Alert email sent for {severity} error")
            
        except Exception as e:
            logger.error(f"Failed to send alert email: {str(e)}")
            
    def handle_error(self, error: Exception, severity: str = ErrorSeverity.ERROR, 
                    context: Optional[Dict[str, Any]] = None, reraise: bool = True):
        """
        Handle an error with appropriate logging and alerts.
        
        Args:
            error: The exception to handle
            severity: Error severity level
            context: Additional context about the error
            reraise: Whether to re-raise the exception after handling
        """
        # Log the error
        self._log_error(error, severity, context)
        
        # Log to standard logger
        log_message = f"{severity}: {str(error)}"
        if context:
            log_message += f" Context: {context}"
            
        if severity == ErrorSeverity.INFO:
            logger.info(log_message)
        elif severity == ErrorSeverity.WARNING:
            logger.warning(log_message)
        elif severity == ErrorSeverity.ERROR:
            logger.error(log_message)
        elif severity == ErrorSeverity.CRITICAL:
            logger.critical(log_message)
            
        # Send alert if severity meets threshold
        if self._should_alert(severity):
            self._send_alert(error, severity, context)
            
        # Re-raise if requested
        if reraise:
            raise error
            
    def get_recent_errors(self, hours: int = 24) -> list:
        """Get list of recent errors from the log file."""
        try:
            if not os.path.exists(self.error_log_file):
                return []
                
            recent_errors = []
            cutoff_time = datetime.now().timestamp() - (hours * 3600)
            
            with open(self.error_log_file, 'r') as f:
                for line in f:
                    try:
                        error_data = eval(line.strip())
                        error_time = datetime.fromisoformat(error_data['timestamp']).timestamp()
                        if error_time >= cutoff_time:
                            recent_errors.append(error_data)
                    except Exception:
                        continue
                        
            return recent_errors
            
        except Exception as e:
            logger.error(f"Failed to get recent errors: {str(e)}")
            return [] 