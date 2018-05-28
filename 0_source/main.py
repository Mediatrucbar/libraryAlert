#!/usr/bin Python

from bs4 import BeautifulSoup

print ('Hello World !')

#Open buffer to get all html code
fileBuffer = open('../3_others/webDump.html', 'r')
soup = BeautifulSoup(fileBuffer, "html.parser")

#Find all loans history table
allLoansHistory = soup.find_all('table', "tablesorter loans-history")

for tbody in allLoansHistory:
    for tr in tbody:
        for td in tr:
            i=+1
            print(i)
            if(i==7):
                print(td.get_text())

