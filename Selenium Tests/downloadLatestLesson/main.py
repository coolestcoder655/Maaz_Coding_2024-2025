from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from json import load

# Setup Chrome WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Read credentials from file
with open(r"downloadLatestLesson\confidential.json", "r") as file:
    credentials = load(file)
    username = credentials["email"]
    password = credentials["password"]

# Open OneDrive login page
driver.get("https://onedrive.live.com/")

# Click on the "Sign In" button if it exists
try:
    signInButton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
    )
    signInButton.click()
except:
    print("Sign-in button not found, proceeding directly...")

# Wait for the email input field
emailInput = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "loginfmt"))
)
emailInput.send_keys(username + Keys.ENTER)

# Wait for the password field
passwordInput = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "passwd"))
)
passwordInput.send_keys(password + Keys.ENTER)

# Optional: Handle "Stay signed in?" prompt
try:
    staySignedIn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "idSIButton9"))
    )
    staySignedIn.click()
except:
    print("No 'Stay signed in?' prompt detected.")

# Wait a few seconds to ensure login completes
sleep(5)

# Now, you should be logged into OneDrive!
print("Login successful!")

# You can now interact with OneDrive or navigate to files
