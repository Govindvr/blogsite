from django.db import models

class Userdetails(models.Model):
    usernm=models.CharField(max_length=200,null=False,primary_key = True)
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    mail=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
