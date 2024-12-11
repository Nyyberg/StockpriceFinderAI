# filename: tool.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time

def handle_cookies(driver: webdriver.Chrome):
    try:
        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "L2AGLb"))
        )
        cookie_button.click()
    except:
        print("No cookie consent prompt found or handled.")

def get_stock_price(query: str):
    # Set up Chrome options to run in headless mode

    # Create a new instance of the Chrome driver
    
    driver = webdriver.Chrome()
    driver.get(f"https://www.google.com/search?client=firefox-b-d&q={query}")
    handle_cookies(driver)

    try:
        # Navigate to Google Finance
       

        # Wait for the stock price element to load
        stock_price_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div[13]/div[3]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[3]/g-card-section/div/g-card-section/div[2]/div[1]/span[1]/span/span[1]"))
        )

        # Extract the current value of the stock
        stock_price = stock_price_element.text.strip()

        return stock_price

    except TimeoutException:
        print("Failed to load stock price")
        driver.quit()
        return None

    finally:
        # Close the browser window
        driver.quit()

if __name__ == "__main__":
    stock_price = get_stock_price()
    if stock_price:
        print(f"Current value of stock: ${stock_price}")
