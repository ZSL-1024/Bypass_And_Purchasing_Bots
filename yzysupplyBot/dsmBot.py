import os
import sys
import xlrd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

def main():
    chromedriver = "/Users/rahulbrahmal/Documents/Bot/yzysupplyBot/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.implicitly_wait(5)

    url = "http://yeezysupply.com"

    driver.get(url)

    # itemPos = []
    # itemPos = driver.find_elements_by_class_name("PGI__img_wrap js-grid-item-inner");
    # for item in itemPos:
    #     item.click

    el = driver.find_elements_by_xpath("//*[@id=js-main]/div/a[1]")
    #
    for element in el:
        action = webdriver.common.action_chains.ActionChains(driver);
        action.move_to_element_with_offset(element, 80, 195)
        action.click()

    print ("OUT")


    time.sleep(20)


if __name__ == "__main__":
    main()
