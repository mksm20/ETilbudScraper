from ctypes import sizeof
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import obj
import re


class Main_Module:
        groceryList = []
        url = 'https://etilbudsavis.dk/tilbud'
        path = '/Users/martin mortensen/Desktop/Div/Python/Projects/ScaperEtilbud/chromedriver'
        driver = webdriver.Chrome(path)
        driver.get(url)
        for i in range(30):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(1)
        all_offers = driver.find_elements(By.TAG_NAME, 'li')
        idx = 1  
        for offers in all_offers:
            try:                                   
                name = offers.find_element(
                    By.XPATH,
                    f"""//*[@id="main"]/div[2]/ul
                    /li[{idx}]/a/div/div[3]/header""").text
                price = offers.find_element(
                    By.XPATH, 
                    f"""//*[@id="main"]/div[2]/ul
                    /li[{idx}]/a/div/div[3]/div[2]/div/span""").text
                store = offers.find_element(
                    By.XPATH, 
                    f"""//*[@id="main"]/div[2]/ul
                    /li[{idx}]/a/div/div[3]/div[3]/div/div""").text
                extra = offers.find_element(
                    By.XPATH, 
                    f"""/html/body/div[1]/div/div[2]/div[2]/div[2]/ul
                    /li[{idx}]/a/div/div[3]/div[1]""").text
                a = obj.grocery()
                a.Name = name
                a.Store = store
                price = re.sub(" kr.", "", price)
                a.Price = price
                a.Extra = extra
                idx = idx + 1
                print(price, name)
                groceryList.append(a)
            except:
                selenium.common.exceptions.NoSuchElementException 
                continue
        driver.quit()
 