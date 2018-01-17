import time


def main():

    with open("browser.pickle","rb") as f:
        browser = pickle.load(f)
        checkBrowserBool = checkBrowser(browser)
        if  checkBrowserBool == False:
            browser = logIn()


    sleepSec = 6 * 60
    print(sleepSec)
    time.sleep(sleepSec)







main()


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
