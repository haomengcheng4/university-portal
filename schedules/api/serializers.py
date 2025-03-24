from rest_framework import serializers
from schedules.models import Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField(source='group.name', read_only=True)
    subject_name = serializers.CharField(source='subject.name', read_only=True)
    teacher_name = serializers.CharField(source='teacher.username', read_only=True)
    classroom_name = serializers.CharField(source='classroom.name', read_only=True)

    class Meta:
        model = Schedule
        fields = ['id', 'group', 'group_name', 'subject', 'subject_name', 'teacher', 'teacher_name', 'classroom', 'classroom_name', 'day_of_week', 'start_time', 'end_time']
