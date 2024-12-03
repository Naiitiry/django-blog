from django.forms import ModelForm
from .models import Post, Comment, Category, Tag

class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=['title','description','category']

class CommentForm(ModelForm):
    class Meta:
        model=Comment
        exclude=('comment_date',)

