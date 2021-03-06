import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import bs4 as bs
import re
import mechanicalsoup
import time

#firebase-adminsdk-jgy6n@courseschedule-8a816.iam.gserviceaccount.com
# Fetch the service account key JSON file contents
cred = credentials.Certificate('courseschedule-8a816-firebase-adminsdk-jgy6n-2f35d9eaad.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://courseschedule-8a816.firebaseio.com/'
})


def main():

    #getting firebase data
    ref = db.reference('courses')
    data = ref.get()

    print(data)


main()
