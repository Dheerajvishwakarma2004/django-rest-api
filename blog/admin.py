from django.contrib import admin
from .models import CustomUser, Post
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Post)
