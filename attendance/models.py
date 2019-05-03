from django.db import models
import uuid

class Department(models.Model):
    dept_code = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return '(%s) %s'%(self.dept_code, self.name)


class Course(models.Model):
    course_code = models.CharField(max_length=50, primary_key=True)
    department = models.ForeignKey(Department, on_delete=True)
    course_name = models.CharField(max_length=150)

    def __str__(self):
        return '(%s) %s'%(self.course_code, self.course_name)


class Student(models.Model):
    adm_no = models.CharField(max_length=50, primary_key=True)
    full_name = models.CharField(max_length=200)
    course_code = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return '(%s) %s'%(self.adm_no, self.full_name)


class Lecturer(models.Model):
    staff_no = models.CharField(max_length=50, primary_key=True)
    full_name = models.CharField(max_length=200)

    def __str__(self):
        return '(%s) %s'%(self.staff_no, self.full_name)


class Unit(models.Model):
    unit_code = models.CharField(max_length=50, primary_key=True)
    course_code = models.ForeignKey(Course, on_delete=models.CASCADE)
    unit_name = models.CharField(max_length=200)

    def __str__(self):
        return '(%s) %s'%(self.unit_code, self.unit_name)


class UnitDetail(models.Model):
    unit_code = models.ForeignKey(Unit, on_delete=models.CASCADE)
    semester = models.CharField(max_length=20)
    year = models.DateField()


class RegisteredUnit(models.Model):
    unit_code = models.ForeignKey(Unit, on_delete=models.CASCADE)
    adm_no = models.ForeignKey(Student, on_delete=models.CASCADE)


class UnitAssign(models.Model):
    unit_code = models.ForeignKey(Unit, on_delete=models.CASCADE)
    staff_no = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    course_code = models.ForeignKey(Course, on_delete=models.CASCADE)


class LecturerSession(models.Model):
    session_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    staff_no = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    unit_code = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return '(%s) %s %s'%(self.session_id, self.staff_no, unit_code)


class AttendanceList(models.Model):
    adm_no = models.ForeignKey(Student, on_delete=models.CASCADE)
    unit_code = models.ForeignKey(Unit, on_delete=models.CASCADE)
    staff_no = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    session = models.ForeignKey(LecturerSession, on_delete=models.CASCADE)
    course_code = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)



# class CourseUnit(models.Model):
#     course_code = models.ForeignKey('Course', on_delete=models.CASCADE)
#     unit_code = models.ForeignKey('Unit', on_delete=models.CASCADE)

