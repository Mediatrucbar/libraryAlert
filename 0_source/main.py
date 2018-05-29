#!/usr/bin/python

from bs4 import BeautifulSoup
from books import *

print('Crosne library Alert !!')

data = []
bookList = Books()
data = bookList.getBooksList()

#Find all loans history table
print(data)

