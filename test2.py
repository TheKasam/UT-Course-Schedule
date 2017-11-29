import re
import mechanicalsoup
import bs4 as bs

#regular query: course_tr.find('td',{'data-th':'Days'})
#text gives you string
#contents gives you list
#select_one
#find text     course_a = soup.find(text=unique).parent
#getting class value - b.get('class')

def main():

    with open("soup.html") as f:
      soup = bs.BeautifulSoup(f,'lxml')


    u = soup.find(text="40350").parent

    print(findUnique('40350',soup))



def findUnique(unique,soup):

    course_a = soup.find(text=unique).parent
    course_tr = course_a.parent.parent

    days = course_tr.find('td',{'data-th':'Days'}).select_one('span').text
    hour = course_tr.find('td',{'data-th':'Hour'}).select_one('span').text
    room = course_tr.find('td',{'data-th':'Room'}).select_one('span').text
    instructor = course_tr.find('td',{'data-th':'Instructor'}).text
    status = course_tr.find('td',{'data-th':'Status'}).text
    return(status)

    db.reference().child('courses').child('unique').child('1').update({
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
