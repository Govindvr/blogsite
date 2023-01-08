from django.db import models
from django.contrib.auth.models import User

class Userdetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'