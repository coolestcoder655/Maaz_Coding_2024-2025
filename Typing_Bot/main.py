from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

"""
driver.get("https://google.com")

inputElement = driver.find_element(By.CLASS_NAME, "gLFyf")
inputElement.send_keys("apple", Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

"""

with open("confidential.txt", "r") as file:
    lines = []
    for line in file:
        line.strip()
        lines.append(line)

    username = lines[0]
    passcode = lines[1]

class TypingBot():
    def __init__(self):
        self.service = Service(executable_path="chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)

    def login(self):
        self.driver.get("https://launchpad.classlink.com/")
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search-bar-input"))
        )
        link = self.driver.find_element(By.CLASS_NAME, "search-bar-input")
        link.send_keys("lewisville isd")

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "dropdown-list-item"))
        )
        lewisvilleIsd = self.driver.find_element(By.CLASS_NAME, "dropdown-list-item")
        lewisvilleIsd.click()

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "username"))
        )

        loginInput = self.driver.find_element(By.ID, "username")
        loginInput.send_keys(username + Keys.TAB + passcode + Keys.ENTER)


        element = self.driver.find_element("xpath", "//div[text()='Typing.com']")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Typing.com"))
        )

        typingapp = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Typing.com")
        typingapp.click()

        """
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "left-icon ng-untouched ng-pristine ng-valid"))
        )

        appInput = self.driver.find_element(By.CLASS_NAME, "left-icon ng-untouched ng-pristine ng-valid")
        appInput.send_keys("Typing.com")

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Typing.com"))
        )

        typingAppLink = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Typing.com")
        typingAppLink.click()"

        """


bot = TypingBot()
bot.login()
sleep(60)
