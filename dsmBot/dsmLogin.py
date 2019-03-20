import os
import sys
import xlrd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def main():
    chromedriver = "/Users/rahulbrahmal/Documents/Bot/dsmBot/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.implicitly_wait(5)

    url = "https://shop.doverstreetmarket.com/us/customer/account/login/referer/aHR0cHM6Ly9zaG9wLmRvdmVyc3RyZWV0bWFya2V0LmNvbS91cy9jdXN0b21lci9hY2NvdW50L2luZGV4Lw,,/"

    i = 0
    while (i <= 5):
        driver.get(url);

        emailAddress = driver.find_element_by_name("login[username]")
        emailAddress.send_keys("rahulvbrahmal@gmail.com");

        password = driver.find_element_by_name("login[password]")
        password.send_keys("S@hana68")

        # captcha = driver.find_element_by_class("recaptcha-checkbox-checkmark")
        # captcha.click();
        #
        # password.send_keys(Keys.ENTER);
        #
        time.sleep(20)
        driver.get("https://shop.doverstreetmarket.com/us/customer/account/logout/")





if __name__ == "__main__":
    main()
