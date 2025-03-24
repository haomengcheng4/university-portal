from django.urls import path
from .views import ScheduleListView, ScheduleDetailView

urlpatterns = [
    path('', ScheduleListView.as_view(), name='schedule-list'),
    path('<int:pk>/', ScheduleDetailView.as_view(), name='schedule-detail'),
]
