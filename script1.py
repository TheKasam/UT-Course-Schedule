import pickle
import re
import mechanicalsoup
import sys



with open("sp500tickers.pickle","rb") as f:
    browser = pickle.load(f)

link = 'https://utdirect.utexas.edu/apps/registrar/course_schedule/20182/32975/'
browser.open(link)
soup = browser.get_current_page()
title = soup.title.text


ans = '0'

if title == 'Page not found':
    pass

elif soup.find('div',{'class':'error'}) == 'No class was found for your input.':

    pass

else:
    ans = '1'


dataToSendBack = ans
print(dataToSendBack)

sys.stdout.flush()
