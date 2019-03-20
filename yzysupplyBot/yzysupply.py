import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    chromedriver = "chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver

    # billingShipping = open('billingShipping.txt', 'r')
    # idx = 0
    # # dataVals = []
    # # for data in billingShipping:
    # #     dataVals.insert(idx, data)
    # #     idx += 1
    # #

    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--proxy-server=%s' % proxy Address here)
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(chromedriver, chrome_options = chrome_options)

    url = "https://yeezysupply.com/collections/footwear"

    driver.get(url)

    print ("Opening Page")
    driver.implicitly_wait(8)
    i = 1
    while (i <= 40):
        driver.implicitly_wait(50)
        strTemp = '//*[@id="js-main"]/div/a[' + str(i) + ']'
        xpathObj = driver.find_element_by_xpath(strTemp)
        textVal = xpathObj.get_attribute('href')

        # if (("yeezy-boost-350" in textVal.lower()) or ("yeezy-350" in textVal.lower()) or ("boost-350" in textVal.lower()) or ("350" in textVal.lower())):
        #     print "Found Match"
        #     driver.find_element_by_xpath(strTemp).click()
        #     break;

        if (('mens-nubuck-military-boot' in textVal.lower())):
            idVal = xpathObj.get_attribute('data-id')
            driver.find_element_by_xpath(strTemp).click()
            break

        i += 1

    print ("Found ID and selected it")
    # Clicks on the correct size for the shoe and checks out
    driver.implicitly_wait(10)
    xpathSizeSelector = '//*[@id="P-' + str(idVal) + '"]/div[2]/form/div[2]/div/select'

    # waitFirst = WebDriverWait(driver, 100000000)
    # elementFirst = waitFirst.until(EC.element_to_be_clickable((By.XPATH, xpathSizeSelector)))
    select = Select(driver.find_element_by_xpath(xpathSizeSelector))

    j = 2
    while (j <= len(select.options)):
        driver.implicitly_wait(10)
        xpathSizeSpecific = '//*[@id="P-' + str(idVal) + '"]/div[2]/form/div[2]/div/select/option[' + str(j) + ']'
        sizeObj = driver.find_element_by_xpath(xpathSizeSpecific)
        textSelected = sizeObj.get_attribute('class')
        ifSizeText = sizeObj.text.lower()
        # print (ifSizeText)
        #Clicks on first not sold out
        if (("sold-out" not in textSelected.lower()) or ("size" not in ifSizeText)):
            sizeObj.click()
            xpathPurchaseButton = '//*[@id="P-' + str(idVal) + '"]/div[2]/form/input'
            break;

        j += 1

    driver.implicitly_wait(20)
    driver.find_element_by_xpath(xpathPurchaseButton).click()

    print ("Selects size and clicks button")
    waitOne = WebDriverWait(driver, 100000000)
    elementOne = waitOne.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="js-main"]/div/form/div/div[3]/input[2]')))

    # Clicks on the check out button
    # driver.switch_to_frame('tmx_tags_iframe')
    # driver.implicitly_wait(100)
    # time.sleep(2)
    buttonCheckOut = driver.find_element_by_xpath('//*[@id="js-main"]/div/form/div/div[3]/input[2]')
    # a = driver.find_elements_by_css_selector("iframe")
    # driver.switch_to_frame(a[0])
    buttonCheckOut.click()
    # button = driver.switch_to_frame(a[0])
    # button.click()

    # print a
    # print (len(a))
    # driver.execute_script("document.getElementsByClassName('K__button CA__button-checkout')[0].click()")

    # Waiting in Queue
    waitTwo = WebDriverWait(driver, 30)
    element = waitTwo.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout_email"]')))
    #Autofill Billing
    print ("In billing section. Starting autofill.")

    driver.find_element_by_xpath('//*[@id="checkout_email"]').send_keys('rahulvbrahmal+1@gmail.com')
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]').send_keys('Rahul')
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_last_name"]').send_keys('Viraj Brahmal')
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]').send_keys('848 Spring Street NW')
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address2"]').send_keys('Apartment 1502')
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]').send_keys('Atlanta')

    # Country Dropdown
    countryObj = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_country"]')
    select = Select(countryObj)
    k = 1
    while (k <= len(select.options)):
        xpathCountry = '//*[@id="checkout_shipping_address_country"]/option[' + str(k) + ']'
        countryNameObj = driver.find_element_by_xpath(xpathCountry)
        countryName = countryNameObj.text
        if ('United States' in countryName):
            countryNameObj.click()
            break

        k += 1

    # State Dropdown
    stateObj = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_province"]')
    select = Select(stateObj)
    m = 1
    while (k <= len(select.options)):
        xpathState = '//*[@id="checkout_shipping_address_country"]/option[' + str(k) + ']'
        stateNameObj = driver.find_element_by_xpath(xpathState)
        stateName = stateNameObj.text
        if ('Georgia' in stateName):
            stateNameObj.click()
            break
        m += 1

    # Zip Code
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]').send_keys('30308')

    # Phone Number
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_phone"]').send_keys('6788261983')

    driver.implicitly_wait(10)
    # Continue to shipping
    driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/form/div[2]/button').click()

    print ("Clicking on shipping method")
    # Click on cheapest shipping option
    driver.find_element_by_xpath('//*[@id="checkout_shipping_rate_id_shopify-standard20ground20shipping20520to20720days-2000"]').click()

    print ("Going to payment method")
    # Continue to payment method
    driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/form/div[2]/button').click()

    # Billing Info
    print ("Autofilling card info")

    driver.implicitly_wait(30)
    # a = driver.find_elements_by_css_selector("iframe")
    iframeArr = driver.find_elements_by_class_name('card-fields-iframe')

    # Card Number

    driver.switch_to.frame(iframeArr[0])
    driver.find_element_by_xpath('//*[@id="number"]').send_keys('1222343212341323')

    # Name on Card

    driver.switch_to_default_content()
    driver.switch_to.frame(iframeArr[1])
    driver.find_element_by_xpath('//*[@id="name"]').send_keys('Rahul V Brahmal')

    #MM/YY
    driver.switch_to_default_content()
    driver.switch_to.frame(iframeArr[2])
    driver.find_element_by_xpath('//*[@id="expiry"]').send_keys('082019')

    #CVV

    driver.switch_to_default_content()
    driver.switch_to.frame(iframeArr[3])
    driver.find_element_by_xpath('//*[@id="verification_value"]').send_keys('012')

    # Complete order button
    driver.switch_to_default_content()
    driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/form/div[2]/button').click()

    print ("DONE")

    time.sleep(3600)
if __name__ == "__main__":
    main()
