from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    bio = models.CharField(max_length=20,blank=True,null=True)
    


class Post(models.Model):
    title = models.CharField()
    content = models.TextField()
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    
