from turtle import Turtle
from django.db import models
from home.models import Student


# Create your models here.
class Book(models.Model):
    roll_no = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Title", max_length=50)
    picture = models.ImageField(verbose_name="Photo", upload_to="book")
    desc = models.TextField(verbose_name="Description")
    author = models.TextField(verbose_name="Author", null=True)
    pub_year = models.IntegerField(verbose_name="Year published", null=True)
    book_edition = models.IntegerField(verbose_name="Book_edition", null=True)
    dept = models.TextField(verbose_name="Department ", null=True)
    sem = models.IntegerField(verbose_name="Semester", null=True)
    date_posted = models.DateField(
        verbose_name="Date Posted", auto_now_add="True", null=True)
    to_lend = models.BooleanField(verbose_name="To lend", default=True)
    is_verified = models.BooleanField(
        verbose_name="Is verified", default=False)
    date_verified = models.DateTimeField(verbose_name = "Date verified",null=True,blank=True)

    def __str__(self):
        return self.title + " " + str(self.roll_no)


class Request(models.Model):
    s_choices = [
        ('given','given'),
        ('not given','not given'),
        ('given to someone else','given to someone else'),
        ('conformed','conformed')
    ]
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_requested = models.DateTimeField(verbose_name='Date requested',auto_now_add=True)
    status = models.CharField(verbose_name="Status",max_length=25,default = 'not given',choices=s_choices,null=True)
    date_given = models.DateTimeField(verbose_name="Date Given/Rejected", null=True, blank=True)