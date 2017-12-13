import pickle
import re
import mechanicalsoup
import sys



with open("browser.pickle","rb") as f:
    browser = pickle.load(f)


varInput = sys.argv[1].strip()
varType = varInput[-1]

if  varType == 'u':
    link = "https://utdirect.utexas.edu/apps/registrar/course_schedule/20182/" + varInput[:-1]  + "/"
elif varType == 'c':
    feild = varInput[:-1].split()[0]
    number = varInput[:-1].split()[1]
    link = "https://utdirect.utexas.edu/apps/registrar/course_schedule/20182/results/?ccyys=20182&search_type_main=COURSE&fos_cn=" + feild+ "&course_number="+number
elif varType =='p':
    lName = varInput[:-1].split()[0]
    fName = varInput[:-1].split()[1]
    link = "https://utdirect.utexas.edu/apps/registrar/course_schedule/20182/results/?ccyys=20182&search_type_main=INSTR&instr_last_name=" + lName + "&instr_first_initial=" + fName
browser.open(link)
soup = browser.get_current_page()
title = soup.title.text

ans = '0'

if title == 'Page not found':
    pass

elif soup.find('div',{'class':'error'}) != None:
    pass
elif title == 'Session Timeout' or title == 'UT EID Login':
    pass

else:
    ans = '1'
dataToSendBack = ans
print(dataToSendBack)
sys.stdout.flush()
