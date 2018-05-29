from bs4 import BeautifulSoup

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

    def openWebPage(self):
        fileBuffer = open('../3_others/webDump.html', 'r')
        soup = BeautifulSoup(fileBuffer, "html.parser")
        return soup

