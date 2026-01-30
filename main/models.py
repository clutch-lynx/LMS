from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username

class Subject(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Grade(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return f"{self.student.username} - {self.subject.title}: {self.value}"
    

class Lesson(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'teacher'}
    )
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
