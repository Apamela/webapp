from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
    # Creating message subject and sender
    subject = 'Welcome to the NewsLetter'
    sender = 'pamelab.desire@gmail.com@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/wbsiteemail.txt',{"name": name})
    html_content = render_to_string('email/websiteemail.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()