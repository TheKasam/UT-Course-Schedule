#test email service
import smtplib
import time

def main():
    start = time.time()
    service = smtplib.SMTP('smtp.gmail.com', 587)
    service.starttls()
    service.login("support@utcourseupdates.com", "updatescourseut")
    service.sendmail("support@utcourseupdates.com", "saikasam98@gmail.com", "hello my love is gone")
    service.quit()
    print(time.time() - start)
main()
