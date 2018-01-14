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

    ref = db.reference('users')
    data = ref.get()
    emailList = []
    for x in data:
        try:
            data[x]['following']
        except:
            pass
            emailList.append(data[x]['email'])


    emailList.append('saikasam98@gmail.com')
    emailFile = open("emailList1.txt",'w')


    for email in emailList:
        emailFile.write(email)
        print(email)
        msg = MIMEMultipart()
        msg['From'] = "support@utcourseupdates.com"
        msg['To'] = email
        msg['Subject'] = "Ut Course Updates"
        body = "Hello!\nWe see that you have an account at utcourseupdates.com but are not following any courses. If you had a problem adding a course it should be resolved now. If you still can't add it please respond to this email with the course you are unable to add!"
        body = body + "\n\nThanks!"
        body = body + "\nSupport at Ut Course Updates"
        body = body + "\n\nReply to this email requesting to delete your account to stop receiving emails."
        msg.attach(MIMEText(body, 'plain'))
        service = smtplib.SMTP('smtp.gmail.com', 587)
        service.starttls()
        service.login("support@utcourseupdates.com", "updatescourseut")
        text = msg.as_string()
        try:
            service.sendmail("support@utcourseupdates.com", email, text)
            print('sent')
        except:
            service.quit()
            print("This didn't work")
            continue
        service.quit()

main()
