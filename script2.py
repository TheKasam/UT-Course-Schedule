import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import bs4 as bs
import re
import mechanicalsoup
import time
import pickle
import sys
import smtplib
from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText
sys.setrecursionlimit(50000)


def main():
    with open("browser.pickle","rb") as f:
        browser = pickle.load(f)
        checkBrowserBool = checkBrowser(browser)


    feild = "bio"
    number = 325
    browser.open("https://utdirect.utexas.edu/apps/registrar/course_schedule/20182/results/?ccyys=20182&search_type_main=COURSE&fos_cn=" + feild+ "&course_number="+number)
    soup = browser.get_current_page()

    nextPageUrl = soup.find('a',{'id':'next_nav_link'})
    print(nextPageUrl.text)

main()
