from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import random
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Now you can access the variables using os.getenv
# USERNAME = os.getenv("USERNAME")
# PASSWORD = os.getenv("PASSWORD")

USERNAME = "imamnotabot1"
PASSWORD = "imamnotabot"

# 🛠 Setup WebDriver from current directory
driver_path = "./chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# 🌐 Open Nitro Type
driver.get("https://www.nitrotype.com")

# 🕒 Wait and click Log In
time.sleep(3)
login_button = driver.find_element(By.LINK_TEXT, "Log In")
login_button.click()

# 🧑‍💻 Fill in login credentials
time.sleep(2)
driver.find_element(By.NAME, "username").send_keys(USERNAME)
driver.find_element(By.NAME, "password").send_keys(PASSWORD)
driver.find_element(By.XPATH, "//button[text()='Log In']").click()

# 🕐 Wait for login to finish and redirect
time.sleep(5)

# 🏁 Go to race page
driver.get("https://www.nitrotype.com/race")
time.sleep(10)  # Wait for race to load fully

# 🧠 Get race text
text_spans = driver.find_elements(By.CSS_SELECTOR, ".dash-copy > span")
race_text = ''.join([span.text for span in text_spans])
print("Race Text:", race_text)

# 🏆 Find longest word
words = race_text.split()
longest_word = max(words, key=len)
print("Longest word for Nitro:", longest_word)

# ⌨️ Find input box and start typing
input_box = driver.find_element(By.CLASS_NAME, "dash-input")

for word in words:
    if word == longest_word:
        input_box.send_keys(Keys.ENTER)  # Nitro before longest word
        print("💥 Nitro used!")

    for char in word:
        input_box.send_keys(char)
        time.sleep(random.uniform(0.05, 0.12))
    input_box.send_keys(" ")
    time.sleep(random.uniform(0.03, 0.08))

print("✅ Race complete!")