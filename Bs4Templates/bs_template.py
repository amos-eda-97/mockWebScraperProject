#Selenium templates
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import shutil
import time
import os
import json
import re
import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup
def start_driver_1(headless=True):
    if not headless:
        return webdriver.Firefox()
    firefox_options = webdriver.firefox.options.Options()
    firefox_options.add_argument('--headless')
    firefox_options.add_argument('--no-sandbox')
    return webdriver.Firefox(options=firefox_options)
def start_driver(headless=True):
    if not headless:
        return webdriver.Chrome()
    firefox_options = webdriver.chrome.options.Options()
    firefox_options.add_argument('--headless')
    firefox_options.add_argument('--no-sandbox')
    return webdriver.Chrome(options=firefox_options)
	
def waitForElementToPopUpbyClassName(driver, class_name,timeout=10):
    try:
        element_present = EC.presence_of_element_located((By.CLASS_NAME,class_name ))
        WebDriverWait(driver, timeout).until(element_present)
        return driver.find_element(By.CLASS_NAME,class_name)
    except TimeoutException:
        print("Timed out waiting for page to load")
        return None
def waitForElementToPopUpbyID(driver, ID,timeout=10):
    try:
        element_present = EC.presence_of_element_located((By.ID,ID ))
        WebDriverWait(driver, timeout).until(element_present)
        return driver.find_element(By.ID,ID)
    except TimeoutException:
        print("Timed out waiting for page to load")
        return None
def parseHTMLtoBS(driver, html_link):
    driver.get(html_link)
    print("Starting Download from: {}".format(html_link))
    html = driver.execute_script("return document.documentElement.outerHTML")
    product = bs(html, 'html.parser')
    return product
driver= start_driver_1(False)
# productData = parseHTMLtoBS(driver, "https://demoqa.com/books")
# listOfProd = productData.find("div",{"class":"rt-tbody"})
# for i in listOfProd:
#     try:
#         print(i.find("div",{"class":"action-buttons"}).text)
#     except Exception as e:
#         pass
        # print("Error encountered ",e)
# print(productData.find("div",{"class":"rt-tbody"}))