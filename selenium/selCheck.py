from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup Chrome
driver = webdriver.Chrome()  # Or specify path: webdriver.Chrome(executable_path="path/to/chromedriver")

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Wait for manual QR code scan
print("Scan QR code and press Enter...")
input()

# Replace with the exact name of the chat (case-sensitive)
target_name = "subashini akka"  # <- Change this

# Search and open the chat
search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
search_box.click()
search_box.send_keys(target_name)
time.sleep(2)  # Let the search populate
search_box.send_keys(Keys.ENTER)

# Now send "hlo" 1000 times
for _ in range(100):
    message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    message_box.send_keys("Hey suba")
    message_box.send_keys(Keys.ENTER)
    time.sleep(0.1)  # Optional small delay
