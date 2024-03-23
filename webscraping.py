from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://ubys.bakircay.edu.tr")

input_element = driver.find_element(By.ID, "username")
input_element_1 = driver.find_element(By.ID, "password")
input_element.send_keys("220601126")
input_element_1.send_keys("SetaTerazi2002." + Keys.ENTER)

time.sleep(10)

driver.quit()

