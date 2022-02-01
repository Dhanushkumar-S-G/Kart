from django.db import models
from home.models import Student


# Create your models here.
class Book(models.Model):
    roll_no = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Title", max_length=50)
    picture = models.ImageField(verbose_name="Photo", upload_to="book")
    desc = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.title + " " + str(self.roll_no)