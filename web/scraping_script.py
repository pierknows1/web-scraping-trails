from selenium import webdriver
from selenium.webdriver.common.by import By
import time

webdriver_path = "C:/Users/pierr/OneDrive/Desktop/WebScraping/chromedriver.exe"
chrome_beta_path = "C:/Program Files/Google/Chrome Beta/Application/chrome.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_beta_path

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.wikiloc.com/wikiloc/map.do?sw=-89.9995139%2C-179.999&ne=89.999%2C179.999&page=1')

# Wait for the page to load
time.sleep(1)

# Locate the "Sign up" button and click it
sign_up_button = driver.find_element(By.XPATH, '//a[contains(@class, "header__signup-btn")]')
sign_up_button.click()

# Add a delay for observation (optional)
time.sleep(50)

driver.quit()
