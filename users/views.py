from django.shortcuts import render
from django.contrib import admin
from .models import CustomUser

# Create your views here.

admin.site.register(CustomUser)
