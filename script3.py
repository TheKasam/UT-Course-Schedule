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
cred = credentials.Certificate('CourseSchedule-3bcfcbe9da61.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://courseschedule-8a816.firebaseio.com/'
})


def main():


    emailList = [ 'madalyn4@gmail.com', 'adamjbressler@yahoo.com', 'skyler.cheyenne.jennings@gmail.com', 'daniellehyde@utexas.edu', 'kristinmobryan@gmail.com', 'faria.khimani@utexas.edu', 'tranmyle12@gmail.com', 'stevenehuang@gmail.com', 'aaronbkwok@gmail.com', 'parimi.nehal@gmail.com', 'natitribaldos@gmail.com', 'anirudh.vadrevu@gmail.com', 'vince.sluss@yahoo.com', 'saikasam98@gmail.com']

    # emailFile = open("emailList1.txt",'r')
    # sennt = emailFile.read().split(" ")


    # ref = db.reference()
    # data = ref.get()
    # ref = db.reference('users')
    # data = ref.get()
    # print(len(data))
    # emailList = []
    # for x in data:
    #     # if data[x]['email'] not in sennt:
    #     try:
    #         data[x]['following']
    #         emailList.append(data[x]['email'])
    #     except:
    #         print("rip")
    #
    #
    # emailList.append('saikasam98@gmail.com')
    #
    # print(len(emailList))
    # emailFile = open("emailList23.txt",'w')

    print(emailList)
    for email in emailList:
        # emailFile.write(email)
        print(email)
        msg = MIMEMultipart()
        msg['From'] = "help@utcourseupdates.com"
        msg['To'] = email
        msg['Subject'] = "Ut Course Updates is Shutting down for the semester"
        body = "Hello!"
        body = body + "\n Thank you all for using this service this year, had a few issues from the UT Computational Service at the end but hopefully by next semester we'll get in touch with them and have the kinks ironed out!"
        body = body + "\n\nThanks!"
        body = body + "\nHelp at Ut Course Updates"
        msg.attach(MIMEText(body, 'plain'))
        service = smtplib.SMTP('smtp.gmail.com', 587)
        service.starttls()
        service.login("support@utcourseupdates.com", "updatescourseut")
        text = msg.as_string()
        service.sendmail("help@utcourseupdates.com", email, text)
        print('sent')
        try:
            service.sendmail("help@utcourseupdates.com", email, text)
            print('sent')
        except:

            service.quit()
            print("This didn't work")
            continue
        service.quit()

main()
