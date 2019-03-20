import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    # Set up chromedriver
    chromedriver = "/usr/local/bin/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    url = "http://www.adidas.com/us/men-originals-shoes"
    i = 0

    proxy = '71.191.75.67:3128'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % proxy)
    # chrome_options.add_argument('--headless') # for running headless section.

    driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
    driver.get(url)

    driver.find_element_by_xpath('//*[@id="product-C77124"]/div[3]/a/span').click()
    print ("Entering wait")
    time.sleep(10)
    print ("Exiting wait")
    driver.get('https://www.adidas.com/us/wishlist-show')
    print ("Entering wait")
    # time.sleep(10)
    print ("Exiting wait")
    driver.find_element_by_xpath('//*[@id="product_C77124"]/div[5]/div/form/div[1]/div[2]/div/div/a').click()
    driver.find_element_by_xpath('//*[@id="product_C77124"]/div[5]/div/form/div[1]/div[2]/div/div/div/div[2]/div/ul/li[11]/span').click()
    driver.find_element_by_xpath('//*[@id="product_C77124"]/div[5]/div/form/div[7]/div/div/button').click()
    driver.find_element_by_xpath('//*[@id="minicart_overlay"]/div[2]/a[2]').click()

if __name__ == "__main__":
    main()
