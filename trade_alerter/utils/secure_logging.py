import logging
import sys
import re
from datetime import datetime
import os

class SensitiveDataFilter(logging.Filter):
    """Filter to mask sensitive data in log messages."""
    
    def __init__(self):
        super().__init__()
        # Patterns for sensitive data
        self.patterns = [
            (r'password["\']?\s*[:=]\s*["\']?[^"\']+["\']?', 'password="****"'),
            (r'TO_SMS_NUMBER["\']?\s*[:=]\s*["\']?[^"\']+["\']?', 'TO_SMS_NUMBER="****"'),
            (r'GMAIL_APP_PASSWORD["\']?\s*[:=]\s*["\']?[^"\']+["\']?', 'GMAIL_APP_PASSWORD="****"'),
            (r'TRADE_PASSWORD["\']?\s*[:=]\s*["\']?[^"\']+["\']?', 'TRADE_PASSWORD="****"'),
        ]
    
    def filter(self, record):
        """Filter sensitive data from log messages."""
        if isinstance(record.msg, str):
            for pattern, replacement in self.patterns:
                record.msg = re.sub(pattern, replacement, record.msg)
        return True

def setup_logging(log_level=logging.INFO):
    """Set up secure logging configuration."""
    # Create logs directory if it doesn't exist
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Generate log filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d')
    log_file = os.path.join(log_dir, f'post_checker_{timestamp}.log')
    
    # Configure logging
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    # Add sensitive data filter to all handlers
    sensitive_filter = SensitiveDataFilter()
    for handler in logging.getLogger().handlers:
        handler.addFilter(sensitive_filter)
    
    # Set specific loggers
    logging.getLogger('urllib3').setLevel(logging.WARNING)
    logging.getLogger('selenium').setLevel(logging.WARNING)
    
    return logging.getLogger(__name__) 