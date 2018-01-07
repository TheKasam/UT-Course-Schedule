#test email service
import smtplib
import time

def main():
    start = time.time()
    service = smtplib.SMTP_SSL('smtp.gmail.com', 587)
    service.starttls()
    service.login("saikasam98@gmail.com", "BetterMan")
    service.sendmail("saikasam98@gmail.com", "aj280598@gmail.com", "hello my love is gone")
    service.quit()
    print(time.time() - start)
main()
