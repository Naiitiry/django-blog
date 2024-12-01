from django.forms import ModelForm
from .models import Post, Comment, Category, Tag

class PostForm(ModelForm):
    class Meta:
        model=Post
        exclude=('created_at','updated_at',)

class CommentForm(ModelForm):
    class Meta:
        model=Comment
        exclude=('comment_date',)

