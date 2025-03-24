from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Grade
from .models import CertificateRequest
from .models import RetakeRequest
from .models import ScholarshipApplication
from .forms import ScholarshipApplicationForm

@login_required
def student_grades(request):
    if request.user.role != 'student':
        return render(request, '403.html')  # Redirect if not a student
    grades = Grade.objects.filter(student=request.user)
    return render(request, 'students/view_grades.html', {'grades': grades})

@login_required
def request_certificate(request):
    if request.method == 'POST':
        CertificateRequest.objects.create(student=request.user)
        return redirect('certificate_success')  # Redirect to success page

    return render(request, 'students/request_certificate.html')

@login_required
def certificate_success(request):
    return render(request, 'students/certificate_success.html')

@login_required
def request_retake(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        reason = request.POST.get('reason')

        RetakeRequest.objects.create(student=request.user, subject=subject, reason=reason)
        return redirect('retake_success')  # Redirect to success page

    return render(request, 'students/request_retake.html')

@login_required
def retake_success(request):
    return render(request, 'students/retake_success.html')

@login_required
def apply_scholarship(request):
    if request.method == 'POST':
        form = ScholarshipApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.student = request.user
            application.save()
            return redirect('scholarship_success')

    else:
        form = ScholarshipApplicationForm()

    return render(request, 'students/apply_scholarship.html', {'form': form})

@login_required
def scholarship_success(request):
    return render(request, 'students/scholarship_success.html')
