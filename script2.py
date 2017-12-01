import sys
import time
import re
import mechanicalsoup
import pickle


browser = mechanicalsoup.StatefulBrowser()
browser.open("https://www.google.com/")
soup = browser.get_current_page()


with open("sp500tickers.pickle","wb") as f:
    pickle.dump(browser,f)
