import pymssql
import pandas as pd
from datetime import datetime
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
def connectToDb():
    server = '185.136.157.12'
    user = 'mqttuser'
    paswd = '@5TdXk-XzN?PRd$M'
    database = 'mqtt'
    conn = pymssql.connect(server, user, paswd, database)
    return [conn.cursor(),conn]
def getTopRows(cursor,columnName):
    cursor.execute("select top (1000) "+columnName+" from sampleTable1")
    myRows = cursor.fetchall()
    return myRows
# cursor , conn = connectToDb()
# # cursor.execute("SELECT * FROM	INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = 'sampleTable1'")
# # rows = cursor.fetchall()
# # col_list = [i[3] for i in rows]
# # index = col_list.index("UpdatedDate")
# # dateTimeList = [i[index] for i in getTopRows(cursor)]
# # print(dateTimeList)
# # print([i.month for i in dateTimeList] )
# lod = getTopRows(cursor,"Price")
# print()
# df = pd.DataFrame(lod)
# df.columns = ['Price']
# print(df)
driver= start_driver_1(False)
productData = parseHTMLtoBS(driver,"https://demoqa.com/books")
productList = productData.find_all("div",{"class":"rt-tbody"})[0]
print(len(productList.find_all("div",{"class":"action-buttons"})))
# for i in productList:
#     try:
#         # print(i.find("div",{"class":"action-buttons"}))
#         print(i)
#     except:
#         pass
#Getting 