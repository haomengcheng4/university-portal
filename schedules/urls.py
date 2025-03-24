from django.urls import path
from .views import student_schedule, teacher_schedule

urlpatterns = [
    path('student-schedule/', student_schedule, name='student_schedule'),
    path('teacher-schedule/', teacher_schedule, name='teacher_schedule'),
]
