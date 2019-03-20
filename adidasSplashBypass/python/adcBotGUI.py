import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QMenu
#from PyQt5.QtGui import QIcon, QKeySequence
# from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class AppScreen(QWidget):

    def __init__(self):
        super(AppScreen, self).__init__()
        self.title = 'Adidas Exploit Bot'
        self.left = 0
        self.top = 0
        self.width = 500
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createAndPopulateTable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # menu = self.menuBar().addMenu('File')
        # Show widget
        self.show()

    def createAndPopulateTable(self):

       # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(('Driver Name', 'Driver State', 'Running Process'))

        # Set up chromedriver
        chromedriver = "/usr/local/bin/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        url = "http://whatismyipaddress.com"
        i = 0
        proxyList = open("proxies.txt", "r")
        for proxy in proxyList:
            driverName = "driver" + str(i)
            driverStrName = "driver" + str(i)

            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--proxy-server=%s' % proxy)
            # chrome_options.add_argument('--headless') # for running headless section.

            driverName = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
            driverName.get(url)

            tableItem = QTableWidgetItem(driverStrName)
            tableItem.setFlags(tableItem.flags() & ~Qt.ItemIsEditable)

            self.tableWidget.setItem(i, 0, tableItem)
            self.tableWidget.setItem(i, 1, QTableWidgetItem("Loading Page"))
            self.tableWidget.setItem(i, 2, QTableWidgetItem("Loading WhatIsMyIP"))

        self.tableWidget.move(0,0)

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            currentVal = currentQTableWidgetItem.text()
            if ("driver" in currentVal):
                # Method to call driver
                # driverChangeLink(driverStrName, "http://www.google.com")
                print ("CLICKED")
            # print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    def contextMenuEvent(self, event):
        self.menu = QMenu(self)
        testAction = QAction('Test', self)
        testAction.triggered.connect(lambda: self.renameSlot(event))
        self.menu.addAction(testAction)

        # Add other actions here

        self.menu.popup(QCursor.pos())

    def testAction(self, event):
        print ("Test has been called")

        #HAVE TO ADD DIFFERENT MENU ACTION CLICKS HERE

        # menu.addAction(QAction("Cu&t", self, shortcut=QKeySequence.Cut,
        #         statusTip="Cut the current selection's contents to the clipboard",
        #         triggered=self.cut))
        # X
        # menu.exec_(event.globalPos())

    # def driverChangeLink(name, newUrl):
    #         name.get(newUrl)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AppScreen()
    sys.exit(app.exec_())
