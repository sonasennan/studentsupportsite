from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Notes(models.Model):
    subject=models.CharField(max_length=200)
    pdf=models.FileField(upload_to="notes/files")
    year=models.IntegerField()
    type=models.CharField(max_length=100)

    def __str__(self):
        return self.subject

class Questionpapers(models.Model):
    subject=models.CharField(max_length=200)
    pdf=models.FileField(upload_to="questions/files")
    year=models.IntegerField()
    type=models.CharField(max_length=100)
    yearofexamination=models.IntegerField()

    def __str__(self):
        return self.subject

class CustomUser(AbstractUser):
    department=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)

    is_student=models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)




