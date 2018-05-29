#!/usr/bin Python

from bs4 import BeautifulSoup

print('Crosne library Alert !!')

#Open buffer to get all html code
fileBuffer = open('../3_others/webDump.html', 'r')
soup = BeautifulSoup(fileBuffer, "html.parser")
data = []
#Find all loans history table
table = soup.find('table', "tablesorter loans-history")
table_body = table.find('tbody')

rows = table_body.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

print(data)

