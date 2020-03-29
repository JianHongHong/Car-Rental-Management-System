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

class InsertStaff(BaseTest):

    # Test for insert staff in staff page
    def test_staffInsert(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        # driver.get("http://localhost:8000/management/home")
        # driver.find_element_by_link_text("Register New Staff Member").click()
        # driver.find_element_by_id("firstName").clear()
        # driver.find_element_by_id("firstName").send_keys("Test")
        # driver.find_element_by_id("lastName").clear()
        # driver.find_element_by_id("lastName").send_keys("Test")
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Su'])[1]/following::td[17]").click()
        # driver.find_element_by_id("datepicker").click()
        # driver.find_element_by_id("datepicker").clear()
        # driver.find_element_by_id("datepicker").send_keys("-10-10")
        # driver.find_element_by_id("datepicker").send_keys(Keys.UP)
        # driver.find_element_by_id("datepicker").send_keys(Keys.DOWN)
        # driver.find_element_by_id("datepicker").click()
        # driver.find_element_by_id("datepicker").clear()
        # driver.find_element_by_id("datepicker").send_keys("1990-10-28")
        # driver.find_element_by_id("TFN").click()
        # driver.find_element_by_id("TFN").clear()
        # driver.find_element_by_id("TFN").send_keys("12345678")
        # driver.find_element_by_id("phoneNumber").clear()
        # driver.find_element_by_id("phoneNumber").send_keys("12345678")
        # driver.find_element_by_id("email").click()
        # driver.find_element_by_id("email").clear()
        # driver.find_element_by_id("email").send_keys("test@test.com")
        # driver.find_element_by_id("streetAddress").clear()
        # driver.find_element_by_id("streetAddress").send_keys("128 Test")
        # driver.find_element_by_id("city").clear()
        # driver.find_element_by_id("city").send_keys("Brisbane")
        # driver.find_element_by_id("postalCode").clear()
        # driver.find_element_by_id("postalCode").send_keys("4000")
        # Select(driver.find_element_by_name("state")).select_by_visible_text("Queensland")
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Store'])[1]/following::span[3]").click()
        # driver.find_element_by_id("select2-userType-container").click()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Register'])[1]/following::input[1]").click()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Register'])[1]/following::input[1]").clear()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Register'])[1]/following::input[1]").send_keys("Sta")
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Register'])[1]/following::input[1]").send_keys(Keys.ENTER)
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Staff'])[2]/following::button[1]").click()
