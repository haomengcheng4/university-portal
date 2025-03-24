from rest_framework import serializers
from users.models import CustomUser
from students.models import Grade
from schedules.models import Schedule

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']

class AssignedGradeSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.username', read_only=True)
    subject_name = serializers.CharField(source='subject.name', read_only=True)

    class Meta:
        model = Grade
        fields = ['id', 'student', 'student_name', 'subject', 'subject_name', 'grade', 'date_assigned']

class TeacherScheduleSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField(source='group.name', read_only=True)
    subject_name = serializers.CharField(source='subject.name', read_only=True)
    classroom_name = serializers.CharField(source='classroom.name', read_only=True)

    class Meta:
        model = Schedule
        fields = ['id', 'group', 'group_name', 'subject', 'subject_name', 'classroom', 'classroom_name', 'day_of_week', 'start_time', 'end_time']
