import re
from typing import List, Optional
import logging

logger = logging.getLogger(__name__)

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass

def validate_phone_number(phone: str) -> str:
    """Validate and sanitize phone number."""
    # Remove any non-digit characters
    digits_only = re.sub(r'\D', '', phone)
    
    # Check if it's a valid US phone number (10 digits)
    if not re.match(r'^\d{10}$', digits_only):
        raise ValidationError(f"Invalid phone number format: {phone}")
    
    return digits_only

def validate_email(email: str) -> str:
    """Validate and sanitize email address."""
    # Basic email validation regex
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Sanitize by removing any whitespace
    sanitized_email = email.strip()
    
    if not re.match(email_pattern, sanitized_email):
        raise ValidationError(f"Invalid email format: {email}")
    
    return sanitized_email

def validate_emails(emails: str) -> List[str]:
    """Validate and sanitize comma-separated email addresses."""
    if not emails:
        return []
    
    # Split by comma and validate each email
    email_list = [email.strip() for email in emails.split(',') if email.strip()]
    validated_emails = []
    
    for email in email_list:
        try:
            validated_email = validate_email(email)
            validated_emails.append(validated_email)
        except ValidationError as e:
            logger.warning(f"Skipping invalid email: {str(e)}")
            continue
    
    return validated_emails

def sanitize_post_content(content: str) -> str:
    """Sanitize post content to remove potentially harmful characters."""
    if not content:
        return ""
    
    # Remove any control characters
    sanitized = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', content)
    
    # Remove any HTML tags
    sanitized = re.sub(r'<[^>]+>', '', sanitized)
    
    # Remove any script tags and their content
    sanitized = re.sub(r'<script.*?</script>', '', sanitized, flags=re.DOTALL)
    
    return sanitized.strip()

def validate_config(config: dict) -> dict:
    """Validate configuration dictionary."""
    required_fields = [
        "login_url",
        "target_url",
        "post_selector",
        "username",
        "password"
    ]
    
    missing_fields = [field for field in required_fields if field not in config]
    if missing_fields:
        raise ValidationError(f"Missing required config fields: {', '.join(missing_fields)}")
    
    # Validate URLs
    url_pattern = r'^https?://[^\s/$.?#].[^\s]*$'
    if not re.match(url_pattern, config["login_url"]):
        raise ValidationError(f"Invalid login URL: {config['login_url']}")
    if not re.match(url_pattern, config["target_url"]):
        raise ValidationError(f"Invalid target URL: {config['target_url']}")
    
    return config 