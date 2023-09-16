from selenium import webdriver
from bs4 import BeautifulSoup
import re
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
import os
import shutil

# capture the browser in the port we opened it locally
chrome_options = Options()
# chrome_options.headless = True
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)

df = pd.read_csv("C:/Users/HARSHA/Desktop/liked.csv")
for i in range(0, len(df)):
    print(str(df["Track Name"][i]) + " : " + str(df["Artist Name(s)"][i]))
