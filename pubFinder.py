import csv
import time
import codecs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import tkinter

root = tkinter.Tk()
root.withdraw()

nothingFound = 'No results were found'

def readFile():

    fileName = 'sampleList.csv'
    checkList = []
    with codecs.open(fileName, 'r', encoding='utf-8') as f:
        a = csv.reader(f)
        checkList = list(a)

    return checkList

def peformSearch(driver,checkString):
    searchBox = driver.find_element_by_css_selector('#SearchTerm1')
    searchBox.clear()
    searchBox.send_keys(checkString)
    searchBox.send_keys(Keys.ENTER)
    time.sleep(1.5)
    pageSource = driver.page_source

    ftLinkList = []
    ftLinks = driver.find_elements_by_class_name('ft-access-option')
    for link in ftLinks:
        ftLinkList.append(link.text)
    time.sleep(1)
    return (pageSource, ftLinkList)


def checkISSN(driver, checkString, vendorName='Not Provided', startDate='NA', endDate='NA'):

    pageSource, pubs = peformSearch(driver,checkString)

    noResults = False
    if nothingFound in pageSource:
        noResults = True
        print('No Results for '+str(checkString))


    vendorMatch = 'Not Provided'
    if vendorName != 'Not Provided':
        if vendorName in pubs:
            vendorMatch = True
        # add the vendor search data later

    startDateMatch = 'NA'
    if startDate != 'NA':
        pass

    endDateMatch = 'NA'
    if endDate != 'NA':
        pass

    return([checkString,noResults,vendorName, vendorMatch, startDate, startDateMatch, endDate, endDateMatch])

def openConnection():
    # establish login
    driver = webdriver.Chrome()
    driver.get("http://search.ebscohost.com/login.aspx?direct=true&db=edspub&type=44&site=eds-live&bquery=")

    return driver

def writeResults(resultList):
    resultsLog = 'Results.csv'
    with codecs.open(resultsLog, 'a', encoding='utf-8') as x:
        wr = csv.writer(x,quoting=csv.QUOTE_ALL)
        wr.writerow(resultList)

def checkISSNList():
    driver = openConnection()
    checkList = readFile()

    for issn in checkList:
        checkString = issn[0]
        vendorName = issn[1]
        startDate = issn[2]
        endDate = issn[3]

        results = checkISSN(driver, checkString, vendorName, startDate, endDate)
        writeResults(results)


    driver.close()
