from email.message import EmailMessage
import ssl
import smtplib
# import name

with open("thename.txt") as fp:
    l=fp.read()

receiver=l.split('\n')
sender = "nktarantino04@gmail.com"
password = "shyfhktihncbzzvr"
# receiver=name.names

print(l[1])

subject = "check mail"
message = """
check out the lastest video on Youtube:https://youtube.com/shorts/ufuZpLieeYE?feature=share
"""

getred = EmailMessage()
getred['From'] = sender
getred['To'] = receiver
getred['Subject'] = subject
getred.set_content(message)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender, password)
    for i in range(len(receiver)):
        smtp.sendmail(sender, receiver[i], getred.as_string())


print("executed")