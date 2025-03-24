from django.urls import path, include

urlpatterns = [
    path('users/', include('users.api.urls')),  # User-related API endpoints
    path('students/', include('students.api.urls')),  # Student-related API endpoints
    path('teachers/', include('teachers.api.urls')),  # Teacher-related API endpoints
    path('schedules/', include('schedules.api.urls')),  # Schedule-related API endpoints
]
