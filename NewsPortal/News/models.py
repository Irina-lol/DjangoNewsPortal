from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Sum


class Author (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        postR = self.post_set.all().aggregate(postRating=Sum ('rating'))
        p_R = 0
        p_R += postR.get('postRating')

        commentR = self.user.comment_set.all().aggregate(commentRating=Sum ('rating'))
        c_R = 0
        c_R += commentR.get('commentRating')

        self.rating = p_R * 3 + c_R
        self.save()

    def __str__(self):
        return f"{self.user}"

class Category (models.Model):
    name = models.CharField (max_length=30, unique=True)

    def __str__(self):
        return f"{self.name}"


class Post (models.Model):
    news = "NV"
    articles = "AR"

    POST_TYPES = [
        (news, 'Новость'),
        (articles, 'Статья')
    ]
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=2, choices=POST_TYPES, default=news)
    date_in = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through="PostCategory")
    title = models.CharField(max_length=90)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:124] + '...'

    def __str__(self):
        dataf = 'Post from {}'.format(self.date_in.strftime('%d.%m.%Y.'))
        return f"{self.title},{self.text},{dataf}"

    def get_absolute_url(self):
        return reverse('newss', args=[str(self.id)])


class PostCategory (models.Model):
    post = models.ForeignKey (Post, on_delete=models.CASCADE)
    category = models.ForeignKey (Category, on_delete=models.CASCADE)


class Comment (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_in = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return f"{self.date_in}, {self.user}"
