from django.contrib import admin
from .models import Student, Lecturer, Unit, UnitAssign, Course, LecturerSession, AttendanceList, UnitDetail, RegisteredUnit, Department
# Register your models here.

admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Unit)
admin.site.register(UnitAssign)
admin.site.register(Course)
admin.site.register(LecturerSession)
admin.site.register(AttendanceList)
admin.site.register(UnitDetail)
admin.site.register(RegisteredUnit)
admin.site.register(Department)
