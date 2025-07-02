from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
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

# 🛠 Setup WebDriver with automatic ChromeDriver management
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# 🏁 Go to race page
driver.get("https://www.nitrotype.com/race")
time.sleep(10)  # Wait for race to load fully

# 🔍 Wait for race to be ready and find input box
print("🔍 Looking for input box...")
input_box = None
max_attempts = 20
attempt = 0

while attempt < max_attempts and input_box is None:
    try:
        # Try different possible selectors for the input box
        selectors = [
            ".dash-input",
            "input[type='text']",
            ".race-input",
            "#input",
            "input.dash-input",
            "textarea",
            "[contenteditable='true']"
        ]
        
        for selector in selectors:
            try:
                input_box = driver.find_element(By.CSS_SELECTOR, selector)
                print(f"✅ Found input box with selector: {selector}")
                break
            except:
                continue
                
        if input_box is None:
            print(f"⏳ Attempt {attempt + 1}/{max_attempts} - Input box not found, waiting...")
            time.sleep(2)
            attempt += 1
    except Exception as e:
        print(f"❌ Error on attempt {attempt + 1}: {e}")
        time.sleep(2)
        attempt += 1

if input_box is None:
    print("❌ Could not find input box after multiple attempts")
    print("🔍 Available elements on page:")
    # Debug: Print some elements to see what's available
    try:
        all_inputs = driver.find_elements(By.TAG_NAME, "input")
        print(f"Found {len(all_inputs)} input elements")
        for i, inp in enumerate(all_inputs[:5]):  # Show first 5
            print(f"  Input {i+1}: class='{inp.get_attribute('class')}', type='{inp.get_attribute('type')}'")
    except:
        pass
    
    try:
        all_textareas = driver.find_elements(By.TAG_NAME, "textarea")
        print(f"Found {len(all_textareas)} textarea elements")
    except:
        pass
    
    driver.quit()
    exit()

# 🧠 Get race text
print("🧠 Getting race text...")
text_spans = driver.find_elements(By.CSS_SELECTOR, ".dash-copy > span")
if not text_spans:
    # Try alternative selectors for race text
    alternative_selectors = [
        ".race-text span",
        ".typing-text span",
        ".quote span",
        "[data-testid='race-text'] span"
    ]
    
    for selector in alternative_selectors:
        text_spans = driver.find_elements(By.CSS_SELECTOR, selector)
        if text_spans:
            print(f"✅ Found race text with selector: {selector}")
            break

race_text = ''.join([span.text for span in text_spans])
print("Race Text:", race_text)

if not race_text.strip():
    print("❌ No race text found - the race might not have started yet")
    driver.quit()
    exit()

# 🏆 Find longest word
words = race_text.split()
longest_word = max(words, key=len)
print("Longest word for Nitro:", longest_word)

# ⌨️ Start typing the race text
print("⌨️ Starting to type...")
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

# 🔚 Close the browser
time.sleep(3)
driver.quit()