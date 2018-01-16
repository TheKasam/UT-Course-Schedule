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

    # emailFile = open("emailList1.txt",'r')
    # sennt = emailFile.read().split(" ")
    #

    # ref = db.reference()
    # data = ref.get()
    # print(data)
    # ref = db.reference('users')
    # data = ref.get()
    # print(len(data))
    emailList = []
    # for x in data:
    #     # if data[x]['email'] not in sennt:
    #     try:
    #         data[x]['following']
    #     except:
    #
    #         emailList.append(data[x]['email'])


    emailList.append('saikasam98@gmail.com')
    # emailList.remove('ikunge@utexas.edu')
    # emailList.remove('chuffithetugboatcoach37@gmail.com')
    # print(len(emailList))
    # emailFile = open("emailList2.txt",'w')


    for email in emailList:
        # emailFile.write(email)
        print(email)
        msg = MIMEMultipart()
        msg['From'] = "help@utcourseupdates.com"
        msg['To'] = email
        msg['Subject'] = "Ut Course Updates"
        body = "Hello!\n 33675 went from waitlisted to closed."
        body = body + "\n\nThanks!"
        body = body + "\nHelp at Ut Course Updates"
        body = body + "\n\nReply to this email requesting to delete your account to stop receiving emails."
        msg.attach(MIMEText(body, 'plain'))
        service = smtplib.SMTP('smtp.gmail.com', 587)
        service.starttls()
        service.login("help@utcourseupdates.com", "updatescourseut")
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
