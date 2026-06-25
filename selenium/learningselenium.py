# 1.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # The Keys class provide keys in the keyboard like RETURN, F1, ALT etc
from selenium.webdriver.common.by import By  # used to locate elements within a document
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.python.org")  # The driver.get method will navigate to a page given by the URL
assert ".org" in driver.title  # an assertion to confirm that title has the word “Python” in it
elem = driver.find_element(By.NAME,"q")  # WebDriver offers a number of ways to find elements using the find_element method
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

# unitesting
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

# navigating

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
# Be aware that if your page uses a lot of AJAX on load then WebDriver may not know when it has completely loaded.
# If you need to ensure such pages are fully loaded then you can use waits.
# to find element:
# we can use
# driver.find_element(By.ID, "passwd-id")
# driver.find_element(By.NAME, "passwd")
# driver.find_element(By.XPATH, "//input[@id='passwd-id']")
# driver.find_element(By.CSS_SELECTOR, "input#passwd-id")
element = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
element.send_keys("blastoutsolutions")
element.send_keys("blastoutsolutions",Keys.ENTER)
time.sleep(2)
element.clear()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.nseindia.com/option-chain")
# filling in forms
# option tag   <option value="volvo">Volvo</option>
# there willbe a box and in it we have to we have to choose the option
element = driver.find_element(By.XPATH, '//*[@id="optionchain_equity_sp"]/div/div/div[2]/div[2]/div')
all_options = element.find_elements(By.TAG_NAME, "option")
for option in all_options:
    # print("Value is: %s" % option.get_attribute("value"))
    if "TITAN" == option.get_attribute("value"):
        option.click()

from selenium.webdriver.support.ui import Select

select = Select(driver.find_element(By.ID, "equity_optionchain_select"))
select.select_by_index(1)
# option=select.options
# the above tag is to get all options
# select.deselect_all()
# this is for multiple select option like checkbox
all_option = select.all_selected_options
select.select_by_visible_text("NIFTY")
select.select_by_value("BANKNIFTY")

# drag and drop
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/draggable/")
driver.maximize_window()
source1 = driver.find_element(By.ID,'draggable')
target1 = driver.find_element(By.ID,'droppable')
from selenium.webdriver import ActionChains

action_Chains = ActionChains(driver)
action_Chains.drag_and_drop(source1, target1).perform()

# switch window
driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/python/")
driver.find_element(By.XPATH, '//*[@id="main"]/div[4]/a').click()
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH, '//*[@id="w3-exerciseform"]/div/p[2]/a').click()
driver.switch_to.window(driver.window_handles[0])
# 0 for the first window and 1 for second window

# frame to frame
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# to maximize the browser window
driver.maximize_window()
# get method to launch the URL
driver.get("https://the-internet.herokuapp.com")
# to refresh the browser
driver.refresh()
driver.find_element(By.LINK_TEXT, "Frames").click()
driver.find_element(By.LINK_TEXT, "Nested Frames").click()
# to switch to frame with frame name
driver.switch_to.frame("frame-bottom")
# to get the text inside the frame and print on console
# to move out the current frame to the page level
driver.switch_to.default_content()
# to close the browser
# driver.quit()

# need to learn..........

# navigation:

driver.back()  # which means used to go back <--
driver.forward()  # which means used to go forward -->

# cookies
driver = webdriver.Chrome()
driver.get("http://www.example.com")

# Now set the cookie. This one's valid for the entire domain
cookie = {'name': 'foo', 'value': 'bar'}
driver.add_cookie(cookie)

# And now output all the available cookies for the current URL
driver.get_cookies()
driver.delete_all_cookies()

# locating elements by:
# ID = "id"
# NAME = "name"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"


# by hyper link (continue_link = driver.find_element(By.LINK_TEXT, 'Continue')
# (continue_link = driver.find_element(By.LINK_TEXT, 'Continue')

# explicitly wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://somedomain/url_that_delays_loading")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()

# page down

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.blastoutsolutions.com/")
# driver.execute_script("window.scrollTo(0, 500);")# (0,500) the first parameter is for horizontal movement and the second for vertical
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# action driver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.get("https://campus.w3schools.com/collections/course-catalog/products/w3schools-full-access-course")
the_menu=driver.find_element(By.XPATH,'//*[@id="site-header-nav"]/nav/ul/li[3]/details/summary')
the_submenu=driver.find_element(By.XPATH,'//*[@id="site-header-nav"]/nav/ul/li[3]/details/ul/li[1]/a')
ActionChains(driver).move_to_element(the_menu).click(the_submenu).perform()
# or
driver=webdriver.Chrome()
driver.get("https://campus.w3schools.com/collections/course-catalog/products/w3schools-full-access-course")
action=ActionChains(driver)
the_menu=driver.find_element(By.XPATH,'//*[@id="site-header-nav"]/nav/ul/li[3]/details/summary')
the_submenu=driver.find_element(By.XPATH,'//*[@id="site-header-nav"]/nav/ul/li[3]/details/ul/li[3]/a')
action.move_to_element(the_menu)
# action.click(the_submenu)
action.click(on_element=the_submenu)
# action.click(on_element=None)# If None, clicks on current mouse position.
action.perform()


# click and hold
driver=webdriver.Chrome()
driver.get("https://campus.w3schools.com/collections/course-catalog/products/w3schools-full-access-course")
action=ActionChains(driver)
the_menu=driver.find_element(By.XPATH,'//*[@id="site-header-nav"]/nav/ul/li[3]/details/summary')
the_submenu=driver.find_element(By.XPATH,'//*[@id="site-header-nav"]/nav/ul/li[3]/details/ul/li[3]/a')
action.move_to_element(the_menu)
action.click_and_hold(the_submenu) # the menu will hold until you perform the action
# action.click_and_hold(on_element=None) #If None, clicks on current mouse position.
action.perform()

# context_click:
driver=webdriver.Chrome()
driver.get("https://campus.w3schools.com/collections/course-catalog/products/w3schools-full-access-course")
action=ActionChains(driver)
the_menu=driver.find_element(By.XPATH,'//*[@id="site-header-nav"]/nav/ul/li[3]/details/summary')
the_submenu=driver.find_element(By.XPATH,'//*[@id="site-header-nav"]/nav/ul/li[3]/details/ul/li[3]/a')
action.move_to_element(the_menu)
action.context_click(the_submenu) # The element to context-click
# If None, clicks on current mouse position.
action.perform()

# drag and drop
# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
# create webdriver object
driver = webdriver.Chrome()
# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
# get element
element1 = driver.find_element(By.LINK_TEXT,"Courses")
# create action chain object
action = ActionChains(driver)
# drag_and_drop_by_offset the item
action.drag_and_drop_by_offset(element1, 100, 200)
# perform the operation
action.perform()


# key_down action

#This article revolves around key_down method on Action Chains in Python Selenium.
# key_down method is used to send a key press, without releasing it.
# this method is used in case one wants to press, ctrl+c, or ctrl+v
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("http://www.blastmediasolutions.com/")
driver.maximize_window()
action = ActionChains(driver)
action.key_down(Keys.CONTROL).send_keys('U').key_up(Keys.CONTROL).perform()


# json,csv
# file modes
# string io
# itertools
# map
# filter

# regular expression(text processing)
# pandas
# file handling
# selenium
# beautifulsoup
# os module
# problemsolving ability

# for tutorial

# python documentation
# real python blog
# python engineer
# pypi
# python library reference

# blackbox-AI
# corey schafer-youtube

# naukri,linkedin,monster

