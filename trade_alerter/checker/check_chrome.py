import platform
import subprocess
import sys
from pathlib import Path

def check_chrome_installation(config=None):
    """Check if Chrome browser is installed on the system.
    
    Args:
        config (dict, optional): Configuration dictionary. Not used in this function
            but included for compatibility with other functions.
    """
    system = platform.system()
    
    if system == "Darwin":  # macOS
        chrome_paths = [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            str(Path.home() / "Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
        ]
    elif system == "Windows":
        chrome_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            str(Path.home() / "AppData/Local/Google/Chrome/Application/chrome.exe")
        ]
    else:  # Linux
        chrome_paths = [
            "/usr/bin/google-chrome",
            "/usr/bin/google-chrome-stable",
            "/snap/bin/google-chrome"
        ]

    # Check if Chrome exists in any of the expected paths
    for path in chrome_paths:
        if Path(path).exists():
            try:
                # Try to get Chrome version
                if system == "Windows":
                    result = subprocess.run([path, "--version"], capture_output=True, text=True)
                else:
                    result = subprocess.run([path, "--version"], capture_output=True, text=True)
                
                version = result.stdout.strip()
                print(f"✅ Chrome is installed: {version}")
                return True
            except Exception as e:
                print(f"Found Chrome at {path} but couldn't get version: {e}")
                return True

    print("❌ Chrome is not installed")
    print("\nInstallation instructions:")
    if system == "Darwin":
        print("1. Visit https://www.google.com/chrome/")
        print("2. Download and install Chrome for Mac")
    elif system == "Windows":
        print("1. Visit https://www.google.com/chrome/")
        print("2. Download and install Chrome for Windows")
    else:
        print("For Ubuntu/Debian:")
        print("sudo apt-get update")
        print("sudo apt-get install -y google-chrome-stable")
        print("\nFor Fedora:")
        print("sudo dnf install google-chrome-stable")
    
    return False

if __name__ == "__main__":
    check_chrome_installation() 