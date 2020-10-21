from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    # define what we want in our blog
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + '|' + str(self.author)
