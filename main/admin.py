from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CustomUser, Subject, Grade

admin.site.register(CustomUser)
admin.site.register(Subject)
admin.site.register(Grade)