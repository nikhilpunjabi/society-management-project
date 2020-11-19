import smtplib
from email.mime.text import MIMEText

class Network:
    def __init__(self,str):
        text="""Dear Resident, 
                kindly pay your society maintenance amount within 2-3  working days
                otherwise after that penalty will be charged"""

        msg=MIMEText(text)
        msg['From']="2017.avinash.bhawnani@ves.ac.in"
        msg['To']=str
        msg['Subject']="REMINDER !!"

        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('2017.avinash.bhawnani@ves.ac.in','AVInash@03')

        server.send_message(msg)
        server.quit()


#n=Network('2017.avinash.bhawnani@ves.ac.in')

