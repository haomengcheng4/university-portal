from django.contrib import admin
from .models import Class, Classroom, Subject, Group, Schedule

admin.site.register(Class)
admin.site.register(Classroom)
admin.site.register(Subject)
admin.site.register(Group)
admin.site.register(Schedule)