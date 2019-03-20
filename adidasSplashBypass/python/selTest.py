import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():

    # Set up chromedriver
    # chromedriver = "/Users/rahulbrahmal/Documents/Bot/adcBot/chromedriver"
    chromedriver = '/usr/local/bin/chromedriver'
    os.environ["webdriver.chrome.driver"] = chromedriver
    url = "http://whatismyipaddress.com"
    i = 0
    proxyList = open("proxies.txt", "r")
    for proxy in proxyList:
        driverName = "driver" + str(i)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % proxy)
        # chrome_options.add_argument('--headless') # for running headless section.

        driverName = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
        driverName.get(url)

if __name__ == "__main__":
    main()
