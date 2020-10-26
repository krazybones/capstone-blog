from django import forms
from .models import Post, Category, Comment

# options = [('Neutral', 'Neutral'), ('Coding Hacks', 'Coding Hacks'), ('Lifestyle Hacks', 'Lifestyle Hacks'), ('Entertainment', 'Entertainment'),
#            ('Sports', 'Sports'), ('Finance', 'Finance'), ('Cooking', 'Cooking'), ('Current Events', 'Current Events'), ]

options = Category.objects.all().values_list('name', 'name')

option_list = []

for item in options:
    option_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author',
                  'category', 'body', 'header_image')

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
        'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'show', 'type': 'hidden', 'placeholder': 'Enter Username..'}),
        # video 17!!!!
        # 'author': forms.Select(attrs={'class': 'form-control'}),
        'category': forms.ChoiceField(choices=option_list),
        'body': forms.Textarea(attrs={'class': 'form-control'}),
    }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
        # 'author': forms.Select(attrs={'class': 'form-control'}),
        # 'category': forms.Select(choices=options, attrs={'class': 'form-control'}),
        'body': forms.Textarea(attrs={'class': 'form-control'}),
    }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'body': forms.Textarea(attrs={'class': 'form-control'}),
    }
