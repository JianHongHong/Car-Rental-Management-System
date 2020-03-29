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

class HomeOrder(BaseTest):

    # Test for store in public webpage
    def test_homeOrder(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        # driver.get("http://localhost:8000/")
        # driver.find_element_by_id("select2-pickupStore-container").click()
        # driver.find_element_by_id("select2-returnStore-container").click()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='New user? Sign up'])[1]/following::form[1]").click()
        # driver.find_element_by_id("pickupdate").click()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Su'])[1]/following::td[35]").click()
        # driver.find_element_by_id("returndate").click()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Su'])[1]/following::td[42]").click()
        # driver.find_element_by_id("selectBtn").click()
        # driver.find_element_by_link_text("Please Login").click()
        # driver.find_element_by_id("username").click()
        # driver.find_element_by_id("username").clear()
        # driver.find_element_by_id("username").send_keys("crccurtisl")
        # driver.find_element_by_id("password").click()
        # driver.find_element_by_id("password").clear()
        # driver.find_element_by_id("password").send_keys("test")
        # driver.find_element_by_id("password").send_keys(Keys.ENTER)
        # driver.find_element_by_id("username").click()
        # driver.find_element_by_id("username").clear()
        # driver.find_element_by_id("username").send_keys("crccurtisl")
        # driver.find_element_by_id("password").click()
        # driver.find_element_by_id("password").clear()
        # driver.find_element_by_id("password").send_keys("dev")
        # driver.find_element_by_id("password").send_keys(Keys.ENTER)
        # driver.find_element_by_link_text("Current Cart").click()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Year:'])[2]/following::input[1]").click()
        # driver.find_element_by_id("confirmOrder").click()