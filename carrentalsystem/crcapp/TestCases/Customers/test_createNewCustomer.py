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

class CustomerAdd(BaseTest):
    def test_register_a_new_customer(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        # driver.get("http://127.0.0.1:8000/management/home")
        # driver.find_element_by_link_text("Register New Customer").click()
        # driver.find_element_by_id("firstName").click()
        # driver.find_element_by_id("firstName").clear()
        # driver.find_element_by_id("firstName").send_keys("Tom")
        # driver.find_element_by_id("lastName").click()
        # driver.find_element_by_id("lastName").clear()
        # driver.find_element_by_id("lastName").send_keys("Test")
        # driver.find_element_by_name("gender").click()
        # Select(driver.find_element_by_name("gender")).select_by_visible_text("Male")
        # driver.find_element_by_name("gender").click()
        # driver.find_element_by_id("streetAddress").click()
        # driver.find_element_by_id("streetAddress").clear()
        # driver.find_element_by_id("streetAddress").send_keys("Test this")
        # driver.find_element_by_id("city").clear()
        # driver.find_element_by_id("city").send_keys("City")
        # driver.find_element_by_id("postalCode").clear()
        # driver.find_element_by_id("postalCode").send_keys("4032")
        # driver.find_element_by_name("stateAddress").click()
        # Select(driver.find_element_by_name("stateAddress")).select_by_visible_text("Queensland")
        # driver.find_element_by_name("stateAddress").click()
        # driver.find_element_by_id("DriverLicenseNumber").click()
        # driver.find_element_by_id("DriverLicenseNumber").clear()
        # driver.find_element_by_id("DriverLicenseNumber").send_keys("9999999999")
        # driver.find_element_by_id("DOB").click()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Su'])[1]/following::td[33]").click()
        # driver.find_element_by_id("phoneNumber").click()
        # driver.find_element_by_id("phoneNumber").clear()
        # driver.find_element_by_id("phoneNumber").send_keys("0458553121")
        # driver.find_element_by_id("email").click()
        # driver.find_element_by_id("email").clear()
        # driver.find_element_by_id("email").send_keys("test@test.com")
        # driver.find_element_by_id("occupation").click()
        # driver.find_element_by_id("occupation").clear()
        # driver.find_element_by_id("occupation").send_keys("Developer")
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Occupation'])[1]/following::button[1]").click()
        # self.assertEqual("Customer created.", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Register New Customer'])[1]/following::p[1]").text)