from django.contrib import admin
from rest_framework import fields
from .models import Users
# Register your models here.
@admin.register(Users)
class UsersModelAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','password']