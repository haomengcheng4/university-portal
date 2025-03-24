from django.test import TestCase
from users.models import CustomUser
from students.models import Grade
from subjects.models import Subject

class GradeModelTest(TestCase):
    def setUp(self):
        self.teacher = CustomUser.objects.create(username="teacher1", role="teacher")
        self.student = CustomUser.objects.create(username="student1", role="student")
        self.subject = Subject.objects.create(name="Mathematics")
        self.grade = Grade.objects.create(student=self.student, subject=self.subject, grade="A", teacher=self.teacher)

    def test_grade_creation(self):
        self.assertEqual(str(self.grade), "student1 - Mathematics - A")
