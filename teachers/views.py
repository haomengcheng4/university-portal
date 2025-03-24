from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from students.models import Grade
from .forms import GradeUpdateForm
from .models import Announcement
from .forms import AnnouncementForm


@login_required
def view_grades(request):
    if request.user.role != 'teacher':
        return redirect('home')  # Ensure only teachers access this

    grades = Grade.objects.filter(teacher=request.user)
    return render(request, 'teachers/view_grades.html', {'grades': grades})

@login_required
def update_grade(request, grade_id):
    grade = get_object_or_404(Grade, id=grade_id)

    if request.user != grade.teacher:
        return redirect('view_grades')  # Ensure only the assigned teacher can update

    if request.method == 'POST':
        form = GradeUpdateForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('view_grades')

    else:
        form = GradeUpdateForm(instance=grade)

    return render(request, 'teachers/update_grade.html', {'form': form})

@login_required
def create_announcement(request):
    if request.user.role != 'teacher':
        return redirect('home')  # Redirect non-teachers away

    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.teacher = request.user  # Assign the logged-in teacher
            announcement.save()
            return redirect('view_announcements')
    else:
        form = AnnouncementForm()

    return render(request, 'teachers/create_announcement.html', {'form': form})

@login_required
def view_announcements(request):
    announcements = Announcement.objects.all().order_by('-created_at')
    return render(request, 'teachers/view_announcements.html', {'announcements': announcements})
