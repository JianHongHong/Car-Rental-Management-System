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

class VehiclesInsert(BaseTest):

    # Test for editing of vehicle in staff page
    def test_VehiclesInsert(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_link_text("Login").click()
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("dev")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("dev")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password'])[1]/following::button[1]").click()
        driver.find_element_by_link_text("Insert Vehicle").click()
        driver.find_element_by_id("makeName").click()
        driver.find_element_by_id("makeName").clear()
        driver.find_element_by_id("makeName").send_keys("111")
        driver.find_element_by_id("model").click()
        driver.find_element_by_id("model").clear()
        driver.find_element_by_id("model").send_keys("111")
        driver.find_element_by_id("series").click()
        driver.find_element_by_id("series").clear()
        driver.find_element_by_id("series").send_keys("111")
        driver.find_element_by_id("year").click()
        driver.find_element_by_id("year").clear()
        driver.find_element_by_id("year").send_keys("2018")
        driver.find_element_by_id("enginesize").click()
        driver.find_element_by_id("enginesize").clear()
        driver.find_element_by_id("enginesize").send_keys("111")
        driver.find_element_by_id("seatingCapacity").click()
        driver.find_element_by_id("seatingCapacity").clear()
        driver.find_element_by_id("seatingCapacity").send_keys("111")
        driver.find_element_by_id("fuelSystem").click()
        driver.find_element_by_id("fuelSystem").clear()
        driver.find_element_by_id("fuelSystem").send_keys("111")
        driver.find_element_by_id("tankcapacity").click()
        driver.find_element_by_id("tankcapacity").clear()
        driver.find_element_by_id("tankcapacity").send_keys("111")
        driver.find_element_by_id("power").click()
        driver.find_element_by_id("power").clear()
        driver.find_element_by_id("power").send_keys("111")
        driver.find_element_by_id("standardTransmission").click()
        driver.find_element_by_id("standardTransmission").clear()
        driver.find_element_by_id("standardTransmission").send_keys("111")
        driver.find_element_by_id("wheelBase").click()
        driver.find_element_by_id("wheelBase").clear()
        driver.find_element_by_id("wheelBase").send_keys("111")
        driver.find_element_by_id("bodyType").click()
        driver.find_element_by_id("bodyType").clear()
        driver.find_element_by_id("bodyType").send_keys("111")
        driver.find_element_by_id("driveType").click()
        Select(driver.find_element_by_id("driveType")).select_by_visible_text("AWD")
        driver.find_element_by_id("newPrice").click()
        driver.find_element_by_id("newPrice").clear()
        driver.find_element_by_id("newPrice").send_keys("111")
        driver.find_element_by_id("select2-storeID-container").click()
        # DropDown not working
        # driver.find_element_by_id("select2-storeID-result-ud7i-S0001").click() 
        # driver.find_element_by_id("submit").click()
        # WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//*[@id='content']/div/div/div/div/p"), "Vehicle inserted."))
        # driver.find_element_by_xpath("//*[@id='mainContent']/div[1]/div/nav/ol/li[1]/a").click()
        # driver.find_element_by_link_text("View Vehicles").click()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Search:'])[1]/input[1]").click()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Search:'])[1]/input[1]").clear()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Search:'])[1]/input[1]").send_keys("111")
        # self.assertEqual("111", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='V15402'])[1]/following::td[1]").text)