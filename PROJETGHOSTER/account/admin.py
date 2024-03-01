from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User_app

admin.site.register(User_app,UserAdmin)
# Register your models here.
