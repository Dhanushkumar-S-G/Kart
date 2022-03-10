from django.shortcuts import render, redirect
from django.contrib.auth import logout
from home.models import Student
from .models import Book, Request
import datetime
from django.core import serializers
from django.contrib import messages
from .tasks import sorry_mail


# Create your views here.
def dashboard(request):
    if request.session.get('roll_no'):
        roll_no = request.session['roll_no']
        student = Student.objects.get(roll_no=roll_no)
        books = Book.objects.raw(
            "select * from dashboard_book where roll_no_id  = '" + roll_no + "'")
        if request.method == 'POST':
            if 'hide' in request.POST:
                book_id = request.POST.get('hide')
                book = Book.objects.get(id=book_id)
                book.date_posted = datetime.datetime.now()
                book.to_lend = False
                book.save()

            if 'lend' in request.POST:
                book_id = request.POST.get('lend')
                book = Book.objects.get(id=book_id)
                book.to_lend = True
                book.date_posted = datetime.datetime.now()
                book.save()
        return render(request, 'dashboard/dashboard.html', {'student': student, 'books': books})
    else:
        return redirect('/')


def log_out(request):
    logout(request)
    return redirect('/')


def profile(request):
    if request.session.get('roll_no'):
        student = Student.objects.get(roll_no=request.session['roll_no'])
        if request.method == 'POST':
            student.photo = request.FILES.get('photo')
            student.phone = request.POST.get('phone')
            student.twitter = request.POST.get('twitter')
            student.facebook = request.POST.get('facebook')
            student.instagram = request.POST.get('instagram')
            student.about = request.POST.get('about')
            student.save()
            redirect('/me/profile')

        return render(request, 'dashboard/profile.html', {'student': student})
    else:
        return redirect('/')


def explore(request):
    if request.session.get('roll_no'):
        student = Student.objects.get(roll_no=request.session['roll_no'])
        if request.method == "POST" and 'req' in request.POST:
            book_id = request.POST.get('req')
            book = Book.objects.get(id = book_id)
            c = Request.objects.filter(book = book,student =  student, status = 'not given')
            if len(c) >=1:
                messages.error(request,"You have already requested this book")
            else:
                book = Book.objects.get(id = book_id)
                d = datetime.datetime.now()
                req_b = Request.objects.create(book=book, student=student, date_requested=d)
                req_b.save()
        books = Book.objects.raw(
            "select * from dashboard_book where to_lend = True and is_verified = True order by date_posted desc;")
        books_json = serializers.serialize("json",books)
        return render(request, 'dashboard/explore.html', {'student': student, 'books': books, 'books_json':books_json})
    else:
        redirect('/')


def lend(request):
    if request.session.get('roll_no'):
        student = Student.objects.get(roll_no=request.session['roll_no'])
        if request.method == "POST":
            title = request.POST.get('title')
            desc = request.POST.get('description')
            picture = request.FILES.get('picture')
            book = Book(roll_no=student, title=title, desc=desc, picture=picture)
            book.author = request.POST.get('author')
            book.pub_year = request.POST.get('year')
            book.book_edition = request.POST.get('edition')
            book.dept = request.POST.get('department')
            book.sem = request.POST.get('semester')
            book.save()
            return redirect('/me')

        return render(request, 'dashboard/lend.html', {'student': student})
    else:
        redirect('/')


def view_profile(request, roll=None):
    if request.session.get('roll_no') and roll:
        student = Student.objects.get(roll_no=request.session['roll_no'])
        try:
            stu = Student.objects.get(roll_no=roll)
            return render(request, 'dashboard/view_profile.html', {'student': student, 'stu': stu})
        except Student.DoesNotExist:
            return redirect('/')

    else:
        return redirect('/')


def share_request(request):
    if request.session.get('roll_no'):
        student = Student.objects.get(roll_no=request.session['roll_no'])
        if student.is_staff:
            if request.method == 'POST' and 'verify' in request.POST:
                book_id = request.POST.get('verify')
                book = Book.objects.get(id = book_id)
                book.is_verified = True
                book.date_verified = datetime.datetime.now()
                book.save()
            books = Book.objects.filter(is_verified = False)
            return render(request,'dashboard/share_r.html',{'student':student,'books':books})
    else:
        redirect('/')
    return 

def books_requested(request):
    if request.session.get('roll_no'):
        student = Student.objects.get(roll_no=request.session['roll_no'])
        if student.is_staff:
            if request.method == 'POST' and 'conform' in request.POST:
                req_id = request.POST.get('conform')
                req = Request.objects.get(id = req_id)
                book = Book.objects.get(id = req.book.id)
                book.to_lend = False
                book.save()
                req.status = 'conformed'
                req.save()

            if request.method == 'POST' and 'give' in request.POST:
                req_id = request.POST.get('give')
                req = Request.objects.get(id = req_id)
                req.date_given = datetime.datetime.now()
                req.status = 'given'
                sorry_mail.delay(req_id)
                req.save()
            reqs = Request.objects.exclude(status = 'given').exclude(status = 'given to someone else')
            return render(request,'dashboard/book_r.html',{'student':student,'reqs':reqs})
    else:
        redirect('/')
    return 



def error404(request, exception):
    return render(request, 'dashboard/404.html')
