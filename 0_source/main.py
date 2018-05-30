#!/usr/bin/python

from books import *

print('Crosne library Alert !!')

bookList = Books()

soup = bookList.openWebPage()
data = bookList.getBooksList(soup)

print(htmlBuffer)

