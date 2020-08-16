import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


#Edit this function to change the format of the email subject
def create_subject(start_date = "12th-May-2020" , end_date="31st-July-2021" , extras = "") : #Use extras to specify report id , username etc
    subject = "Report insights from "  + start_date + " to " + end_date + "  - " + extras #Change here to edit subject
    return subject


def report_mailer(emailfrom , emailto , filesToSend , username , password) :
    #Function Parameters 
    #emailfrom : abcd@gmail.com
    #emailto : pqrs@gmail.com
    #filesToSend : ["Names.csv" , "abcd.png" ]
    #Username : abcd@gmail.com
    #password : password

    msg = MIMEMultipart()
    msg["From"] = emailfrom
    msg["To"] = emailto

    for fileToSend in filesToSend : 
        ctype, encoding = mimetypes.guess_type(fileToSend)
        if ctype is None or encoding is not None:
            ctype = "application/octet-stream"

        maintype, subtype = ctype.split("/", 1)
        if maintype == "text":
            fp = open(fileToSend)
            # Note: we should handle calculating the charset
            attachment = MIMEText(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == "image":
            fp = open(fileToSend, "rb")
            attachment = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == "audio":
            fp = open(fileToSend, "rb")
            attachment = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
        else:
            fp = open(fileToSend, "rb")
            attachment = MIMEBase(maintype, subtype)
            attachment.set_payload(fp.read())
            fp.close()
            encoders.encode_base64(attachment)
        attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
        msg.attach(attachment)

        server = smtplib.SMTP("smtp.gmail.com:587")
        server.starttls()
        server.login(username,password)
        server.sendmail(emailfrom, emailto, msg.as_string())
        server.quit()