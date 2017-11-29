import re
import mechanicalsoup
import bs4 as bs



with open("soup.html") as f:
  soup = bs.BeautifulSoup(f,'lxml')


u = soup.find('a',{'title':"Unique number"})
b = u.parent.parent
print(b.get('class'))

def fineUnique():
    pass





def findHeaders():
    headers = []
    for header in soup.find_all('td',{'class':'course_header'}):
        headers.append(header)
    return headers
