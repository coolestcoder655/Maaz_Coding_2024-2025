import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Setup Chrome
service = webdriver.chrome.service.Service("chromedriver.exe")
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options, service=service)

# Open site
driver.get("http://quotes.toscrape.com")

# Prepare CSV file
with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author", "Tags"]) # CSV headers
    
    while True:
        # Scrape quotes on current page
        quotes = driver.find_elements(By.CLASS_NAME, "quote")
        for quote in quotes:
            text = quote.find_element(By.CLASS_NAME, "text").text
            author = quote.find_element(By.CLASS_NAME, "author").text
            tags = [tag.text for tag in quote.find_elements(By.CLASS_NAME, "tag")]
            writer.writerow([text, author, ", ".join(tags)])
    
        # Try to click "Next"
        try:
            next_button = driver.find_element(By.CLASS_NAME, "next")
            next_button.find_element(By.TAG_NAME, "a").click()
            time.sleep(1) # Wait for next page to load
        except:
            print("Scraping completed. No more pages.")
            break
        
driver.quit()