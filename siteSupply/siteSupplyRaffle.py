import os
import sys
import xlrd
from selenium import webdriver
from twocaptchaapi import TwoCaptchaApi
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

def main():

    workbookRead = xlrd.open_workbook("/Users/rahulbrahmal/Documents/Bot/dsmBot/extraFiles/moreEmails.xls")
    #/Users/rahulbrahmal/Documents/Bot/dsmBot/excelFiles/gmailAccounts.xls
    accounts = workbookRead.sheet_by_index(0)

    workbookPostcodes = xlrd.open_workbook("/Users/rahulbrahmal/Documents/Bot/dsmBot/extraFiles/morePostcodes.xlsx")
    #/Users/rahulbrahmal/Documents/Bot/dsmBot/excelFiles/londonPostcodesCondensed.xlsx
    sheetPostcodes = workbookPostcodes.sheet_by_index(0)

    workbookPhone = xlrd.open_workbook("/Users/rahulbrahmal/Documents/Bot/dsmBot/extraFiles/moreNumbers.xlsx")
    #/Users/rahulbrahmal/Documents/Bot/dsmBot/excelFiles/phoneNumbers.xlsx
    sheetPhone = workbookPhone.sheet_by_index(0)

    chromedriver = "/Users/rahulbrahmal/Documents/Bot/dsmBot/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.implicitly_wait(60)

    url = "https://slamjamsocialism-drops.com/drops/8";

    # driver.get(url)

    fileRead = open("/Users/rahulbrahmal/Documents/Bot/dsmBot/extraFiles/neerav500.rtf");
    # #/Users/rahulbrahmal/Documents/Bot/dsmBot/excelFiles/names.rtf
    api = TwoCaptchaApi('9cccbd94c566a11cdb2727a97318748b')
    shoeSize = ""
    shoeIndex = 0;
    phoneNumberVal = ""
    lastDigits = 127537
    lastDigitsString = ""
    phoneIndex = 0;
    rowRead = 1;
    for line in fileRead:
        if (rowRead <= accounts.nrows - 1):

            if (shoeIndex == 0):
                shoeSize = "7"
                shoeIndex = 1
            elif (shoeIndex == 1):
                shoeSize = "8"
                shoeIndex = 2
            elif (shoeIndex == 2):
                shoeSize = "8"
                shoeIndex = 3
            elif (shoeIndex == 3):
                shoeSize = "9"
                shoeIndex = 4
            elif (shoeIndex == 4):
                shoeSize = "9"
                shoeIndex = 5
            elif (shoeIndex == 5):
                shoeSize = "10"
                shoeIndex = 6
            elif (shoeIndex == 6):
                shoeSize = "10"
                shoeIndex = 7
            elif (shoeIndex == 7):
                shoeSize = "11"
                shoeIndex = 8
            elif (shoeIndex == 8):
                shoeSize = "11"
                shoeIndex = 9
            elif (shoeIndex == 9):
                shoeSize = "12"
                shoeIndex = 10
            elif (shoeIndex == 10):
                shoeSize = "7"
                shoeIndex = 0
            # shoeSize = "Size US 8.5"

            lastDigits += 113462
            if (lastDigits > 990000):
                phoneIndex += 1
                lastDigits = 123537 - (8 * rowRead);


            lastDigitsString = str(lastDigits)
            middleDigit = str((sheetPhone.cell_value(rowx = phoneIndex, colx = 0)))

            phoneNumberVal = "07" + middleDigit[0:3] + lastDigitsString

            driver.get(url)

            names = line.split(" ")
            print (names[0] + " " + names[1])
            print ((accounts.cell_value(rowx = rowRead, colx = 0)).lower() + "@gmail.com")
            print (sheetPostcodes.cell_value(rowx = (10 * rowRead), colx = 0))
            print (phoneNumberVal)

            driver.implicitly_wait(30);
            nameFirst = driver.find_element_by_xpath('//*[@id="raffle1"]/div[1]/div[1]/input')
            nameFirst.send_keys(names[0])

            nameSecond = driver.find_element_by_xpath('//*[@id="raffle1"]/div[2]/div[1]/input')
            nameSecond.send_keys(names[1])

            email = driver.find_element_by_xpath('//*[@id="raffle1"]/div[3]/div[1]/input')
            emailVal = (accounts.cell_value(rowx = rowRead, colx = 0)).lower() + "@gmail.com"
            email.send_keys(emailVal);

            phoneNumber = driver.find_element_by_xpath('//*[@id="raffle1"]/div[4]/div[1]/input')
            phoneNumber.send_keys(phoneNumberVal)

            countryVal = driver.find_element_by_xpath('//*[@id="raffle1"]/div[5]/div[1]/div/div[1]/div/div/div[1]/input')
            countryVal.send_keys('United Kingdom of Great Britain and Northern Ireland')

            # countryValDropdown = driver.find_element_by_xpath('//*[@id="raffle1"]/div[5]/div[1]/div/ul/li/a/div')
            # countryValDropdown.click()

            city = driver.find_element_by_xpath('//*[@id="raffle1"]/div[6]/div[1]/input')
            city.send_keys("London")

            # postCode = driver.find_element_by_name("Postcode");
            # postCode.send_keys(sheetPostcodes.cell_value(rowx = (10 * rowRead), colx = 0))

            sizeSelection = Select(driver.find_element_by_xpath('//*[@id="status"]'));
            sizeSelection.select_by_visible_text(shoeSize);

            # buttonCaptcha = driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]/div[5]')
            # buttonCaptcha.click()

            with open('/my/captcha/path.png', 'rb') as captcha_file:
                captcha = api.solve(captcha_file)

            print(captcha.await_result())

            

            iframeArr = driver.find_elements_by_xpath('//*[@id="g-recaptcha"]/div/div/iframe')

            # Card Number

            driver.switch_to.frame(iframeArr[0])
            driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]').click()

            driver.switch_to_default_content()

            buttonSubmit = driver.find_element_by_xpath('//*[@id="raffle1"]/input')
            buttonSubmit.click();

            driver.wait(1);

            rowRead += 1

            driver.implicitly_wait(5);

            driver.get(url)

            print (rowRead)


if __name__ == "__main__":
    main()
