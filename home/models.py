from django.db import models
from django.contrib.auth.models import User
from .helpers import *

from django.urls import reverse
from datetime import date,datetime
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=1000,unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse("article-detail", args=(str(self.id)))
        return reverse("home")
    
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Category, self).save(*args, **kwargs)

class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='blog/profile/',null=True, blank=True)
    facebook_url = models.CharField(max_length=255,null=True,blank=True)
    instagram_url = models.CharField(max_length=255,null=True,blank=True)
    twitter_url = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        # return reverse("article-detail", args=(str(self.id)))
        return reverse("show_profile_page", args=[str(self.pk)])



class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    title_tag = models.CharField(max_length=1000)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default='1')
    content = RichTextField(blank=True,null=True)
    # content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='blog',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=255,default='coding')
    snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse("article-detail", args=(str(self.id)))
        return reverse("home")


class Comment(models.Model):
    post = models.ForeignKey(BlogModel,related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)