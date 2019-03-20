import os
import sys
import xlrd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def main():

    workbookRead = xlrd.open_workbook("/Users/rahulbrahmal/Documents/Bot/dsmBot/excelFiles/gmailAccounts.xls")
    accounts = workbookRead.sheet_by_index(0)

    chromedriver = "/Users/rahulbrahmal/Documents/Bot/dsmBot/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.implicitly_wait(5)

    url = "http://newyork.doverstreetmarket.com/subscribe/";
    # driver.get(url)

    fileRead = open("names.rtf");

    rowRead = 1;
    for line in fileRead:
        if (rowRead <= accounts.nrows - 1):

            driver.get(url)

            names = line.split(" ")

            firstName = driver.find_element_by_name("Name")
            firstName.send_keys(names[0])
            lastName = driver.find_element_by_name("Surname")
            lastName.send_keys(names[1])
            email = driver.find_element_by_name("Email")
            emailVal = (accounts.cell_value(rowx = rowRead, colx = 0)).lower() + "@gmail.com"
            email.send_keys(emailVal);
            email.send_keys(Keys.ENTER);

            rowRead += 1

            driver.implicitly_wait(5);


if __name__ == "__main__":
    main();
