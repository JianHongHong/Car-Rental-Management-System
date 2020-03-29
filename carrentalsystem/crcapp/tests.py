from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
import unittest, time, re, os, platform

class BaseTest(TestCase):
    def setUp(self):
        PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
        if platform.system() == 'Darwin':
            DRIVER = os.path.join(PROJECT_ROOT, "../drivers/chromedriver")
        elif platform.system() == 'Windows':
            DRIVER = os.path.join(PROJECT_ROOT, "../drivers/chromedriver.exe")
        
        options = Options()
        options.add_argument('--headless') # comment this out to show chrome windows runnning
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(DRIVER,chrome_options=options)
        # self.driver.fullscreen_window() # To check everything works in fullscreen
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
