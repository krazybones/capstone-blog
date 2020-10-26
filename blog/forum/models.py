from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


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


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=250, blank=True, null=True)
    facebook_url = models.CharField(max_length=250, blank=True, null=True)
    insta_url = models.CharField(max_length=250, blank=True, null=True)
    twitter_url = models.CharField(max_length=250, blank=True, null=True)
    linkedin_url = models.CharField(max_length=250, blank=True, null=True)

    # added for admin area
    def __str__(self):
        return str(self.user)

    # added for create profile redirect
    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    # define what we want in our blog
    title = models.CharField(max_length=250)
    header_image = models.ImageField(
        null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length=250, default='Neutral', choices=option_list)
    snippet = models.CharField(
        max_length=250, default='Click to read further..')
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    # added for the admin area
    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        # return reverse('post-detail', args=(str(self.id)))
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
