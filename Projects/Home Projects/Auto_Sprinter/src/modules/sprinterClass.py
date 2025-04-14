from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Sprinter:
	def __init__(self):
		service = Service(executable_path=r"src\modules\chromedriver.exe")
		driver = webdriver.Chrome(service=service)

		driver.get("https://seraphv11.netlify.app/games/sprinter/")

		time.sleep(10)

		driver.quit()

spt = Sprinter()