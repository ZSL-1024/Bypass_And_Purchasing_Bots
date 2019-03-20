import os
import sys
import time
from firebase import firebase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():

    # Chromedriver set up
    chromedriver = 'chromedriver'
    os.environ["webdriver.chrome.driver"] = chromedriver
    chrome_options = webdriver.ChromeOptions()



    # firebase = firebase.FirebaseApplication('https://pricecomparer-4b38f.firebaseio.com/', None);
    # result = firebase.get('/users', None);

    url = 'https://www.goat.com/#!/s/%20'
    # Creates webdriver instance
    driver = webdriver.Chrome(chromedriver)
    driver.get(url)

    totalResults = driver.find_element_by_xpath('//*[@id="App-react-component-f64ab93f-9bba-48fa-8d1d-081ecf99e1a1"]/div/div[2]/h3').text
    totalResults = totalResults.split()
    totalResults = int(totalResults[0])

    i = 1;
    while (i <= totalResults):
        driver.implicitly_wait(10)
        # Gets the product page
        xpathMain = '//*[@id="App-react-component-36b040c2-285a-4c59-b7ec-bcaab49ce369"]/div/div[2]/div/div[' + str(i) + ']/a/div[2]/h3'
        name = driver.find_element_by_xpath(xpathMain).text
        print name
        driver.find_element_by_xpath(xpathMain).click()
        j = 0;
        while (true):
            try:
                driver.find_element_by_xpath('//*[@id="App-react-component-36b040c2-285a-4c59-b7ec-bcaab49ce369"]/div/div[2]/div[1]/div[2]/div[3]/div[4]/div[1]/span[%i]', j)
                priceVal = driver.find_element_by_xpath('//*[@id="App-react-component-36b040c2-285a-4c59-b7ec-bcaab49ce369"]/div/div[2]/div[1]/div[2]/div[3]/div[4]/div[2]/div/div[2]/div[1]')
                print priceVal
            except:
                break

            j = j + 1

        i = i + 1

    driver.close()

if __name__ == "__main__":
    main()
