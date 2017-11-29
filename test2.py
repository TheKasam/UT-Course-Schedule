
import requests


resp2 = requests.get("https://utdirect.utexas.edu/apps/registrar/course_schedule/20179/results/?ccyys=20179&fos_fl=ASE&level=L&search_type_main=FIELD&x=114&y=13")
print(resp2.text)
