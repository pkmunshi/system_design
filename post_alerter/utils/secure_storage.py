import os
import json
from cryptography.fernet import Fernet
from base64 import b64encode, b64decode, urlsafe_b64encode
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class SecureStorage:
    def __init__(self, encryption_key=None):
        """Initialize secure storage with encryption key."""
        if encryption_key:
            try:
                # First, ensure we have a valid Fernet key
                if len(encryption_key) != 44:  # Fernet keys are 32 bytes, base64 encoded = 44 chars
                    # If the key is not the right length, generate a new one
                    logger.warning("Invalid key length, generating new key")
                    self.key = Fernet.generate_key()
                else:
                    # Try to decode and re-encode to ensure it's valid
                    try:
                        # First try direct use
                        self.key = encryption_key.encode()
                        # Test if it works
                        Fernet(self.key)
                    except Exception:
                        # If that fails, try to fix the padding
                        try:
                            # Add padding if needed
                            key_bytes = encryption_key.encode()
                            padding = 4 - (len(key_bytes) % 4)
                            if padding != 4:
                                key_bytes += b'=' * padding
                            # Convert to URL-safe base64
                            self.key = urlsafe_b64encode(b64decode(key_bytes))
                            # Test if it works
                            Fernet(self.key)
                        except Exception as e:
                            logger.error(f"Failed to process encryption key: {str(e)}")
                            # Generate a new key if all attempts fail
                            self.key = Fernet.generate_key()
            except Exception as e:
                logger.error(f"Error processing encryption key: {str(e)}")
                self.key = Fernet.generate_key()
        else:
            self.key = Fernet.generate_key()
            
        self.cipher_suite = Fernet(self.key)
        logger.info("SecureStorage initialized successfully")
        
    def encrypt(self, data):
        """Encrypt data before storage."""
        if isinstance(data, str):
            data = data.encode()
        return self.cipher_suite.encrypt(data)
    
    def decrypt(self, encrypted_data):
        """Decrypt stored data."""
        return self.cipher_suite.decrypt(encrypted_data).decode()
    
    def save_encrypted(self, data, filepath):
        """Save encrypted data to file."""
        try:
            encrypted_data = self.encrypt(data)
            with open(filepath, 'wb') as f:
                f.write(encrypted_data)
            logger.debug(f"Data encrypted and saved to {filepath}")
        except Exception as e:
            logger.error(f"Failed to save encrypted data: {str(e)}")
            raise
    
    def load_encrypted(self, filepath):
        """Load and decrypt data from file."""
        try:
            if not os.path.exists(filepath):
                return None
            with open(filepath, 'rb') as f:
                encrypted_data = f.read()
            return self.decrypt(encrypted_data)
        except Exception as e:
            logger.error(f"Failed to load encrypted data: {str(e)}")
            raise

    def save_diff(self, old_post, new_post, filepath):
        """Save encrypted diff with timestamp."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        diff_content = {
            "timestamp": timestamp,
            "old_post": old_post,
            "new_post": new_post
        }
        self.save_encrypted(json.dumps(diff_content), filepath)
        return diff_content 