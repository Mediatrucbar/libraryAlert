from bs4 import BeautifulSoup

class Books:

    def getBooksList(self):
        data = []

        #Open buffer to get all html code
        fileBuffer = open('../3_others/webDump.html', 'r')
        web_page = BeautifulSoup(fileBuffer, "html.parser")

        table = web_page.find('table', "tablesorter loans-history")
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')

        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])

        return data
