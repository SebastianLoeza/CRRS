
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

    # create webdriver object
driver = webdriver.Safari()

    # get geeksforgeeks.org
driver.get("https://royaleapi.com/card/fisherman")
radio_bt = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='page_content']/div[3]/div[2]/a[2]")))
radio_bt.click()
try:

    radio_tache = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='dismiss-button']")))
    radio_tache.click()
except NoSuchElementException:
    try:
        radio_close = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='dismiss-button']")))
        radio_close.click() 
    
    except NoSuchElementException:
        print("No hay bro xd")

driver.quit()

