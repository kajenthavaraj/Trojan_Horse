from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
import selenium
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from cv2 import cv2
import numpy as np
from PIL import ImageGrab
import time
import os
from pynput.keyboard import Key, Controller
import pyautogui

#from Screen_Automation.startloom import *    - old start loom
from Screen_Automation.startOBS import *

#from editor import edit_video

######link to google sheet######
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet1 = client.open("Trojan Horse Automation").sheet1

######set up driver######
PATH = "C:\Program Files (x86)\chromedriver.exe"
chrome_options = webdriver.ChromeOptions() #remove automation software warning from browser
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(PATH,options=chrome_options)

actionChains = ActionChains(driver)
touchActions = TouchActions(driver)

######function to highlight text in ads library######
def highlight():
    element = driver.find_element_by_class_name("_94cs")
    actionChains = ActionChains(driver)
    actionChains.move_to_element(element).perform()
    actionChains.double_click(element).perform()
    actionChains.click(element).perform()

######function to mimic scrolling in ads library######   - 5 seconds
def scroll():
    actionChains = ActionChains(driver)
    i = 0
    #total time = 5 secs
    while i < 10:
        actionChains.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
        time.sleep(0.5)        
        i = i + 1

######Get info from google sheet######
brand_name = sheet1.col_values(1)
brand_web_col = sheet1.col_values(2)
brand_ads_col = sheet1.col_values(3)
competion_ads_col = sheet1.col_values(4)
ads_status_col = sheet1.col_values(5)
instagram_col = sheet1.col_values(6)

tab4 = "https://www.ionic-x.com"


num_brands = len(brand_name) - 1

