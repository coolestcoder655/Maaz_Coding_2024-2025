from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class Sprinter:
	def __init__(self):
		service = Service(executable_path=r"src\chromedriver.exe")
		self.driver = webdriver.Chrome(service=service)

		self.driver.get("https://html5.gamemonetize.games/hh90yoihuo53syyljqu19nalp0zhxued/")
		# self.driver.maximize_window()
		self.beginSprinting()

	def beginSprinting(self):
		"""
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((By.ID, "sdk__splash-button"))
		)

		self.driver.find_element(By.ID, "sdk__splash-button").click()
		time.sleep(15)
		
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((By.ID, "promo-button"))
		)
		self.driver.find_element(By.ID, "promo-button").click()
		print("Clicked on the promo button")

		"""
		time.sleep(30)
		print("Started sprinting")
		

		# canvas = self.driver.find_element(By.XPATH, "//*[@id='container']/canvas")
		canvas = self.driver.find_element(By.TAG_NAME, "canvas")

		while True:
			canvas.send_keys(Keys.ARROW_LEFT)
			canvas.send_keys(Keys.ARROW_RIGHT)

	

spr = Sprinter()