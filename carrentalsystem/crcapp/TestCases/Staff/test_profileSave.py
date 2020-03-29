import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, os, platform
from crcapp.tests import BaseTest

class ProfileSave(BaseTest):

    # Test for insert staff in staff page
    def test_staffProfileSave(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        # driver.get("http://localhost:8000/management/home")
        # driver.find_element_by_link_text("Profile").click()
        # driver.find_element_by_id("TFN").click()
        # driver.find_element_by_id("TFN").clear()
        # driver.find_element_by_id("TFN").send_keys("12345678")
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Email Address'])[1]/following::button[1]").click()
        # driver.find_element_by_link_text("Security Information").click()
        # driver.find_element_by_id("password").click()
        # driver.find_element_by_id("confpassword").clear()
        # driver.find_element_by_id("confpassword").send_keys("test")
        # driver.find_element_by_id("password").click()
        # driver.find_element_by_id("password").click()
        # # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=password | ]]
        # driver.find_element_by_id("password").clear()
        # driver.find_element_by_id("password").send_keys("dev")
        # driver.find_element_by_id("confpassword").clear()
        # driver.find_element_by_id("confpassword").send_keys("dev")
        # driver.find_element_by_id("pwsave").click()
        # ERROR: Caught exception [unknown command []]
        # ERROR: Caught exception [unknown command []]