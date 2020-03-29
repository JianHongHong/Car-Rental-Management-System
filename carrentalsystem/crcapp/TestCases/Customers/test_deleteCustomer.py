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

class CustomerDel(BaseTest):
    def test_delete_customer(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        # driver.get("http://127.0.0.1:8000/management/home")
        # driver.find_element_by_link_text("View Customers").click()
        # driver.find_element_by_link_text("6").click()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Search:'])[1]/input[1]").click()
        # driver.find_element_by_link_text("C0011560").click()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Save'])[1]/following::button[1]").click()
        # driver.find_element_by_link_text("Yes").click()
        # driver.get("http://127.0.0.1:8000/management/customer/C0011560")
        # self.assertEqual("Page not found (404)", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Request Method:'])[1]/preceding::h1[1]").text)
        # ERROR: Caught exception [unknown command []]