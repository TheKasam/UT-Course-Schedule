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

#firebase-adminsdk-jgy6n@courseschedule-8a816.iam.gserviceaccount.com
# Fetch the service account key JSON file contents
cred = credentials.Certificate('courseschedule-8a816-firebase-adminsdk-jgy6n-2f35d9eaad.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://courseschedule-8a816.firebaseio.com/'
})


def main():
    totalTime = 60 * 5
    startTime = 0
    endTime = 60 * 5
    while(True):

        timeToSleep = totalTime - (endTime - startTime)
        print(endTime,startTime)
        print(timeToSleep,"sec")
        if timeToSleep > 0:
            time.sleep(timeToSleep)

        startTime = time.time()

        print("new LOOOP")
        ###put out most infinate loop ###

        #logging in to course schedule
        with open("browser.pickle","rb") as f:
            browser = pickle.load(f)
            checkBrowserBool = checkBrowser(browser)
            if  checkBrowserBool == False:
                browser = logIn()




        #getting firebase data
        ref = db.reference('courses')
        data = ref.get()
        #print(data)
        #getting a list of keys

        try:
            dataKeysList = data.keys()
        except:
            endTime = time.time()
            continue


        for outerKey in dataKeysList:
            outerDict = data[outerKey]
            try:
                int(outerKey)
            #checking if there are inner courses
            except ValueError:


                #checking if values have been uploaded
                if len(outerDict) < 2:
                    #uploading values
                    queryType = data[outerKey]['queryType']

                    if queryType == 'course':
                        saveCourse(outerKey,browser)
                    elif queryType == 'prof':
                        saveProf(outerKey,browser)
                    endTime = time.time()
                    continue

                innerKeys = data[outerKey].keys()
                for innerKey in innerKeys:
                    if innerKey == 'queryType':
                        endTime = time.time()
                        continue
                    innerDict = data[outerKey][innerKey]
                    checkForUpdates(innerDict,browser,outerKey)
                endTime = time.time()
                continue

            if len(outerDict) < 7:
                saveUnique(outerKey,browser)
                endTime = time.time()
                continue

            checkForUpdates(outerDict,browser,False)

        endTime = time.time()
        print(dataKeysList)

def checkForUpdates(checkDict,browser,outerKey):
    unique = checkDict['unique']
    print("checking",outerKey,unique)
    ### GET SOUP ###
    browser.open("https://utdirect.utexas.edu/apps/registrar/course_schedule/20182/" + unique  + "/")
    soup = browser.get_current_page()

    course_a = soup.find(text=unique).parent
    course_tr = course_a.parent.parent

    webDict = {}

    try:
        webDict['days'] = course_tr.find('td',{'data-th':'Days'}).select_one('span').text
    except:
        webDict['days'] = " "
    try:
        webDict['hour'] = course_tr.find('td',{'data-th':'Hour'}).select_one('span').text
    except:
        webDict['hour'] = " "
    try:
        webDict['room'] = course_tr.find('td',{'data-th':'Room'}).select_one('span').text
    except:
        webDict['room'] = " "
    try:
        instructorLst = course_tr.find('td',{'data-th':'Instructor'}).text.strip().split(" ")
    except:
        instructorLst = ["None",'N']

    if instructorLst == ['']:
        instructorLst = ['None','N']
    instructor = instructorName(instructorLst)

    webDict['instructor'] = instructor

    try:
        webDict['status'] = course_tr.find('td',{'data-th':'Status'}).text
    except:
        webDict['status'] = " "
    webDict['unique'] = unique

    changed = []
    prev = []
    new = []
    for key in webDict:
        if webDict[key] != checkDict[key]:
            changed.append(key)
            new.append(webDict[key])
            prev.append(checkDict[key])
    if changed:
        print(changed, prev, new,outerKey,checkDict)

        if outerKey:

            courseId = outerKey

            print("Sent update")
            sendUpdate(unique, changed, prev, new,courseId) ### send emails ###
            print("Sent succesful")

            db.reference().child('courses').child(courseId).child(unique).update({
                'days':webDict['days'],
                'hour':webDict['hour'],
                'room':webDict['room'],
                'instructor':webDict['instructor'],
                'status':webDict['status'],
            })
            print("Saved")
        else:
            print("Sent update")
            courseId = unique
            sendUpdate(unique, changed, prev, new,courseId) ### send emails ###
            print("Sent succesful")

            db.reference().child('courses').child(unique).update({
                'days':webDict['days'],
                'hour':webDict['hour'],
                'room':webDict['room'],
                'instructor':webDict['instructor'],
                'status':webDict['status'],
            })
            print("Saved")


