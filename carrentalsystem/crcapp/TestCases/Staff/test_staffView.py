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

class StaffView(BaseTest):

    # Test for view of staff in staff page
    def test_staffView(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        # driver.get("http://localhost:8000/management/home")
        # driver.find_element_by_link_text("View Staff").click()
        # driver.find_element_by_link_text("E00002").click()
        # driver.find_element_by_name("modify").click()
        # self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^xpath=\(\.//[\s\S]*\[normalize-space\(text\(\)\) and normalize-space\(\.\)='Jax Lee'\]\)\[1\]/following::p\[1\]$")