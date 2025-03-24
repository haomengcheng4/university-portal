from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Schedule

@login_required
def student_schedule(request):
    if request.user.role != 'student':
        return render(request, '403.html')  # Restrict access if not a student

    student_groups = request.user.group_set.all()  # Get student's groups
    schedules = Schedule.objects.filter(group__in=student_groups).order_by('day_of_week', 'start_time')

    return render(request, 'schedules/student_schedule.html', {'schedules': schedules})

@login_required
def teacher_schedule(request):
    if request.user.role != 'teacher':
        return render(request, '403.html')  # Restrict access if not a teacher

    schedules = Schedule.objects.filter(teacher=request.user).order_by('day_of_week', 'start_time')

    return render(request, 'schedules/teacher_schedule.html', {'schedules': schedules})
