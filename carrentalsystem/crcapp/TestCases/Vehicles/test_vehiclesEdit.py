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

class VehiclesEdit(BaseTest):

    # Test for editing of vehicle in staff page
    def test_VehiclesEdit(self):
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
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Search:'])[1]/input[1]").send_keys("V14811")
        driver.find_element_by_link_text("V14811").click()
        driver.find_element_by_id("makeName").click()
        driver.find_element_by_id("makeName").clear()
        driver.find_element_by_id("makeName").send_keys("TEST")
        driver.find_element_by_id("model").clear()
        driver.find_element_by_id("model").send_keys("TEST")
        driver.find_element_by_id("series").clear()
        driver.find_element_by_id("series").send_keys("TEST")
        driver.find_element_by_id("year").clear()
        driver.find_element_by_id("year").send_keys("2008")
        driver.find_element_by_id("enginesize").clear()
        driver.find_element_by_id("enginesize").send_keys("2")
        driver.find_element_by_id("seatingCapacity").clear()
        driver.find_element_by_id("seatingCapacity").send_keys("5")
        driver.find_element_by_id("fuelSystem").clear()
        driver.find_element_by_id("fuelSystem").send_keys("TEST")
        driver.find_element_by_id("tankcapacity").clear()
        driver.find_element_by_id("tankcapacity").send_keys("0")
        driver.find_element_by_id("power").clear()
        driver.find_element_by_id("power").send_keys("0")
        driver.find_element_by_id("standardTransmission").clear()
        driver.find_element_by_id("standardTransmission").send_keys("0")
        driver.find_element_by_id("wheelBase").clear()
        driver.find_element_by_id("wheelBase").send_keys("0")
        driver.find_element_by_id("bodyType").clear()
        driver.find_element_by_id("bodyType").send_keys("TEST")
        driver.find_element_by_id("driveType").click()
        Select(driver.find_element_by_id("driveType")).select_by_visible_text("AWD")
        driver.find_element_by_id("newPrice").click()
        driver.find_element_by_id("newPrice").clear()
        driver.find_element_by_id("newPrice").send_keys("0")
        driver.find_element_by_id("select2-storeID-container").click()
        # Drop-down box not working
        # driver.find_element_by_xpath("//*[@id='vform']/div/div[2]/div[2]/input").click()
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div/div/div/div/p")))
        # driver.find_element_by_link_text("Vehicle").click()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Search:'])[1]/input[1]").click()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Search:'])[1]/input[1]").clear()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Search:'])[1]/input[1]").send_keys("V14811")
        # self.assertEqual("V14811", driver.find_element_by_link_text("V14811").text)