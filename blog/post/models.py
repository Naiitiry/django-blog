from django.db import models

from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Category(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=100,null=False,blank=False)
    description=models.TextField(null=False,blank=False)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='posts')
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    comment=models.TextField(null=False,blank=False)
    comment_date=models.DateField(default=date.today)


    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')

    def __str__(self):
        return self.comment

class Tag(models.Model):
    name=models.CharField(max_length=20,null=False,blank=False)

    post=models.ManyToManyField(Post)