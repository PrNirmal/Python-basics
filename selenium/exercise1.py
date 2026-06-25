from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get("https://www.zaubacorp.com/charges")
time.sleep(2)
elem=driver.find_element(By.XPATH,'//*[@id="edit-company-director"]/div[4]/input')
elem.click()
time.sleep(2)
elem2=driver.find_element(By.XPATH,'//*[@id="searchid"]')
elem2.send_keys("villupuram")
elem2.send_keys(Keys.RETURN)
time.sleep(2)
driver.execute_script("window.scrollTo(0, 500)")
driver.find_element(By.XPATH,'//*[@id="results"]/tbody/tr[1]/td[2]/a').click()
