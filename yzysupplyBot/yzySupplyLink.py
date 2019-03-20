import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def main():
    chromedriver = "chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)

    url = "https://yeezysupply.com/products/mens-suede-military-boot-military-light/?back=%2Fcollections%2Ffootwear"

    driver.get(url)

    driver.find_element_by_xpath('//*[@id="P-12175275923"]/div[2]/form/div[2]/div/select')
    //*[@id="P-12175275923"]/div[2]/form/div[2]
    //*[@id="P-12582691539"]/div[2]/form/div[2]

if __name__ == "__main__":
    main()
