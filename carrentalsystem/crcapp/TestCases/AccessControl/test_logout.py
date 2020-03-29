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

class Logout(BaseTest):
    # Test for logout successfull
    def test_Logout(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_link_text("Login").click()
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").send_keys("dev")
        driver.find_element_by_id("password").send_keys("dev")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password'])[1]/following::button[1]").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Logout")))
        driver.find_element_by_link_text("Logout").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
        self.assertEqual("Successfully logged off.", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Login'])[2]/following::div[4]").text)
    