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

class PublicStore(BaseTest):

    # Test for store in public webpage
    def test_publicStore(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_link_text("Stores").click()
        driver.find_element_by_xpath("//*[@id='heading0']/div/div/h4/a").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Contact Number:'])[2]/following::h5[1]").click()
        self.assertEqual("Darlinghurst Store", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Contact Number:'])[2]/following::h5[1]").text)