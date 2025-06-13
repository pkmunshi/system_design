import os
from dotenv import load_dotenv
import json
from main import load_config

def test_environment():
    """Test if all required environment variables are set."""
    print("Testing environment variables...")
    
    # Load environment variables
    load_dotenv()
    
    # List of required environment variables
    required_vars = [
        "TRADE_USERNAME",
        "TRADE_PASSWORD",
        "FROM_EMAIL",
        "GMAIL_APP_PASSWORD",
        "TO_SMS_NUMBER",
        "TO_EMAILS"
    ]
    
    # Check each variable
    missing_vars = []
    for var in required_vars:
        value = os.getenv(var)
        if value:
            # Mask sensitive values
            if var in ["TRADE_PASSWORD", "GMAIL_APP_PASSWORD"]:
                print(f"✓ {var} is set (value masked)")
            else:
                print(f"✓ {var} is set")
        else:
            missing_vars.append(var)
            print(f"✗ {var} is not set")
    
    if missing_vars:
        print("\nMissing environment variables:")
        for var in missing_vars:
            print(f"- {var}")
        return False
    
    print("\nAll environment variables are set!")
    return True

def test_config_loading():
    """Test if configuration can be loaded correctly."""
    print("\nTesting configuration loading...")
    try:
        config = load_config()
        print("✓ Configuration loaded successfully")
        
        # Verify config structure
        required_keys = ["login_url", "target_url", "post_selector", "username", "password"]
        for key in required_keys:
            if key in config:
                print(f"✓ Config contains {key}")
            else:
                print(f"✗ Config missing {key}")
                return False
        
        return True
    except Exception as e:
        print(f"✗ Failed to load configuration: {str(e)}")
        return False

if __name__ == "__main__":
    print("Starting environment and configuration tests...\n")
    
    env_ok = test_environment()
    config_ok = test_config_loading()
    
    print("\nTest Summary:")
    print(f"Environment Variables: {'✓ PASS' if env_ok else '✗ FAIL'}")
    print(f"Configuration Loading: {'✓ PASS' if config_ok else '✗ FAIL'}")
    
    if env_ok and config_ok:
        print("\nAll tests passed! The environment is properly configured.")
    else:
        print("\nSome tests failed. Please check the errors above.") 