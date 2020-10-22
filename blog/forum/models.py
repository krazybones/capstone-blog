from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.


class Category(models.Model):
    # define what we want in our blog
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

# hard code option
# options = [('Neutral', 'Neutral'), ('Coding Hacks', 'Coding Hacks'), ('Lifestyle Hacks', 'Lifestyle Hacks'), ('Entertainment', 'Entertainment'),
#            ('Sports', 'Sports'), ('Finance', 'Finance'), ('Cooking', 'Cooking'), ('Current Events', 'Current Events'), ]


# dynamic option
options = Category.objects.all().values_list('name', 'name')

option_list = []

for item in options:
    option_list.append(item)


class Post(models.Model):
    # define what we want in our blog
    title = models.CharField(max_length=250)
    title_tag = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length=250, default='Neutral', choices=option_list)

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        # return reverse('post-detail', args=(str(self.id)))
        return reverse('home')
