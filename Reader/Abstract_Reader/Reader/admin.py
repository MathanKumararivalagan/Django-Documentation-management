from django.contrib import admin
from django.urls import path
from . import views
# Register your models here.

from .models import *
# Register your models here.
admin.site.register(Student)