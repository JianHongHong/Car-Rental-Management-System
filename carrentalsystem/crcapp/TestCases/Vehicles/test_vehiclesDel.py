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

class VehiclesDel(BaseTest):

    # Test for deleting of vehicle in staff page
    def test_VehiclesDel(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_link_text("Login").click()
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("dev")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("dev")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password'])[1]/following::button[1]").click()
        driver.find_element_by_link_text("View Vehicles").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Search:'])[1]/input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Search:'])[1]/input[1]").clear()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Search:'])[1]/input[1]").send_keys("V14806")
        driver.find_element_by_link_text("V14806").click()
        self.accept_next_alert = True
        driver.find_element_by_id("deleteBtn").click()
        self.assertEqual("Are your sure, you want to delete the vehicle: V14806", self.close_alert_and_get_its_text())
        time.sleep(0.1)
        self.assertEqual("Vehicle Deleted", self.close_alert_and_get_its_text())
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Search:'])[1]/input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Search:'])[1]/input[1]").clear()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Search:'])[1]/input[1]").send_keys("V14806")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Search:'])[1]/input[1]").send_keys(Keys.ENTER)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Vehicle ID'])[3]/following::td[1]").click()
        self.assertEqual("No matching records found", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Vehicle ID'])[3]/following::td[1]").text)