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

class StaffLogin(BaseTest):

    # Test for insert staff in staff page
    def test_staffLogin(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        # driver.get("http://localhost:8000/management/home")
        # driver.find_element_by_link_text("Login Management").click()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Select store to view employees'])[1]/following::span[3]").click()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Date Joined'])[2]/following::input[1]").clear()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Date Joined'])[2]/following::input[1]").send_keys("bris")
        # driver.find_element_by_id("btnStore").click()
        # try: self.assertEqual("E00001", driver.find_element_by_id("mainContent").text)
        # except AssertionError as e: self.verificationErrors.append(str(e))
        # driver.find_element_by_link_text("E00001").click()
        # driver.find_element_by_id("disableBtn").click()
        # try: self.assertEqual("Enable Account", driver.find_element_by_id("enableBtn").text)
        # except AssertionError as e: self.verificationErrors.append(str(e))
        # driver.find_element_by_id("enableBtn").click()
        # ERROR: Caught exception [unknown command []]