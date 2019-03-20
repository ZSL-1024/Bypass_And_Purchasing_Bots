var webdriver = require('selenium-webdriver');
var driver = new webdriver.Builder().forBrowser('chrome').build()
driver.get("http://www.google.com")
driver.findElement(webdriver.By.name('q'))
driver.findElement(webdriver.By.name('q')).sendKeys("testing testing 123")
driver.findElement(webdriver.By.className('sbico')).click()
driver.findElement(webdriver.By.className('sbico')).click()
driver.findElement(webdriver.By.className('sbico')).sendKeys(
