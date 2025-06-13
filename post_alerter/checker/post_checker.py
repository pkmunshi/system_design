import asyncio
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('post_checker.log')
    ]
)
logger = logging.getLogger(__name__)

async def login_and_get_latest_post(config):
    logger.info("Starting post check process")
    
    # Set up Chrome options
    logger.info("Configuring Chrome options")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Initialize the Chrome driver
    logger.info("Initializing Chrome driver")
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        logger.info("Chrome driver initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize Chrome driver: {str(e)}")
        raise
    
    try:
        # Go to login page
        logger.info(f"Navigating to login page: {config['login_url']}")
        driver.get(config['login_url'])
        
        # Fill in login form
        logger.info("Attempting to fill login form")
        try:
            email_input = driver.find_element(By.NAME, "email")
            password_input = driver.find_element(By.NAME, "password")
            login_button = driver.find_element(By.NAME, "login")
            
            email_input.send_keys(config['username'])
            password_input.send_keys(config['password'])
            logger.info("Login credentials entered successfully")
            
            login_button.click()
            logger.info("Login button clicked")
        except Exception as e:
            logger.error(f"Failed to complete login process: {str(e)}")
            raise

        # Wait for navigation and go to target URL
        today = datetime.today().strftime("%Y-%m-%d")
        logger.info(f"Waiting for page load after login (2 seconds)")
        driver.implicitly_wait(2)
        
        url = config['target_url'].format(date=today)
        logger.info(f"Navigating to target URL: {url}")
        driver.get(url)

        # Wait for page to load
        logger.info("Waiting for page body to load")
        wait = WebDriverWait(driver, 10)
        try:
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            logger.info("Page body loaded successfully")
        except Exception as e:
            logger.error(f"Timeout waiting for page body: {str(e)}")
            raise

        # Get page source and parse with BeautifulSoup
        logger.info("Getting page source")
        page_source = driver.page_source
        logger.info("Parsing page with BeautifulSoup")
        soup = BeautifulSoup(page_source, 'html.parser')

        # Find the post element using the selector
        logger.info(f"Looking for post element with selector: {config['post_selector']}")
        post_element = soup.select_one(config['post_selector'])
        
        if post_element:
            # Extract text content and clean it
            post_text = post_element.get_text(strip=True)
            logger.info("Post content extracted successfully")
            logger.info(f"Extracted post content: {post_text[:100]}...")  # Log first 100 chars
            return post_text
        else:
            logger.warning(f"Could not find post element with selector: {config['post_selector']}")
            return None

    except Exception as e:
        logger.error(f"An error occurred during post check: {str(e)}")
        raise
    finally:
        logger.info("Closing Chrome driver")
        driver.quit()
        logger.info("Chrome driver closed")
