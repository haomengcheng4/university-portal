from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from users.models import CustomUser
from students.models import Grade
from subjects.models import Subject

class StudentGradeViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.student = CustomUser.objects.create_user(username="student1", password="password", role="student")
        self.teacher = CustomUser.objects.create_user(username="teacher1", password="password", role="teacher")
        self.subject = Subject.objects.create(name="Mathematics")
        self.grade = Grade.objects.create(student=self.student, subject=self.subject, grade="B", teacher=self.teacher)

    def test_student_can_view_own_grades(self):
        self.client.login(username="student1", password="password")
        response = self.client.get(reverse('student-grades'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['grade'], 'B')
