from django.db import models
from users.models import CustomUser

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="teacher_profile")
    specialization = models.CharField(max_length=100)
    assigned_classes = models.ManyToManyField('schedules.Class', related_name="assigned_teachers")

    def __str__(self):
        return self.user.username
    
class Announcement(models.Model):
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'})
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    for_group = models.CharField(max_length=50, blank=True, null=True)  # Can be a specific group or all students

    def __str__(self):
        return f"{self.title} by {self.teacher.username}"