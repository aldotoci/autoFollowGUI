from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import random

cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False

class Bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(capabilities=cap, executable_path='./geckodriver')
        self.login()

    def waitForElementXPATH(self, elementAddress):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.visibility_of_element_located((By.XPATH, elementAddress)))
        time.sleep(random.randint(1,3))
        return element
    
    def waitForElementCSS_Selectori(self, elementAddress):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, elementAddress)))
        time.sleep(random.randint(1,3))
        return element

    def login(self):
        self.driver.get("https://www.instagram.com/")
        #time.sleep(5)
        user_name_elem = self.waitForElementXPATH("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passwarword_elem = self.waitForElementXPATH("//input[@name='password']")
        passwarword_elem.clear()
        passwarword_elem.send_keys(self.password)
        passwarword_elem.send_keys(Keys.RETURN)
        time.sleep(random.randint(8,12))
    
    def follow(self, username):
        self.driver.get(f'https://www.instagram.com/{username}/')

        try:
            followButton = self.waitForElementXPATH('//button[@class="_acan _acap _acas"]')
            followButton.click()
            time.sleep(3)
            return True
        except:
            print('USR DNE || Already Followed')
            return False