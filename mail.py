import smtplib
import imghdr
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
from datetime import datetime
import json



def send_email(company_names):


    login = "chhetrirobot@gmail.com" # paste your login 

    sender_email = login 
    receiver_email = company_names['email']
    message = MIMEMultipart("alternative") 
    message["Subject"] = f"Share Applied | {company_names['company']} | {company_names['type']}" 
    message["From"] = login 
    message["To"] = receiver_email
    if company_names['error']:
        error='' 



    html =f"""\
    <html>
    <body>
            <p>CompanyName: {company_names['company']}</p>
            <p>ShareType: {company_names['type']}</p>
            <p>Type: {company_names['share_type']}</p>
            <p>Applied Time: {company_names['applied_time']}</p>

            Thanks,<br>
            Mero share Automation
        </body>
    </html>
    """
    part2 = MIMEText(html, "html") 
    message.attach(part2)





    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('chhetrirobot@gmail.com',"")
    server.send_message(message)
    server.quit()
    print('Sent')

    print(company_names['company'])

