from django.contrib import admin
from .models import Subject, User,Faculty,Semester

# Register your models here.
admin.site.register(User)
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Faculty)