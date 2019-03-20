import os
import sys
import time
from selenium import webdriver
from joblib import Parallel, delayed
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    chromedriver = "/Users/rahulbrahmal/Documents/Bot/nmdHU/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver


    url = "https://www.adidas.co.uk/koln-shoes/BY9804.html" #CHANGE THIS LINK

    proxyList = open('proxyList.txt', 'r');

    i = 1;
    for proxy in proxyList:
        driverName = 'driver' + str(i)

        fileName = 'billing' + str(i) + '.txt'
        billingShipping = open(fileName, 'r')
        arrInfo = [];
        idx = 0
        for info in billingShipping:
            arrInfo.insert(idx, info)
            idx += 1
            # arrInfo.append(info)

        Parallel(n_jobs=-1)(delayed(runPageSequence)(driverName, arrInfo))

        i += 1



def runPageSequence(driverName, arrInfo):
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--proxy-server=%s' % proxy)
    # chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920, 1080')

    driverName = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
    driverName.implicitly_wait(5)
    driverName.get(url);

    #clicks on size selector box
    driverName.find_element_by_xpath('//*[@id="size-selector"]/div/div[1]/div[2]').click()
    #clicks on dropdown
    time.sleep(2)

    size = float(arrInfo[11])
    size = size - 6
    size = int(size / 0.5) + 1

    strXpath = '//*[@id="size-selector"]/div/div[1]/div[1]/span/div/ul/li[' + str(size) + ']'
    driverName.find_element_by_xpath(strXpath).click() #Adjust the size with 3

    #clicks on size
    time.sleep(2)
    driverName.find_element_by_xpath('//*[@id="add-to-bag"]').click()
    #clicks on bag
    time.sleep(2)
    bagClick = driverName.find_element_by_xpath('//*[@id="add-to-bag-order-summary"]/a[2]')
    if (bagClick.is_displayed()):
        bagClick.click()
    else:
        driverName.find_element_by_xpath('//*[@id="added-to-bag-modal"]/div/div[2]/main/div/div[2]').click

    #Clicks on Bag
    # driverName.find_element_by_xpath('//*[@id="mobile-toolbar"]/div/a').click()

    driverName.get('https://www.adidas.co.uk/on/demandware.store/Sites-adidas-GB-Site/en_GB/Cart-Show')

    #Clicks on checkout
    driverName.find_element_by_xpath('//*[@id="dwfrm_cart_checkoutCart"]').click()

    #Autofill

    #First Name
    driverName.find_element_by_xpath('//*[@id="dwfrm_shipping_shiptoaddress_shippingAddress_firstName"]').send_keys(arrInfo[0])
    #Last Name
    driverName.implicitly_wait(2)
    driverName.find_element_by_xpath('//*[@id="dwfrm_shipping_shiptoaddress_shippingAddress_lastName"]').send_keys(arrInfo[1])
    #Address 1
    driverName.implicitly_wait(2)
    driverName.find_element_by_xpath('//*[@id="dwfrm_shipping_shiptoaddress_shippingAddress_address1"]').send_keys(arrInfo[2])
    #Address 2
    driverName.implicitly_wait(2)
    driverName.find_element_by_xpath('//*[@id="dwfrm_shipping_shiptoaddress_shippingAddress_address2"]').send_keys(arrInfo[3])
    #Town or City
    driverName.implicitly_wait(2)
    driverName.find_element_by_xpath('//*[@id="dwfrm_shipping_shiptoaddress_shippingAddress_city"]').send_keys(arrInfo[4])
    #Postcode
    driverName.implicitly_wait(2)
    driverName.find_element_by_xpath('//*[@id="dwfrm_shipping_shiptoaddress_shippingAddress_postalCode"]').send_keys(arrInfo[5])
    #Email
    driverName.implicitly_wait(2)
    driverName.find_element_by_xpath('//*[@id="dwfrm_shipping_email_emailAddress"]').send_keys(arrInfo[6])

    #Click ReviewAndPay Button
    driverName.implicitly_wait(2)
    # buttonReviewAndPay = driverName.find_element_by_xpath('//*[@id="shippingForm"]/div[2]/ng-form/div[6]/div/button')
    # if (buttonReviewAndPay.is_displayed()):
    #     buttonReviewAndPay.click()

    #Payment Info Filling in

    #Card Number
    driverName.find_element_by_xpath('//*[@id="dwfrm_adyenencrypted_number"]').send_keys(arrInfo[7])
    #ExpiryDateMonthButton
    driverName.find_element_by_xpath('//*[@id="adyen-encrypted-form"]/fieldset/div[3]/div[2]/div/div/div/a').click()
    #ExpiryDateMonthVal
    monthVal = int(arrInfo[8]) + 2
    monthXPath = '//*[@id="adyen-encrypted-form"]/fieldset/div[3]/div[2]/div/div/div/div/div[2]/div/ul/li[' + str(monthVal) + ']'
    driverName.find_element_by_xpath(monthXPath).click() #Replace 4 with the month. 2 is
    # //*[@id="adyen-encrypted-form"]/fieldset/div[3]/div[2]/div/div/div/div/div[2]/div/ul/li[3]/span
    # //*[@id="adyen-encrypted-form"]/fieldset/div[3]/div[2]/div/div/div/div/div[2]/div/ul/li[4]/span
    # //*[@id="adyen-encrypted-form"]/fieldset/div[3]/div[2]/div/div/div/div/div[2]/div/ul/li[4]/span
    # //*[@id="adyen-encrypted-form"]/fieldset/div[3]/div[2]/div/div/div/div/div[2]/div/ul/li[5]/span

    #YearButton
    driverName.find_element_by_xpath('//*[@id="adyen-encrypted-form"]/fieldset/div[3]/div[3]/div/div/div/a').click()
    #YearButtonVal
    yearVal = int(arrInfo[9]) - 2017 + 2
    yearXPath = '//*[@id="adyen-encrypted-form"]/fieldset/div[3]/div[3]/div/div/div/div/div[2]/div/ul/li[' + str(yearVal) + ']'
    driverName.find_element_by_xpath(yearXPath).click()

    #CVV val
    driverName.find_element_by_xpath('//*[@id="dwfrm_adyenencrypted_cvc"]').send_keys(arrInfo[10])

    #Click on button
    driverName.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[4]/div/button').click()
    time.sleep(120)





if __name__ == "__main__":
    main()