def sendUpdate(unique, changed, prev, new,courseId):
    print(courseId)
    ref = db.reference('courses_subscribers/' + courseId)

    try:
        values = ref.get().values()
    except:
        print("line 176ish")
        return

    print(values)
    for each in values:
        refe = db.reference('users/' + each + "/email")
        print(refe.get())
        recept = refe.get()
        msg = MIMEMultipart()
        msg['From'] = "help@utcourseupdates.com"
        msg['To'] = recept
        msg['Subject'] = "Your Course " + unique +" has changed.\n"
        body = "Your course " + unique + " has changed. "
        for i in range(len(changed)):
            print(i)
            body +=  "Its " + changed[i] + " has changed from " + prev[i] + " to " + new[i] + ".\n"
        body = body + "\nPlease log in and remove all courses at utcourseupdates.com or reply to this email to stop receiving emails."
        body = body + "\n\nThanks!"
        body = body + "\nHelp at Ut Course Updates"
        msg.attach(MIMEText(body, 'plain'))
        service = smtplib.SMTP('smtp.gmail.com', 587)
        service.starttls()
        service.login("help@utcourseupdates.com", "updatescourseut")
        text = msg.as_string()
        try:
            service.sendmail("help@utcourseupdates.com", recept, text)
        except:
            service.quit()
            print("This didn't work")
            service.sendmail("help@utcourseupdates.com", 'saikasam98@gmail.com', text)
            continue
        service.quit()

def instructorName(instructorLst):
    instructorLstLocal = []
    for x in range(len(instructorLst)):

        if instructorLst[x] != " " and instructorLst[x] != "" :
            instructorLstLocal.append(instructorLst[x].replace(",",""))

    if len(instructorLstLocal) > 1:

        return (instructorLstLocal[0] + " " + instructorLstLocal[1][0])
    else:
        return  (instructorLstLocal[0])


#gets data about course and saves it
def saveUnique(unique,browser):

    ### GET SOUP ###
    browser.open("https://utdirect.utexas.edu/apps/registrar/course_schedule/20182/" + unique  + "/")
    soup = browser.get_current_page()

    course_a = soup.find(text=unique).parent
    course_tr = course_a.parent.parent

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
        instructorLst = course_tr.find('td',{'data-th':'Instructor'}).text.strip().split(" ")
    except:
        instructorLst = ['None','N']
    if instructorLst == ['']:
        instructorLst = ['None','N']
    instructor = instructorName(instructorLst)
    try:
        status = course_tr.find('td',{'data-th':'Status'}).text
    except:
        status = " "


    db.reference().child('courses').child(unique).update({
        'unique':unique,
        'days':days,
        'hour':hour,
        'room':room,
        'instructor':instructor,
        'status':status,
    })
    print("saved unique")

def saveCourse(courseId,browser):

    newCouseId = ""
    if len(courseId.split(" ")) > 2:
        for x in range(len(courseId)):
            if x == 1 and courseId[x] == " ":
                newCouseId += '+'
            else:
                newCouseId += courseId[x]


    if newCouseId:
        courseIdLst= newCouseId.split(" ")
        feild = courseIdLst[0]
        number = courseIdLst[1]
    else:
        feild = courseId.split(" ")[0]
        number = courseId.split(" ")[1]


    ### GET SOUP ###
    browser.open("https://utdirect.utexas.edu/apps/registrar/course_schedule/20182/results/?ccyys=20182&search_type_main=COURSE&fos_cn=" + feild+ "&course_number="+number)
    soup = browser.get_current_page()

    course_a = soup.find('td',{'class':'course_header'}) #dont need

    nextPage = True
    while nextPage:
        print("PAge")
        b = soup.find_all('a',{'title':'Unique number'})
        for uniqueNum in b:
            unique = uniqueNum.text
            course_a = soup.find(text=unique).parent
            course_tr = course_a.parent.parent

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
                instructorLst = course_tr.find('td',{'data-th':'Instructor'}).text.strip().split(" ")
            except:
                instructorLst = ['None','N']
            if instructorLst == ['']:
                instructorLst = ['None','N']

            instructor = instructorName(instructorLst)

            try:
                status = course_tr.find('td',{'data-th':'Status'}).text
            except:
                status = " "

            db.reference().child('courses').child(courseId).child(unique).update({
                'unique':unique,
                'days':days,
                'hour':hour,
                'room':room,
                'instructor':instructor,
                'status':status,
            })
            print("saved course")
        try:
            nextPageUrl = soup.find('a',{'id':'next_nav_link'})['href']
            nextPage = True
            browser.open("https://utdirect.utexas.edu/apps/registrar/course_schedule/20182/results/"+nextPageUrl)
            soup = browser.get_current_page()
        except:
            nextPage = False
def saveProf(prof,browser):

    name = prof.split()
    lName = name[0]
    fName = name[1]

    ### GET SOUP ###
    browser.open("https://utdirect.utexas.edu/apps/registrar/course_schedule/20182/results/?ccyys=20182&search_type_main=INSTR&instr_last_name=" + lName + "&instr_first_initial=" + fName)
    soup = browser.get_current_page()


    b = soup.find_all('a',{'title':'Unique number'})
    for uniqueNum in b:
        unique = uniqueNum.text
        course_a = soup.find(text=unique).parent
        course_tr = course_a.parent.parent

        days = course_tr.find('td',{'data-th':'Days'}).select_one('span').text
        hour = course_tr.find('td',{'data-th':'Hour'}).select_one('span').text
        room = course_tr.find('td',{'data-th':'Room'}).select_one('span').text
        instructorLst = course_tr.find('td',{'data-th':'Instructor'}).text.split(" ")
        instructor = instructorName(instructorLst)
        status = course_tr.find('td',{'data-th':'Status'}).text

        db.reference().child('courses').child(prof).child(unique).update({
            'unique':unique,
            'days':days,
            'hour':hour,
            'room':room,
            'instructor':instructor,
            'status':status,
        })

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
