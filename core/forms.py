from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Post
User = get_user_model()


class SignupForm(UserCreationForm):
    class Meta :
        model = User
        fields = ('username','email')
        
        

class PostCreateForm(forms.ModelForm):
    class Meta :
        models = Post
        fields = ['title','content']