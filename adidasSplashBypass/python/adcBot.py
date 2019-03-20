import os
import sys
import time
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
    chromedriver = "/Users/rahulbrahmal/Desktop/adcBot/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver

    url = "http://whatismyipaddress.com" #Put the link of the spash page here
    i = 0
    proxyList = open("proxies.txt", "r")
    for proxy in proxyList:
        driverName = "driver" + str(i)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % proxy)
        # chrome_options.add_argument('--headless') # for running headless section.

        driverName = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
        driverName.get(url)
        driverName.set_window_position(-10000, 0)

        i += 1

    time.sleep(100000)

if __name__ == "__main__":
    main()
