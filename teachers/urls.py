from django.urls import path
from .views import view_grades, update_grade
from .views import create_announcement, view_announcements

urlpatterns = [
    path('view-grades/', view_grades, name='view_grades'),
    path('update-grade/<int:grade_id>/', update_grade, name='update_grade'),
    path('create-announcement/', create_announcement, name='create_announcement'),
    path('view-announcements/', view_announcements, name='view_announcements'),
]
