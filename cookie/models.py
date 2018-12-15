from django.db import models


# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=30,unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=30)


class Contact(models.Model):
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=30)
    Mobile = models.IntegerField()
    Email = models.EmailField()
    Yourmessage = models.TextField()

