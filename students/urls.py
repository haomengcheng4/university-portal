from django.urls import path
from .views import student_grades, request_certificate, certificate_success, request_retake, retake_success, apply_scholarship, scholarship_success

urlpatterns = [
    path('grades/', student_grades, name='student_grades'),
    path('request-certificate/', request_certificate, name='request_certificate'),
    path('certificate-success/', certificate_success, name='certificate_success'),
    path('request-retake/', request_retake, name='request_retake'),
    path('retake-success/', retake_success, name='retake_success'),
    path('apply-scholarship/', apply_scholarship, name='apply_scholarship'),
    path('scholarship-success/', scholarship_success, name='scholarship_success'),
    
]
