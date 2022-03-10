from celery import shared_task
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

@shared_task(bind=True)
def new_account(self,mail):
    template = render_to_string('home/email.html')
    e_mail = EmailMessage(
        'Thanks for creating an account in Kart.',  # subject
        template,  # body
        'dhanushkumarganapathy@outlook.com',  # host_email,
        [mail],  # receiver
    )
    e_mail.fail_silently = True
    e_mail.send()
    return "mail sent successfully"