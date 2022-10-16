import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import obj
import re


class Main_Module:
        def run():
            groceryList = []
            url = 'https://etilbudsavis.dk/tilbud'
            path = '/Users/martin mortensen/Desktop/Div/Python/Projects/ScaperEtilbud/chromedriver'
            driver = webdriver.Chrome(path)
            driver.get(url)
            for i in range(10):
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                time.sleep(1)
            all_offers = driver.find_elements(By.TAG_NAME, 'li')
            idx = 1
            
            for offers in all_offers:
                try:
                    name = offers.find_element(By.XPATH,f'//*[@id="main"]/div[2]/ul/li[{idx}]/a/div/div[3]/header').text
                    price = offers.find_element(By.XPATH, f'//*[@id="main"]/div[2]/ul/li[{idx}]/a/div/div[3]/div[2]/div/span').text
                    store = offers.find_element(By.XPATH, f'//*[@id="main"]/div[2]/ul/li[{idx}]/a/div/div[3]/div[3]/div/div').text
                    a = obj.grocery()
                    a.Name = name
                    a.Store = store
                    price = re.sub(" kr.", "", price)
                    a.Price = price
                    idx = idx + 1
                except:
                    selenium.common.exceptions.NoSuchElementException 
                    continue
                print(a.Name)
                groceryList.append(a)
            driver.quit()
            return groceryList