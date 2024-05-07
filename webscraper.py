""" WEB SCRAPER CODE USING SELENIUM AND PYTHON """

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://www.URL.here")

# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Find elements on the page
titles = driver.find_elements(By.CSS_SELECTOR, "h1")
links = driver.find_elements(By.CSS_SELECTOR, "a")

# Extract data from the elements
for title in titles:
    print("Title:", title.text)

for link in links:
    print("Link:", link.get_attribute("href"))

# Close the browser
driver.quit()
