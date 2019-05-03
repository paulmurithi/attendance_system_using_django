from django.db import models


class Department(models.Model):
    dept_code = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200)


class Course(models.Model):
    course_code = models.CharField(max_length=50, primary_key=True)
    department = models.ForeignKey(Department, on_delete=True)
    course_name = models.CharField(max_length=150)


class Student(models.Model):
    adm_no = models.CharField(max_length=50, primary_key=True)
    full_name = models.CharField(max_length=200)
    course_code = models.ForeignKey(Course, on_delete=models.CASCADE)


class Lecturer(models.Model):
    staff_no = models.CharField(max_length=50, primary_key=True)
    full_name = models.CharField(max_length=200)