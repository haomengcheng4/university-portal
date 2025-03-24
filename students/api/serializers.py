from rest_framework import serializers
from students.models import Grade
from users.models import CustomUser

class GradeSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.username', read_only=True)
    subject_name = serializers.CharField(source='subject.name', read_only=True)

    class Meta:
        model = Grade
        fields = ['id', 'student', 'student_name', 'subject', 'subject_name', 'grade', 'teacher', 'date_assigned']
