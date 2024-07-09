import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import psutil
import time

# Load test environment variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env.test'))

def get_dynamic_wait_time():
    """Dynamically calculate the wait time based on system metrics."""
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent

    # Assume a base wait time of 10 seconds
    base_wait_time = 10

    # Adjust wait time based on CPU usage
    if cpu_usage > 75:
        base_wait_time += 5  # Add 5 seconds if CPU usage is high

    # Adjust wait time based on memory usage
    if memory_usage > 75:
        base_wait_time += 5  # Add 5 seconds if memory usage is high

    # Adjust wait time based on network performance (simple ping check)
    try:
        response = os.system("ping -c 1 google.com")
        if response != 0:
            base_wait_time += 5  # Add 5 seconds if network is slow
    except Exception as e:
        base_wait_time += 5  # Add 5 seconds if ping fails

    return base_wait_time

class TestUser(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1200")
        chrome_options.add_argument("--remote-debugging-port=9222")
        
        # Explicitly set the Chrome binary location if needed
        chrome_path = "/usr/bin/google-chrome"  # Adjust if needed
        if os.path.exists(chrome_path):
            chrome_options.binary_location = chrome_path

        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

    def test_user_interaction(self):
        driver = self.driver
        driver.get("https://example.com")  # Replace with the URL you want to test

        # Capture a screenshot for debugging
        driver.save_screenshot("screenshot.png")

        wait_time = get_dynamic_wait_time()

        # Example: Simulate user action to search for something on the page
        try:
            search_box = WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )
            search_box.send_keys("Selenium WebDriver")
            search_box.send_keys(Keys.RETURN)
        except Exception as e:
            print(f"Exception: {e}")
            driver.save_screenshot("error_screenshot.png")
            raise

        # Check the result page
        try:
            WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Selenium WebDriver')]"))
            )
        except Exception as e:
            print(f"Exception: {e}")
            driver.save_screenshot("result_page_error.png")
            raise

        # Example: Simulate clicking a link or button
        try:
            link = WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Documentation"))  # Adjust the element locator as needed
            )
            link.click()
        except Exception as e:
            print(f"Exception: {e}")
            driver.save_screenshot("link_click_error.png")
            raise

        # Check that the new page contains expected content
        try:
            WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Selenium')]"))
            )
        except Exception as e:
            print(f"Exception: {e}")
            driver.save_screenshot("final_page_error.png")
            raise

if __name__ == '__main__':
    unittest.main()
