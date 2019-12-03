
import keys
import scrapFBS
import random
import fileRdWr
import os
import re
import time
import requests
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

s=keys.randomizer('interests')
local=keys.randomizer('location')
interest= (s[1])+"%20"+local
print(interest)
#
option = Options()
d = DesiredCapabilities.CHROME
d['loggingPrefs'] = { 'browser':'ALL' }
d["pageLoadStrategy"] = "none"  #  complete
option = Options()
#option.add_argument("--headless")
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_argument("--disable-images")
option.add_argument("--no-sandbox")
option.add_experimental_option("prefs", {
   "profile.default_content_setting_values.notifications": 2,
   "profile.managed_default_content_settings.images":2
})

path = "/home/shreyanshu/Documents/seleniumtesting/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(chrome_options=option, executable_path=path)
link ='https://www.facebook.com/search/pages/?q='+interest
def first():   
    driver.get(link)
    time.sleep(5)
    email = driver.find_element_by_id("email")
    email.send_keys("testcase.for.sel@gmail.com")
    time.sleep(5)
    paswrd = driver.find_element_by_id("pass")
    paswrd.send_keys("@world-by-me@")
    time.sleep(5)
    login_button = driver.find_element_by_id("loginbutton")
    login_button.click()
    time.sleep(2)
    driver.execute_script("window.history.go(-1)")
    time.sleep(10)
    pagelink()
    #------------------crawling-------------------------
def pagelink():    
        for i in range(10):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(3)
        initial_results = driver.find_elements_by_xpath("//div[@id='BrowseResultsContainer']")
        #---------------------scraping_facebooklink-------------------
        data_list = []
        for i in range(len(initial_results)):
            for card in initial_results[i].find_elements_by_xpath("./div[@class='_3u1 _gli _6pe1 _87m1']"):
                card_link = card.find_element_by_xpath("./div/div[@class='clearfix _ikh']")
                data_list.append(card_link.find_element_by_xpath("./div[@class='_4bl7 _3-90']/a").get_attribute("href"))
                # y = card_link.find_element_by_css_selector("div._pac")
        scrolled_list = []
        for i in range(10):
            xpath_ = "fbBrowseScrollingPagerContainer" + str(i)
            xpath_ = "//div[@id='{0}']".format(xpath_)
            if driver.find_elements_by_xpath(xpath_):
                scrolled_list.append(driver.find_elements_by_xpath(xpath_))
        for k in range(len(scrolled_list)):
            for card in scrolled_list[k][0].find_elements_by_xpath("./div[@class='_1yt']/div[@class='_3u1 _gli _6pe1 _87m1']"):
                card_link = card.find_element_by_xpath("./div/div[@class='clearfix _ikh']")
                data_list.append(card_link.find_element_by_xpath("./div[@class='_4bl7 _3-90']/a").get_attribute("href"))
        #--------------------------------list of links ---------------------#       
        print(len(data_list),"count")
        pagerender(data_list)
        return len(data_list)

def pagerender(data_list):        
        for j in range(len(data_list)):
            print(data_list[j])
            a_link= str(data_list[j])
            driver.get(a_link)
            time.sleep(5)
            scrollPage()
            scrapFBS.scrap_operation(a_link)#calling scrapper
            
            clickONpost()
            time.sleep(10)
            clickONabout()
            fileRdWr.fileReadWr()
            time.sleep(3)
            #os.remove("oyt.txt")

        time.sleep(2)
        driver.quit()    

def clickONpost():           
        try:
            post_clk= driver.find_element_by_css_selector("div._2yaa[data-key='tab_posts'] ")
            post_clk.click()
            postlk=str(driver.current_url)
            print(postlk)
            scrollPage()
            scrapFBS.scrap_operation(postlk)  
        except:
            pass            
        #time.sleep(5) 
def clickONabout():           
        try:
            post_clk= driver.find_element_by_css_selector("div._2yaa[data-key='tab_about'] ")
            post_clk.click()
            postlk=str(driver.current_url)
            print(postlk)
            time.sleep(3)
            scrapFBS.scrap_operation(postlk)  
        except:
            pass         
def scrollPage():    
        try:
            for i in range(10):
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                time.sleep(3)
                # print(i,"scroll",end="")
        except:              
            driver.execute_script("window.history.go(-1)") #go back
            pass


if __name__ == "__main__":
    first()
