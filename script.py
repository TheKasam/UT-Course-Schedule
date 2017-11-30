import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import re
import mechanicalsoup
import bs4 as bs

#firebase-adminsdk-jgy6n@courseschedule-8a816.iam.gserviceaccount.com
# Fetch the service account key JSON file contents
cred = credentials.Certificate('courseschedule-8a816-firebase-adminsdk-jgy6n-2f35d9eaad.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://courseschedule-8a816.firebaseio.com/'
})


def main():

    with open("soup.html") as f:
      soup = bs.BeautifulSoup(f,'lxml')

    #ref = db.reference('courses')
    #print(ref.get())
    #print(type(ref.get()))

    print(saveCourse('ASL  610D',soup))


#gets data about course and saves it
def saveUnique(unique,soup):

    course_a = soup.find(text=unique).parent
    course_tr = course_a.parent.parent

    days = course_tr.find('td',{'data-th':'Days'}).select_one('span').text
    hour = course_tr.find('td',{'data-th':'Hour'}).select_one('span').text
    room = course_tr.find('td',{'data-th':'Room'}).select_one('span').text
    instructor = course_tr.find('td',{'data-th':'Instructor'}).text
    status = course_tr.find('td',{'data-th':'Status'}).text


    db.reference().child('courses').child(unique).update({
        'unique':unique,
        'days':days,
        'hour':hour,
        'room':room,
        'instructor':instructor,
        'status':status,
    })
    return(status)

def saveCourse(courseId,soup):
    course_a = soup.find('td',{'class':'course_header'}) #dont need


    b = soup.find_all('a',{'title':'Unique number'})
    for uniqueNum in b:
        print(uniqueNum.text)
        unique = uniqueNum.text
        course_a = soup.find(text=unique).parent
        course_tr = course_a.parent.parent

        days = course_tr.find('td',{'data-th':'Days'}).select_one('span').text
        hour = course_tr.find('td',{'data-th':'Hour'}).select_one('span').text
        room = course_tr.find('td',{'data-th':'Room'}).select_one('span').text
        instructor = course_tr.find('td',{'data-th':'Instructor'}).text
        status = course_tr.find('td',{'data-th':'Status'}).text

        db.reference().child('courses').child(courseId).child(unique).update({
            'unique':unique,
            'days':days,
            'hour':hour,
            'room':room,
            'instructor':instructor,
            'status':status,
        })


def saveProf(prof,courseId):
    b = soup.find_all('a',{'title':'Unique number'})
    for uniqueNum in b:
        print(uniqueNum.text)
        unique = uniqueNum.text
        course_a = soup.find(text=unique).parent
        course_tr = course_a.parent.parent

        days = course_tr.find('td',{'data-th':'Days'}).select_one('span').text
        hour = course_tr.find('td',{'data-th':'Hour'}).select_one('span').text
        room = course_tr.find('td',{'data-th':'Room'}).select_one('span').text
        instructor = course_tr.find('td',{'data-th':'Instructor'}).text
        status = course_tr.find('td',{'data-th':'Status'}).text

        db.reference().child('courses').child(prof).child(unique).update({
            'unique':unique,
            'days':days,
            'hour':hour,
            'room':room,
            'instructor':instructor,
            'status':status,
        })


def findHeaders():
    headers = []
    for header in soup.find_all('td',{'class':'course_header'}):
        headers.append(header)
    return headers


main()
