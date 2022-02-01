from django.shortcuts import render, redirect
from django.contrib.auth import logout
from home.models import Student
from .models import Book


# Create your views here.
def dashboard(request):
    if request.session.get('roll_no'):
        student = Student.objects.get(roll_no=request.session['roll_no'])
        return render(request, 'dashboard/layout.html', {'student': student})
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
        books = Book.objects.all()
        return render(request, 'dashboard/explore.html', {'student': student, 'books': books})
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

def error404(request, exception):
    return render(request, 'dashboard/404.html')
