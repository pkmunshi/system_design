from cryptography.fernet import Fernet
from base64 import b64encode
import os

def generate_key():
    """Generate a secure encryption key."""
    # Generate a new Fernet key
    key = Fernet.generate_key()
    
    # Print the key in a format that can be directly used in .env file
    print("\nGenerated Encryption Key:")
    print("------------------------")
    print(f"ENCRYPTION_KEY={key.decode()}")
    print("\nAdd this key to your .env file and GitHub secrets.")
    print("IMPORTANT: Keep this key secure and never commit it to version control!")
    
    return key

if __name__ == "__main__":
    generate_key() 