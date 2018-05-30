from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Books:

    def getBooksList(self, web_page):
        data = []
        table = web_page.find('table', "tablesorter loans-history")
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')

        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])

        return data

    def openWebPageTest(self):
        fileBuffer = open('../3_others/webDump.html', 'r')
        soup = BeautifulSoup(fileBuffer, "html.parser")
        return soup

    def openWebPage(self):
        cardNumber = "VYVS001762"
        birthYear = "1990"

        driver = webdriver.Chrome(executable_path = '/home/damien/Dev/library_alert/0_source/chromedriver')
        driver.get('http://bibliotheques.vyvs.fr/index/index/id_profil/67')
        elem = driver.find_element_by_id("username")
        elem.send_keys(cardNumber)
        elem = driver.find_element_by_id("password")
        elem.send_keys(birthYear)
        elem.send_keys(Keys.ENTER)
        elem = driver.find_element_by_class_name("account-link")
        elem.click()
        driver.get('http://bibliotheques.vyvs.fr/abonne/loans-history/id_profil/67')
        htmlBuffer = driver.page_source



