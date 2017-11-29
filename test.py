
import re
import mechanicalsoup
import requests
import time



def main():

    # Connect to Google
    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://utdirect.utexas.edu/apps/registrar/course_schedule/20182/")


    # Fill-in the form
    browser.select_form('form[name="Login"]')
    #browser.get_current_form().print_summary()
    browser["IDToken1"] = "sm69255"
    browser["IDToken2"] = "Sai1baba"

    browser.submit_selected(btnName="Login.Submit")

    stall(8)
    #resp2 = requests.get("https://utdirect.utexas.edu/apps/registrar/course_schedule/20179/results/?ccyys=20179&fos_fl=ASE&level=L&search_type_main=FIELD&x=114&y=13")
    browser.select_form('form[name="Response"]')
    browser.submit_selected()
    #browser.open("https://utdirect.utexas.edu/apps/registrar/course_schedule/20182/")


    browser.select_form('form[name="getform"]')
    browser.submit_selected()

    start = time.time()
    end = time.time()
    while end - start < 8:
        end = time.time()
    browser.open("https://utdirect.utexas.edu/apps/registrar/course_schedule/20182/results/?ccyys=20182&search_type_main=FIELD&fos_fl=ASL&level=L&x=65&y=21")

    print(browser.get_current_page())


def stall(sec):
    start = time.time()
    end = time.time()
    while end - start < sec:
        end = time.time()
