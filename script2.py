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



    feild = "mis"
    number = '325'
    browser.open("https://utdirect.utexas.edu/apps/registrar/course_schedule/20182/results/?ccyys=20182&search_type_main=COURSE&fos_cn=" + feild+ "&course_number="+number)
    soup = browser.get_current_page()

    # browser.open("https://utdirect.utexas.edu/apps/registrar/course_schedule/20182/results/"+nextPageUrl)
    # soup = browser.get_current_page()

    course_a = soup.find('td',{'class':'course_header'})
    nextPage = True

    while nextPage:
        print("PAge")
        b = soup.find_all('a',{'title':'Unique number'})
        for uniqueNum in b:
            unique = uniqueNum.text
            course_a = soup.find(text=unique).parent
            course_tr = course_a.parent.parent
            print(unique)
            try:
                days = course_tr.find('td',{'data-th':'Days'}).select_one('span').text
            except:
                days = " "
            try:
                hour = course_tr.find('td',{'data-th':'Hour'}).select_one('span').text
            except:
                hour = " "
            try:
                room = course_tr.find('td',{'data-th':'Room'}).select_one('span').text
            except:
                room = " "

        try:
            nextPageUrl = soup.find('a',{'id':'next_nav_link'})['href']
            nextPage = True
        except:
            nextPage = False

main()
