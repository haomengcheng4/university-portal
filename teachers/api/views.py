from rest_framework import generics
from users.models import CustomUser
from students.models import Grade
from schedules.models import Schedule
from .serializers import TeacherSerializer, AssignedGradeSerializer, TeacherScheduleSerializer

class TeacherListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(role='teacher')
    serializer_class = TeacherSerializer

class TeacherDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.filter(role='teacher')
    serializer_class = TeacherSerializer

class TeacherGradesView(generics.ListAPIView):
    serializer_class = AssignedGradeSerializer

    def get_queryset(self):
        teacher_id = self.kwargs['teacher_id']
        return Grade.objects.filter(teacher_id=teacher_id)

class TeacherScheduleView(generics.ListAPIView):
    serializer_class = TeacherScheduleSerializer

    def get_queryset(self):
        teacher_id = self.kwargs['teacher_id']
        return Schedule.objects.filter(teacher_id=teacher_id)