i = 1
while i <= num_brands:
    #get ads status from google sheet
    ads_status = ads_status_col[i]

    if ads_status == "yes" or ads_status == "Yes":
        ######save tabs to open from google sheet######
        tab1 = brand_web_col[i]
        tab2 = brand_ads_col[i]
        tab3 = competion_ads_col[i]

        driver = webdriver.Chrome(PATH,options=chrome_options)

        ######pre load all website tabs######
        driver.maximize_window()

        driver.get(tab1) #open tab 1

        driver.execute_script("window.open('about:blank', 'tab2');") #create new tab
        driver.switch_to.window("tab2") #switch to new tab
        driver.get(tab2) #open tab 2 in new tab

        driver.execute_script("window.open('about:blank', 'tab3');") #create new tab
        driver.switch_to.window("tab3") #switch to new tab
        driver.get(tab3) #open tab 3 in new tab
        
        driver.execute_script("window.open('about:blank', 'tab4');") #create new tab
        driver.switch_to.window("tab4") #switch to new tab
        driver.get(tab4) #open tab 4 in new tab
        element = driver.find_element_by_id("comp-knm7au6t") #html case study element
        driver.execute_script("arguments[0].scrollIntoView();", element) #scroll to case study

        driver.switch_to.window(driver.window_handles[0]) #go back to first tab

        #Start recording screen
        start_recording()

        ######Swtich through tabs in timing######

        time.sleep(48 - 2) #time for intro

        driver.switch_to.window(driver.window_handles[1])
        time.sleep(34)#time for mistake 1 - brands ads
        highlight() #highlight number of ads running
        time.sleep(21) #time for mistake 1 - brands ads total = 58 secs

        driver.switch_to.window(driver.window_handles[2])
        time.sleep(4) #time for mistake 1 - competitors ads
        highlight() #highlight number of ads running
        time.sleep(22) #time for mistake 1 - competitors ads

        driver.switch_to.window(driver.window_handles[1])
        time.sleep(8) #time for mistake 2 - brands ads
        scroll() #5 secs
        time.sleep(20) #time for mistake 2 - brands ads

        driver.switch_to.window(driver.window_handles[2])
        time.sleep(2)
        scroll() #5 secs
        time.sleep(65) #time for mistake 2 - competitors ads

        driver.switch_to.window(driver.window_handles[3])
        time.sleep(180 - 1) #time for case study

        ######End recording######
        stop_recording()

        driver.quit()

        #Update Status in video made sheet
        sheet1.update_cell(i+1, 7, "MADE")

    
    elif ads_status == "no" or ads_status == "No":
        ######save tabs to open from google sheet######
        tab1 = brand_web_col[i]
        tab2 = brand_ads_col[i]
        tab3 = competion_ads_col[i]
        insta_tab = instagram_col[i]

        driver = webdriver.Chrome(PATH,options=chrome_options)

        #login to instagram############################################
        driver.get('https://www.instagram.com/accounts/login/')

        time.sleep(2)

        keyboard = Controller()

        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        
        keyboard.press("m")
        keyboard.release("m")
        keyboard.press("d")
        keyboard.release("d")
        keyboard.press("h")
        keyboard.release("h")
        keyboard.press("s")
        keyboard.release("s")
        keyboard.press(".")
        keyboard.release(".")
        keyboard.press("c")
        keyboard.release("c")
        keyboard.press("o")
        keyboard.release("o")
        keyboard.press("m")
        keyboard.release("m")
        keyboard.press("p")
        keyboard.release("p")
        keyboard.press("s")
        keyboard.release("s")
        keyboard.press("c")
        keyboard.release("c")
        keyboard.press("i")
        keyboard.release("i")

        keyboard.press(Key.tab)
        keyboard.release(Key.tab)

        keyboard.press("m")
        keyboard.release("m")
        keyboard.press("d")
        keyboard.release("d")
        keyboard.press("h")
        keyboard.release("h")
        keyboard.press("s")
        keyboard.release("s")
        keyboard.press("2")
        keyboard.release("2")
        keyboard.press("0")
        keyboard.release("0")
        keyboard.press("2")
        keyboard.release("2")
        keyboard.press("0")
        keyboard.release("0")

        keyboard.press(Key.tab)
        keyboard.release(Key.tab)

        keyboard.press(Key.tab)
        keyboard.release(Key.tab)

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(10)
        ############################################

        ######pre load all website tabs######
        driver.maximize_window()

        driver.get(tab1) #open tab 1

        driver.execute_script("window.open('about:blank', 'tab2');") #create new tab
        driver.switch_to.window("tab2") #switch to new tab
        driver.get(tab2) #open tab 2 in new tab

        driver.execute_script("window.open('about:blank', 'tab3');") #create new tab
        driver.switch_to.window("tab3") #switch to new tab
        driver.get(tab3) #open tab 3 in new tab
        
        driver.execute_script("window.open('about:blank', 'insta_tab');") #create new tab
        driver.switch_to.window("insta_tab") #switch to new tab
        driver.get(insta_tab) #open instagram page in new tab

        driver.execute_script("window.open('about:blank', 'tab4');") #create new tab
        driver.switch_to.window("tab4") #switch to new tab
        driver.get(tab4) #open tab 4 in new tab
        element = driver.find_element_by_id("comp-knm7au6t") #html case study element
        driver.execute_script("arguments[0].scrollIntoView();", element) #scroll to case study

        driver.switch_to.window(driver.window_handles[0]) #go back to first tab

        #Start recording screen
        start_recording()

        ######Swtich through tabs in timing######

        time.sleep(40 - 2) #time for intro

        driver.switch_to.window(driver.window_handles[1])
        time.sleep(11)#time for mistake 1 - brands ads
        highlight() #highlight number of ads running
        time.sleep(18) #time for mistake 1 - brands ads total = 20 secs

        driver.switch_to.window(driver.window_handles[2])
        time.sleep(8) #time for mistake 1 - competitors ads
        highlight() #highlight number of ads running
        time.sleep(34) #time for mistake 1 - competitors ads

        driver.switch_to.window(driver.window_handles[3])
        time.sleep(29) #time for mistake 2 - insta

        driver.switch_to.window(driver.window_handles[4])
        time.sleep(158) #time for case study

        ######End recording######
        stop_recording()

        driver.quit()

        #Update Status in video made sheet
        sheet1.update_cell(i+1, 7, "MADE")

    i= i + 1
    print("Finished")





#Update Status in video made sheet 
#sheet1.update_cell(i+1, 7, "MADE")
# ######save tabs to open from google sheet######
# tab1 = brand_web_col[i]
# tab2 = brand_ads_col[i]
# tab3 = competion_ads_col[i]
