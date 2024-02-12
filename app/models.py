from django.db import models

class sample(models.Model):
    name=models.CharField(max_length=50)
    phone_no=models.IntegerField(default="")
    alternative_phoneno=models.IntegerField(default="")
    address=models.CharField(max_length=100, default="")
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    litre = models.IntegerField(default="")

class tryit(models.Model):
    name = models.CharField(max_length=50)
    phone_no = models.IntegerField(default="")
    aadhar = models.IntegerField(default="")
    address = models.CharField(max_length=100, default="")

class doit(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField()


