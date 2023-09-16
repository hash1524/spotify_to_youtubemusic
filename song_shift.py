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
list_titles = list(df["Track Name"])

for i in range(95, len(df)):
    song_title = str(df["Track Name"][i]) + " " + str(df["Artist Name(s)"][i])
    try:
        time.sleep(1)
        cross_button = driver.find_element(
            By.XPATH,
            "/html/body/ytmusic-app/ytmusic-popup-container/tp-yt-paper-dialog[1]/ytmusic-add-to-playlist-renderer/div[1]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]",
        )
        driver.implicitly_wait(10)
        ActionChains(driver).move_to_element(cross_button).click(cross_button).perform()
        time.sleep(1)
        search_input = driver.find_element(
            By.XPATH,
            "/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/input",
        )
        driver.implicitly_wait(10)
        search_input.clear()
        search_input.send_keys(song_title, Keys.ENTER)
    except:
        print(i)
        search_input = driver.find_element(
            By.XPATH,
            "/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/input",
        )
        driver.implicitly_wait(10)
        search_input.clear()
        search_input.send_keys(song_title, Keys.ENTER)

    time.sleep(2)

    try:
        card = driver.find_element(
            By.XPATH,
            "/html/body/ytmusic-app/ytmusic-app-layout/div[5]/ytmusic-search-page/ytmusic-tabbed-search-results-renderer/div[2]/ytmusic-section-list-renderer/div[2]/ytmusic-card-shelf-renderer",
        )
        card_2_button = driver.find_element(
            By.XPATH,
            "/html/body/ytmusic-app/ytmusic-app-layout/div[5]/ytmusic-search-page/ytmusic-tabbed-search-results-renderer/div[2]/ytmusic-section-list-renderer/div[2]/ytmusic-card-shelf-renderer/div/div[2]/div[1]/div/div[2]/div[2]/yt-button-renderer[2]/yt-button-shape/button/div[2]",
        )
        driver.implicitly_wait(10)
        if card_2_button.text == "Save":
            ActionChains(driver).move_to_element(card_2_button).click(
                card_2_button
            ).perform()
            # try:
            #     cross_button = driver.find_element(
            #         By.XPATH,
            #         "/html/body/ytmusic-app/ytmusic-popup-container/tp-yt-paper-dialog[1]/ytmusic-add-to-playlist-renderer/div[1]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]",
            #     )
            # except:
            #     print(i + 1)
            continue
        else:
            try:
                next_list = driver.find_element(
                    By.XPATH,
                    "/html/body/ytmusic-app/ytmusic-app-layout/div[5]/ytmusic-search-page/ytmusic-tabbed-search-results-renderer/div[2]/ytmusic-section-list-renderer/div[2]/ytmusic-shelf-renderer[1]",
                )
                next_list_heading = driver.find_element(
                    By.XPATH,
                    "/html/body/ytmusic-app/ytmusic-app-layout/div[5]/ytmusic-search-page/ytmusic-tabbed-search-results-renderer/div[2]/ytmusic-section-list-renderer/div[2]/ytmusic-shelf-renderer[1]/div[1]",
                )
                driver.implicitly_wait(10)
                if next_list_heading.text == "Songs":
                    menu_button = driver.find_element(
                        By.XPATH,
                        "/html/body/ytmusic-app/ytmusic-app-layout/div[5]/ytmusic-search-page/ytmusic-tabbed-search-results-renderer/div[2]/ytmusic-section-list-renderer/div[2]/ytmusic-shelf-renderer[1]/div[3]/ytmusic-responsive-list-item-renderer[1]/ytmusic-menu-renderer",
                    )
                    driver.implicitly_wait(10)
                    ActionChains(driver).move_to_element(menu_button).click(
                        menu_button
                    ).perform()
                    save_button = driver.find_element(
                        By.XPATH,
                        "/html/body/ytmusic-app/ytmusic-popup-container/tp-yt-iron-dropdown/div/ytmusic-menu-popup-renderer/tp-yt-paper-listbox/ytmusic-menu-navigation-item-renderer[2]/a/yt-formatted-string",
                    )
                    driver.implicitly_wait(10)
                    if save_button.text == "Save to playlist":
                        ActionChains(driver).move_to_element(save_button).click(
                            save_button
                        ).perform()
                        # try:
                        #     cross_button = driver.find_element(
                        #         By.XPATH,
                        #         "/html/body/ytmusic-app/ytmusic-popup-container/tp-yt-paper-dialog[1]/ytmusic-add-to-playlist-renderer/div[1]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]",
                        #     )
                        # except:
                        #     print(i + 1)
                        continue
                    else:
                        continue
                else:
                    continue
            except:
                continue
    except:
        try:
            next_list = driver.find_element(
                By.XPATH,
                "/html/body/ytmusic-app/ytmusic-app-layout/div[5]/ytmusic-search-page/ytmusic-tabbed-search-results-renderer/div[2]/ytmusic-section-list-renderer/div[2]/ytmusic-shelf-renderer[1]",
            )
            next_list_heading = driver.find_element(
                By.XPATH,
                "/html/body/ytmusic-app/ytmusic-app-layout/div[5]/ytmusic-search-page/ytmusic-tabbed-search-results-renderer/div[2]/ytmusic-section-list-renderer/div[2]/ytmusic-shelf-renderer[1]/div[1]",
            )
            if next_list_heading.text == "Songs":
                menu_button = driver.find_element(
                    By.XPATH,
                    "/html/body/ytmusic-app/ytmusic-app-layout/div[5]/ytmusic-search-page/ytmusic-tabbed-search-results-renderer/div[2]/ytmusic-section-list-renderer/div[2]/ytmusic-shelf-renderer[1]/div[3]/ytmusic-responsive-list-item-renderer[1]/ytmusic-menu-renderer",
                )
                driver.implicitly_wait(10)
                ActionChains(driver).move_to_element(menu_button).click(
                    menu_button
                ).perform()
                save_button = driver.find_element(
                    By.XPATH,
                    "/html/body/ytmusic-app/ytmusic-popup-container/tp-yt-iron-dropdown/div/ytmusic-menu-popup-renderer/tp-yt-paper-listbox/ytmusic-menu-navigation-item-renderer[2]/a/yt-formatted-string",
                )
                driver.implicitly_wait(10)
                ActionChains(driver).move_to_element(save_button).click(
                    save_button
                ).perform()
                try:
                    cross_button = driver.find_element(
                        By.XPATH,
                        "/html/body/ytmusic-app/ytmusic-popup-container/tp-yt-paper-dialog[1]/ytmusic-add-to-playlist-renderer/div[1]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]",
                    )
                except:
                    print(i + 1)
                continue
            else:
                continue
        except:
            continue
