import os
import sys
import xlrd
from selenium import webdriver
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
    driver.implicitly_wait(5)

    url = "http://london.doverstreetmarket.com/nike/05.html";

    # driver.get(url)

    fileRead = open("/Users/rahulbrahmal/Documents/Bot/dsmBot/extraFiles/neerav500.rtf");
    #/Users/rahulbrahmal/Documents/Bot/dsmBot/excelFiles/names.rtf
    shoeSize = ""
    shoeIndex = 0;
    phoneNumberVal = ""
    lastDigits = 127537
    lastDigitsString = ""
    phoneIndex = 0;
    rowRead = 1;
    for line in fileRead:
        if (rowRead <= accounts.nrows - 1):

            # if (shoeIndex == 0):
            #     shoeSize = "Size US 8"
            #     shoeIndex = 1
            # elif (shoeIndex == 1):
            #     shoeSize = "Size US 8.5"
            #     shoeIndex = 2
            # elif (shoeIndex == 2):
            #     shoeSize = "Size US 7"
            #     shoeIndex = 0
            shoeSize = "Size US 8.5"

            lastDigits += 113462
            if (lastDigits > 990000):
                phoneIndex += 1
                lastDigits = 123537 - (8 * rowRead);


            lastDigitsString = str(lastDigits)
            middleDigit = str((sheetPhone.cell_value(rowx = phoneIndex, colx = 0)))

            phoneNumberVal = "07" + middleDigit[0:3] + lastDigitsString

            driver.get(url)

            names = line.split(" ")
            # print (names[0] + " " + names[1])
            # print ((accounts.cell_value(rowx = rowRead, colx = 0)).lower() + "@gmail.com")
            # print (sheetPostcodes.cell_value(rowx = (10 * rowRead), colx = 0))
            # print (phoneNumberVal)

            fullName = driver.find_element_by_name("Name")
            fullName.send_keys(names[0] + " " + names[1])
            email = driver.find_element_by_name("Email")
            emailVal = (accounts.cell_value(rowx = rowRead, colx = 0)).lower() + "@gmail.com"
            email.send_keys(emailVal);
            phoneNumber = driver.find_element_by_name("Mobile")
            phoneNumber.send_keys(phoneNumberVal)
            city = driver.find_element_by_name("City")
            city.send_keys("London")
            postCode = driver.find_element_by_name("Postcode");
            postCode.send_keys(sheetPostcodes.cell_value(rowx = (10 * rowRead), colx = 0))
            sizeSelection = Select(driver.find_element_by_id("shoesize"));
            sizeSelection.select_by_visible_text(shoeSize);

            button = driver.find_element_by_id("ButtonSubmit")
            button.click()

            rowRead += 1

            driver.implicitly_wait(5);

            driver.get(url)

            print (rowRead)


if __name__ == "__main__":
    main()
