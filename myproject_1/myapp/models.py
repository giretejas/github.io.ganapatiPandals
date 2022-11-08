from django.db import models

# Create your models here.
class login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    role=models.CharField(max_length=20)

class logins(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    role=models.CharField(max_length=20)

class me(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.CharField(max_length=60)
    subject=models.CharField(max_length=70)
    message=models.CharField(max_length=30)


