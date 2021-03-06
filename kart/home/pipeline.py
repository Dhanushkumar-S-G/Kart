from social_core.pipeline.partial import partial
from django.shortcuts import redirect, render
from .models import Student
import datetime
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .tasks import new_account

department = {
    'ae': 'Aeronautical Engineering',
    'au': 'Automobile Engineering',
    'bt': 'Biotechnology',
    'ce': 'Civil Engineering',
    'cs': 'ComputerScience Engineering',
    'ee': 'Electrical and Electronics Engineering',
    'ec': 'Electronics and Communication Engineering',
    'ei': 'Electronics and Instrumentation Engineering',
    'ft': 'Fashion Technology',
    'is': 'Information Science and Engineering',
    'it': 'Information Technology',
    'me': 'Mechanical Engineering',
    'mc': 'Mechatronics Engineering',
    'tt': 'Textile Technology'
}


@partial
def create_user(backend, response, *args, **kwargs):
    request = kwargs.get('request')
    roll_no = response['family_name']
    name = response['given_name']
    email = response['upn']
    dept = email[-12:-10]
    dept = dept
    try:
        last_login = datetime.datetime.now()
        user = Student.objects.get(roll_no=roll_no)
        user.last_login = last_login
        user.save()
        request.session['roll_no'] = user.roll_no
        return
    except Student.DoesNotExist:
        if request.method == "POST":
            linkedin = request.POST.get('linkedin')
            last_login = datetime.datetime.now()
            user = Student.objects.create(roll_no=roll_no, name=name, mail=email, dept=department[dept], linkedin=linkedin,
                                          last_login=last_login)
            new_account.delay(email)
            request.session['roll_no'] = user.roll_no
            return

        else:
            return render(request, 'home/signup.html', {'roll_no': roll_no, 'name': name, 'email': email, 'dept': dept})
