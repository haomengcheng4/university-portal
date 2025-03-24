from django.urls import path
from .views import TeacherListView, TeacherDetailView, TeacherGradesView, TeacherScheduleView

urlpatterns = [
    path('', TeacherListView.as_view(), name='teacher-list'),
    path('<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
    path('<int:teacher_id>/grades/', TeacherGradesView.as_view(), name='teacher-grades'),
    path('<int:teacher_id>/schedule/', TeacherScheduleView.as_view(), name='teacher-schedule'),
]
