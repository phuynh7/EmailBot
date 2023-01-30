import smtplib
import ssl
from email.message import EmailMessage

email_sender = 'peterhuynh7@outlook.com'
email_password = 'lcyzdqbovtnqigse'
email_receiver = 'peterhuynh214@gmail.com'

subject = 'Hey You won something!'
body = """
You won a prize congratz! Also I wish you happiness and wealth. I know you want that special person to be with you right now but remember she was ok with letting 
you out of her life. It not your job to check up on her. Remember you are not your thoughts just like how you drive your car, it does not make you your car. Thank you for reading <3
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as  smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

