from django.db import models
from django.contrib.auth.models import User
from students.models import CustomUser

# Create your models here.
class Teacher(models.Model):
    subject=models.CharField(max_length=100)
    year=models.IntegerField()
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Assignment(models.Model):
    studentname=models.CharField(max_length=100)
    pdf=models.FileField(upload_to="assignment/files")
    subject=models.CharField(max_length=100)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)


