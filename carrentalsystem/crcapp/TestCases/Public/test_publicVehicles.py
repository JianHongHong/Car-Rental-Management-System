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

class PublicVehicles(BaseTest):

    # Test for vehicle in public webpage
    def test_publicVehicles(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_link_text("Vehicles").click()
        self.assertEqual("Vehicles", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Vehicles'])[2]/following::h4[1]").text)
        self.assertEqual("Make: Mazda", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Year:'])[2]/following::h5[1]").text)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Year:'])[3]/following::p[1]").click()
        self.assertEqual("Vehicle Details", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Mazda 929'])[1]/following::h5[1]").text)