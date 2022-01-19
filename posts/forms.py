"""Post forms"""
#Django
from django import forms 
# Models
from posts.models import Post

class PostForm(forms.ModelForm):
    """Post Model Form"""

    class Meta:
        """Forrm settings"""
        model = Post
        fields = ('user', 'profile', 'title', 'photo')
