import os
import sys
import time
import Tkinter
import tkMessageBox
from Tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


## Purpose of bot is to open multiple instances of chrome page on
## different proxies, and to delete the cookies and capcha indormation
## when clicked on. Should allow for page to be refreshed from new
## location, and thus cop more

##SECOND OPTION
##HMAC Decryption ...

def main():

    #Chromedriver stuff
    chromedriver = "/Users/rahulbrahmal/Documents/Bot/adidasSpashBypass/python/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver

    url = "https://store.nike.com/my/en_gb/pd/sb-dunk-low-pro-black-pigeon-skateboarding-shoe/pid-12056130/pgid-12286163" #Put the link of the spash page here
    i = 1;
    j = 3
    proxyList = open("proxies.txt", "r")
    sizeArr = []
    while (i < 5):
        driverName = "driver" + str(i)
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--proxy-server=%s' % proxy)
        # chrome_options.add_argument('--headless') # for running headless section.
        j += 0.5
        # driverName = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
        driverName = webdriver.Chrome(chromedriver)
        driverName.get(url)

        driverName.find_element_by_xpath('//*[@id="exp-pdp-buying-tools-container"]/form/div[1]/div/a').click();
        strXpath = '//*[@id="exp-pdp-buying-tools-container"]/form/div[1]/div/div/ul/li[' + str(j) + ']';
        driverName.find_element_by_xpath(strXpath).click();
        driverName.find_element_by_xpath('//*[@id="buyingtools-add-to-cart-button"]').click();
        driverName.find_element_by_xpath('/html/body/div[7]/div/div[2]/div[1]/div[2]/div[3]/a[2]');

        i += 1

    # while (i >= 0):
    #     driverName = "driver" +


if __name__ == "__main__":
    main()
