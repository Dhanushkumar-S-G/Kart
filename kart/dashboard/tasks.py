from celery import shared_task
from django.shortcuts import redirect
from .models import Request
import datetime
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


@shared_task(bind=True)
def sorry_mail(self, req_id):
    req = Request.objects.get(id=req_id)
    book = req.book
    reqs = Request.objects.filter(book=book, status='not given')
    for req in reqs:
        req.status = 'given to someone else'
        req.date_given = datetime.datetime.now() 
        template = render_to_string('dashboard/sorry.html')
        e_mail = EmailMessage(
            'Sorry Some one booked the already',  # subject
            template,  # body
            'dhanushkumarganapathy@outlook.com',  # host_email,
            [req.student.mail],  # receiver
        )
        e_mail.fail_silently = True
        e_mail.send()
        req.save()
        redirect('/me/books-requested')

    return "Mail sent successfully"
