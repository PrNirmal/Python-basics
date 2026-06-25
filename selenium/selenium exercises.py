# basics
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()#will maximize the site
element=driver.find_element(By.NAME,"q")
element.clear()
element.send_keys("blastout Solutions1",Keys.BACKSPACE,Keys.ARROW_DOWN,Keys.ENTER)
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
# element.send_keys(Keys.BACKSPACE) #you can also do like this
# element.send_keys(Keys.ARROW_DOWN)
# time.sleep(2)
# element.send_keys(Keys.ENTER)
driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div[1]/div/a").click()
driver.close()

# driver.implicitly_wait(5) doubt


#2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()#used to delete all cookies
driver.get("https://www.gmail.com")
element=driver.find_element(By.ID,"identifierId")
element.send_keys("prnirmalramesh04@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='identifierNext']/div/button/span").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='next']/div/div/a").click()# to click the button
driver.find_element(By.XPATH,"/html/body/header/div/div/div/a[2]").click()
element2=driver.find_element(By.NAME,"identifier")
element2.send_keys("prnirmalramesh04@gmail.com")
driver.find_element(By.XPATH,"//*[@id='identifierNext']/div/button/span").click()
print("cant able to do")
#close the browser
driver.close()


# 3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSemo8qw_TnB02KVdQ0NqtNdPwp41RMCu4x4tLrTQBdSZ3oO7Q/viewform?usp=sf_link")
time.sleep(5)
list_1=["Nirmal","prnirmalramesh04@gmail.com","7708619166","11,a.t.k nagar","19"]

namebox=driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
namebox.send_keys(list_1[0])
namebox.send_keys(Keys.TAB)
mailbox=driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
mailbox.send_keys(list_1[1])
mailbox.send_keys(Keys.TAB)
phonebox=driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
phonebox.send_keys(list_1[2])
phonebox.send_keys(Keys.TAB)
addbox=driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea")
addbox.send_keys(list_1[3])
addbox.send_keys(Keys.TAB)
agebox=driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input")
agebox.send_keys(list_1[4])
agebox.send_keys(Keys.TAB)
opbox=driver.find_element(By.XPATH,"//*[@id='i25']/div[3]/div")
opbox.click()
driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span").click()

driver.minimize_window()
driver.close()

# simplified code to fill the form


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSemo8qw_TnB02KVdQ0NqtNdPwp41RMCu4x4tLrTQBdSZ3oO7Q/viewform?usp=sf_link")
time.sleep(5)
list_1=["//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input",
        "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input",
        "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input",
        "//*[@id='mG61Hd']/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea",
        "//*[@id='mG61Hd']/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input"]
list_2=["ram","prnih04@gmail.com","7703486191","11,a.p.k nagar","41"]
for i in range(len(list_1)):
    fillbox=driver.find_element(By.XPATH,list_1[i])
    fillbox.send_keys(list_2[i])

opbox=driver.find_element(By.XPATH,"//*[@id='i28']/div[3]/div")
opbox.click()
driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span").click()
time.sleep(10)
driver.minimize_window()
driver.close()



# 4.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()
driver.get("https://www.nseindia.com/option-chain")
main_div=driver.find_element(By.CSS_SELECTOR,"#optionchain_equity_sp > div > div > div.row.mt-2.filterMaxWid > div:nth-child(3) > div")
all_options=main_div.find_elements(By.TAG_NAME,"option")
for option in all_options:
    if "ABCAPITAL"==option.get_attribute("text"):
        option.click()

select2=Select(driver.find_element(By.ID,"expirySelect"))
select2.select_by_index(2)

select2=Select(driver.find_element(By.ID,"strikeSelect"))
select2.select_by_visible_text("9,000.00")

driver.find_element(By.ID,"downloadOCTable").click()

# 5.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()
driver.get("https://www.globalsqa.com/cheatsheets/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Pandas Cheat Sheet").click()
# driver.find_element(By.XPATH,'//*[@id="post-6725"]/div/div/div/div[2]/a[2]').click()
driver.switch_to.window(driver.window_handles[0])


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")
driver.get("http://www.google.com")
sleep(4)
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("sample login")
sleep(4)
elem.send_keys(Keys.RETURN)
sleep(4)
driver.find_element(By.XPATH, "/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/a/h3").click()
sleep(4)
driver.find_element(By.NAME, "email").send_keys("abc@gmail.com")
sleep(4)
driver.find_element(By.NAME, "password").send_keys("1234")
sleep(4)
driver.find_element(By.XPATH,"/html/body/div/div/form/div[1]/div[3]").click()
sleep(4)


# selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.get("https://filesamples.com/formats/pdf")
thexpath=['//*[@id="output"]/div[1]/a','//*[@id="output"]/div[2]/a','//*[@id="output"]/div[3]/a']
driver.maximize_window()
driver.execute_script("window.scrollTo(0,500);")
for i in range(len(thexpath)):
    driver.find_element(By.XPATH,thexpath[i]).click()
    sleep(3)
driver.close()
import shutil
the_path="C:/Users/prnir/Downloads/"
thedes="E:/selenium files/"
thefiles=["sample3.pdf","sample2.pdf"]
for i in range(len(thefiles)):
    themain=the_path+thefiles[i]
    thedes2=thedes+thefiles[i]
    shutil.move(themain,thedes2)