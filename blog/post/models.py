from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Category(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=20,null=False,blank=False,unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=100,null=False,blank=False)
    description=models.TextField(null=False,blank=False)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='posts')
    tag=models.ForeignKey(Tag,on_delete=models.CASCADE,related_name='posts',null=True)

    # Seguimiento de likes
    def numero_de_likes(self):
        return Like.objects.filter(post=self).count()

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='likes')
    
    class Mete:
        unique_together = ('user','post') # Evita duplicados

class Comment(models.Model):
    comment=models.TextField(null=False,blank=False)
    comment_date=models.DateField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')

    def __str__(self):
        return f'{self.user.username} - {self.comment[:30]} ({self.comment_date})'
