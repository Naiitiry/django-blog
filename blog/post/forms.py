from django.forms import ModelForm
from .models import Post, Comment, Category, Tag

class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=['title','description','category','tag']

class CommentForm(ModelForm):
    class Meta:
        model=Comment
        exclude=('comment_date',)

class Tag(ModelForm):
    model=Tag
    fields=['name']

    def clean_name(self):
        name=self.cleaned_data.get('name')
        return name.capitalize()