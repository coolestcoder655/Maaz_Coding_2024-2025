from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class CaseOpener():
    def __init__(self):
        service = Service(executable_path="chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.init()

    def init(self):
        self.driver.get("https://kapygames.netlify.app/games/csgo-clicker/csgo-case-clicker-master/")

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "caseTab"))
        )
        self.caseTab = self.driver.find_element(By.ID, "caseTab")
        self.caseTab.click()

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "case3"))
        )

        bravoCase = self.driver.find_element(By.ID, "case3")
        bravoCase.click()

        self.inventoryTab = self.driver.find_element(By.ID, "inventoryTab")
        self.inventoryTab.click()

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventoryItemContainer"))
        )
        self.firstIter = True

    def click(self):
        if self.firstIter:
            clicks = 1239
            self.firstIter = False
        else:
            clicks = 1314
        clicks += 1
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "acceptButton"))
        )
        self.acceptButton = self.driver.find_element(By.ID, "acceptButton")
        for _ in range(1, clicks):
            self.acceptButton.click()


    def buyCase(self):
        self.case = self.driver.find_element(By.ID, "case")
        for _ in range(1, 11):
            self.case.click()
            WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "modalClose"))
            )
            caseClose = self.driver.find_element(By.ID, "modalClose")
            caseClose.click()

caseOpener = CaseOpener()

while True:
    caseOpener.click()
    caseOpener.buyCase()
    sleep(0.5)