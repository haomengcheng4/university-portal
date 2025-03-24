from django import forms
from students.models import Grade
from .models import Announcement

class GradeUpdateForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['grade']

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'message', 'for_group']