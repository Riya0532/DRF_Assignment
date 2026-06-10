from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=10)
    branch = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    hod = models.CharField(max_length=100)

    def __str__(self):
        return self.teacher_name