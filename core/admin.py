from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Post
# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Qo'shimcha ma'lumot",{"fields":("bio",)}),
    )
    
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author']
    