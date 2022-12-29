from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.content

class Like(models.Model):
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    status = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default = timezone.now)