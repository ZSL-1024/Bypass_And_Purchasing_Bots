import os
import sys
import xlrd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

def main():

    workbookRead = xlrd.open_workbook("/Users/rahulbrahmal/Documents/Bot/dsmBot/excelFiles/gmailAccounts.xls")
    accounts = workbookRead.sheet_by_index(0)

    workbookPostcodes = xlrd.open_workbook("/Users/rahulbrahmal/Documents/Bot/dsmBot/excelFiles/londonPostcodesCondensed.xlsx")
    sheetPostcodes = workbookPostcodes.sheet_by_index(0)

    workbookPhone = xlrd.open_workbook("/Users/rahulbrahmal/Documents/Bot/dsmBot/excelFiles/phoneNumbers.xlsx")
    sheetPhone = workbookPhone.sheet_by_index(0)

    workbookBirthday = xlrd.open_workbook("/Users/rahulbrahmal/Documents/Bot/dsmBot/excelFiles/phoneNumbers.xlsx")
    sheetBirthday = workbookBirthday.sheet_by_index(0)

    chromedriver = "/Users/rahulbrahmal/Documents/Bot/dsmBot/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.implicitly_wait(5)

    url = "https://www.nike.com/events-registration/event?id=89091&register=true";

    # driver.get(url)

    fileRead = open("/Users/rahulbrahmal/Documents/Bot/dsmBot/excelFiles/names.rtf");
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
                shoeSize = "US 6 (UK5.5)"
                shoeIndex = 1
            elif (shoeIndex == 1):
                shoeSize = "US 6.5 (UK 6)"
                shoeIndex = 2
            elif (shoeIndex == 2):
                shoeSize = "US 7 (UK 6)"
                shoeIndex = 0

            lastDigits += 113462
            if (lastDigits > 990000):
                phoneIndex += 1
                lastDigits = 123537 - (8 * rowRead);


            lastDigitsString = str(lastDigits)
            middleDigit = str((sheetPhone.cell_value(rowx = phoneIndex, colx = 0)))

            phoneNumberVal = "07" + middleDigit[0:3] + lastDigitsString

            driver.get(url)

            names = line.split(" ")
            emailVal = (accounts.cell_value(rowx = rowRead, colx = 0)).lower() + "@gmail.com"
            birthdayVal = str((sheetBirthday.cell_value(rowx = rowRead - 1, colx = 0))).split(" ")
            # print (names[0] + " " + names[1])
            # print ((accounts.cell_value(rowx = rowRead, colx = 0)).lower() + "@gmail.com")
            # print (sheetPostcodes.cell_value(rowx = (10 * rowRead), colx = 0))
            # print (phoneNumberVal)

            # joinLink = driver.find_element_by_class_name("login-text")
            # joinLink.click()

            nikePlusLogin = driver.find_elements_by_class_name("current-member-signin")
            for e in nikePlusLogin:
                e.click()

            emailRegister = driver.find_value_by_name("emailAddress")
            emailRegister.send_keys(emailVal)

            passwordRegister = driver.find_value_by_name("password")
            passwordRegister.send_keys("Norton00")

            firstNameRegister = driver.find_value_by_name("firstName")
            firstNameRegister.send_keys(names[0])

            lastNameRegister = driver.find_value_by_name("lastName")
            lastNameRegister.send_keys(names[1])

            birthDate = driver.find_element_by_name("dateOfBirth")
            birthDate.send_keys(birthdayVal[0] + birthdayVal[1] + birthdayVal[2])

            gender = driver.find_element_by_class_name("nike-unite-gender-buttons gender nike-unite-component")
            gender.click()

            createAccount = driver.find_element_by_class_name("nike-unite-submit-button joinSubmit nike-unite-component")
            creatAccount.click()

            continueButton = driver.find_element_by_class_name("nsg-button nsg-bg--black register-next-step-cta js-nextStepCta")
            continueButton.click()

            phoneNumber = driver.find_element_by_id("field4")
            phoneNumber.send_keys(phoneNumberVal)

            sizeSelection = Select(driver.find_element_by_class_name("element-container nsg-font-family--platform ng-pristine ng-isolate-scope ng-invalid ng-invalid-empty has-visited ng-touched"));
            sizeSelection.select_by_visible_text(shoeSize);

            sizeSelection = Select(driver.find_element_by_class_name("element-container nsg-font-family--platform ng-pristine ng-isolate-scope ng-invalid ng-invalid-empty has-visited has-focus ng-touched"));
            sizeSelection.select_by_visible_text(shoeSize);

            checkBox = driver.find_element_by_id("field27")
            checkBox.click()

            submitButton = driver.find_element_by_class_name("button-nike nsg-font-family--platform button-large dark-grey button-reserve")
            submitButton.click()

            postCode.send_keys(Keys.ENTER);

            rowRead += 1

            driver.implicitly_wait(5);


if __name__ == "__main__":
    main()
