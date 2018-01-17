import pickle
import mechanicalsoup
import sys
import time

def main():

    # with open("browser.pickle","rb") as f:
    #     browser = pickle.load(f)
    #     checkBrowserBool = checkBrowser(browser)
    #     if  checkBrowserBool == False:
    #         browser = logIn()

    browser = logIn()
    sleepSec = 6 * 60
    print(sleepSec)
    time.sleep(sleepSec)








def logIn():
    # Connect to Google
    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://utdirect.utexas.edu/apps/registrar/course_schedule/20182/")

    # Fill-in the form
    browser.select_form('form[name="Login"]')
    #browser.get_current_form().print_summary()
    browser["IDToken1"] = "mj27879"
    browser["IDToken2"] = "Touchstone789"

    browser.submit_selected(btnName="Login.Submit")

    stall(8)

    browser.select_form('form[name="Response"]')
    browser.submit_selected()

    stall(8)

    browser.select_form('form[name="getform"]')
    browser.submit_selected()

    stall(8)
    with open("browser.pickle","wb") as f:
        pickle.dump(browser,f)
    #browser.open("https://utdirect.utexas.edu/apps/registrar/course_schedule/20182/results/?ccyys=20182&search_type_main=INSTR&instr_last_name=CONLEY&instr_first_initial=&x=40&y=9")
    return(browser)

def stall(sec):
    start = time.time()
    end = time.time()
    while end - start < sec:
        end = time.time()

def checkBrowser(browser):

    ### GET SOUP ###
    browser.open("https://utdirect.utexas.edu/apps/registrar/course_schedule/20182/" + '12345'  + "/")
    soup = browser.get_current_page()
    try:
        course_a = soup.find(text='12345').parent
        print(True)
        return True
    except:
        print(False)
        return False


main()
