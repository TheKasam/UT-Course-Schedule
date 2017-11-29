
import re
import mechanicalsoup
import requests
import time



def main():
    browser = logIn()
    page = browser.get_current_page()
    with open("soup.html", "w") as file:
        file.write(str(page))


def logIn():
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


    browser.select_form('form[name="Response"]')
    browser.submit_selected()

    stall(8)

    browser.select_form('form[name="getform"]')
    browser.submit_selected()

    stall(8)

    browser.open("https://utdirect.utexas.edu/apps/registrar/course_schedule/20182/results/?ccyys=20182&search_type_main=FIELD&fos_fl=ASL&level=L&x=65&y=21")
    return(browser)


def stall(sec):
    start = time.time()
    end = time.time()
    while end - start < sec:
        end = time.time()






main()
