from django.db import models
from news.resources import POSITIONS, sport

 class Author (models.Model):
     full_name = models.CharField (max_length = 255)
     number = models.IntegerField (default = 0)

 class Category (models.Model):
     title = models.CharField (max_length = 255)
     position = models.CharField (max_length = 2, choices = POSITIONS, default = sport)

 class Post (models.Model):
    name = models.CharField (max_length=255)
    time_in = models.DateTimeField (auto_now_add = True)
    time_out = models.DateTimeField (null = True)
    author = models.ForeignKey (Author, on_delete = models.CASCADE)
    category = models.ManyToManyField(Category, through = 'PostCategory')

 class PostCategory (models.Model):
     post = models.ForeignKey (Post, on_delete = models.CASCADE)
     category = models.ForeignKey (Category, on_delete = models.CASCADE)
     amount = models.IntegerField (default = 1)
 class Comment (models.Model):
     pass