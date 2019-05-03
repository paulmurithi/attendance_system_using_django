from django.shortcuts import render, redirect, reverse
from django.views import View
from . import forms
from django.http import HttpResponse, JsonResponse
from .models import Course, Lecturer, Unit, LecturerSession, AttendanceList, Student, UnitAssign, RegisteredUnit, Department
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, update_session_auth_hash
from .utils import render_to_pdf
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.response import Response
from . import serializers
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.conf import settings
from django.core.paginator import Paginator

# uuid session serializer imports
import json
import uuid
from uuid import UUID


class Index(View):
    form_class = forms.LoginForm
    template = "attendance/index.html"

    def get(self, request):
        if request.user.is_authenticated:
            username = request.user
            student = Student.objects.filter(adm_no=username).exists()
            lecturer = Lecturer.objects.filter(staff_no=username).exists()
            department = Department.objects.filter(dept_code=username).exists()
            if student:
                return redirect('attendance:studentindex')
            elif lecturer:
                return redirect('attendance:lecturerindex')
            elif department:
                return redirect('attendance:departmentindex')
            else:
                pass
        else:
            # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
            form = self.form_class(None)
            return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            student = Student.objects.filter(adm_no=username).exists()
            lecturer = Lecturer.objects.filter(adm_no=username).exists()
            department = Student.objects.filter(adm_no=username).exists()
            if student:
                return redirect('attendance:studentindex')
            elif lecturer:
                return redirect('attendance:lecturerindex')
            elif department:
                return redirect('attendance:departmentindex')
            else:
                pass


# change password views
class StudentChangePassword(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    template = 'attendance/student/changepassword.html'
    form_class = forms.ChangePasswordForm

    def test_func(self):
        user = self.request.user
        return Student.objects.filter(adm_no=user).exists()
        # if not lecturer:
        #     return redirect(settings.LOGIN_URL)

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = request.user
            user = User.objects.get(username=username)
            password = form.cleaned_data['password']
            user.set_password(password)
            update_session_auth_hash(request, request.user)
        return HttpResponseRedirect()


class LecturerChangePassword(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    template = 'attendance/lecturer/changepassword.html'
    form_class = forms.ChangePasswordForm

    def test_func(self):
        user = self.request.user
        return Student.objects.filter(adm_no=user).exists()
        # if not lecturer:
        #     return redirect(settings.LOGIN_URL)

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = request.user
            user = User.objects.get(username=username)
            password = form.cleaned_data['password']
            user.set_password(password)
            update_session_auth_hash(request, request.user)
        return HttpResponseRedirect()


class DepartmentChangePassword(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    template = 'attendance/department/changepassword.html'
    form_class = forms.ChangePasswordForm

    def test_func(self):
        user = self.request.user
        return Student.objects.filter(adm_no=user).exists()
        # if not lecturer:
        #     return redirect(settings.LOGIN_URL)

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = request.user
            user = User.objects.get(username=username)
            password = form.cleaned_data['password']
            user.set_password(password)
            update_session_auth_hash(request, request.user)
        return HttpResponseRedirect()

# ==================================================login views ==============================================
# class LecturerLogin(View):
#     template = 'attendance/lecturerlogin.html'
#     form_class = forms.LoginForm
#
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template, {'form': form})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             login(username, password)
#         return HttpResponseRedirect()
#
#
# class DepartmentLogin(View):
#     template = 'attendance/departmentlogin.html'
#     form_class = forms.LoginForm
#
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template, {'form': form})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             login(username, password)
#         return HttpResponseRedirect()
#
# # ==================================================logout views  ===============================================
#
#


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('attendance:index')
#
#
# class LecturerLogout(View):
#     def get(self, request):
#         logout(request)
#
#
# class DepartmentLogout(View):
#     def get(self, request):
#         logout(request)
#
# # ==================================================signup views==================================================
#
#
# class studentSignup(View):
#     template = 'attendance/studentregister.html'
#     form_class = forms.RegisterForm
#
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template, {'form': form})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             login(username, password)
#         return HttpResponseRedirect()
#
#
# class LecturerSignup(View):
#     template = 'attendance/lecturerregister.html'
#     form_class = forms.RegisterForm
#
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template, {'form': form})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             login(username, password)
#         return HttpResponseRedirect()


class SignUp(View):
    form_class = forms.signUpForm
    template = 'attendance/signup.html'


    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # check if the username is in the lec database
            username = form.cleaned_data['username']
            lecturer = Lecturer.objects.filter(staff_no=username).exists()
            student = Student.objects.filter(adm_no=username).exists()
            department = Department.objects.filter(dept_code=username).exists()
            if lecturer or student or department:
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']

                check_username = User.objects.filter(username=username).exists()
                if check_username:
                    context = {
                        'form': form,
                        'error': "You already have an account"
                    }
                    return render(request, self.template, context)
                else:
                    user = User.objects.create_user(username, email, password)
                    user.save()
                    return redirect('login')
            else:
                context = {
                    'form': form,
                    'error': "You cannot create an account.Please contact the admin for assistance."
                }
                return render(request, self.template, context)


# @login_required
# def lec_module(request):
#     user = request.user
#     lecturer = Lecturer.objects.filter(staff_no=user).exists()
#
#     if not lecturer:
#         return redirect('attendance:stud_module')
#
#     # lecturer instance
#     lecturer = Lecturer.objects.get(staff_no=user)
#     lecturer_units = UnitAssign.objects.filter(staff_no=lecturer)
#     if request.method == "POST":
#         form = forms.lec_session_Form(request.POST)
#         if form.is_valid():
#             staff_no = Lecturer.objects.get(staff_no=request.user)
#             session = form.save(commit=False)
#             session.staff_no = staff_no
#             session.date = timezone.now()
#             session.save()
#             session_id = session.session_id
#             return HttpResponseRedirect(reverse('session', args=(session_id,)))
#     else:
#         form = forms.lec_session_Form()
#     context = {
#         'form': form,
#         'lecturer_units': lecturer_units
#     }
#
#     return render(request, 'previoussessions.html', context)
#
#
# def start_seesion(request, unit_code):
#     staff_no = Lecturer.objects.get(staff_no=request.user)
#     session = form.save(commit=False)
#     session.staff_no = staff_no
#     session.date = timezone.now()
#     session.save()
#     session_id = session.session_id
#     return HttpResponseRedirect(reverse('session', args=(session_id,)))
#
#
# def session_details(request, session_id):
#     session_details = LecturerSession.objects.get(session_id=session_id)
#
#     if request.method == "POST":
#         form = forms.attendanceForm(request.POST)
#         if form.is_valid():
#             adm_no = form.cleaned_data['adm_no']
#             print(adm_no)
#             # model intances
#             adm_no = Student.objects.get(adm_no=adm_no)
#             staff_no = Lecturer.objects.get(staff_no=request.user)
#             unit_code = session_details.unit_code
#             course_code = Course.objects.get(course_code="COM")
#             attendanceList = AttendanceList(
#                 adm_no=adm_no,
#                 unit_code=unit_code,
#                 staff_no=staff_no,
#                 course_code=course_code,
#                 session_id=session_details
#             )
#             attendanceList.save()
#             context = {
#                 'saved': "Student has been signed in"
#             }
#             return HttpResponseRedirect(reverse('session', args=(session_id,)))
#     else:
#         form = forms.attendanceForm()
#     context = {
#         'session_details': session_details,
#         'form': form
#     }
#     return render(request, 'session_details.html', context)
#
#
# @login_required
# def stud_module(request):
#     user = request.user
#     student = Student.objects.filter(adm_no=user).exists()
#     if not student:
#         return redirect('attendance:lec_module')
#     return render(request, 'stud_module.html')
# ==================================================department views =============================================


# class DepartmentIndex(View):
#     # login_url = '/accounts/login/'
#     # redirect_field_name = 'redirect_to'
#     template = 'attendance/department/index.html'
#
#     def get(self, request):
#         all_course = Course.objects.all()
#         context = {
#             'all_course': all_course,
#         }
#         return render(request, self.template, context)


class DepartmentIndex(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    template = 'attendance/department/index.html'

    def test_func(self):
        user = self.request.user
        return Department.objects.filter(dept_code=user).exists()
        # if not lecturer:
        #     return redirect(settings.LOGIN_URL)

    def get(self, request):
        courses = {}
        all_course = Course.objects.all()
        for course in all_course:
            total_units = UnitAssign.objects.filter(course_code=course.course_code).count()
            courses[str(course)] = {
                'course_name': course.course_name,
                'course_code': course.course_code,
                'count': total_units
            }
        print(courses)
        context = {
            'all_courses': courses

        }
        return render(request, self.template, context)
        # return JsonResponse(context, safe=False)


class GetUnits(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    template = 'attendance/department/attendanceunits.html'

    def test_func(self):
        user = self.request.user
        return Department.objects.filter(dept_code=user).exists()

    def get(self, request, course_code):
        units = {}
        all_units = Unit.objects.filter(course_code=course_code)
        for unit in all_units:
            total_lectures = LecturerSession.objects.filter(unit_code=unit.unit_code).count()
            units[str(unit)] = {
                'unit_name': unit.unit_name,
                'unit_code': unit.unit_code,
                'count': total_lectures
            }
        print(units)
        context = {
            'all_units': units,
            'course_code': course_code
        }
        return render(request, self.template, context)


class ShowReport(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    template = 'attendance/department/reports.html'

    def test_func(self):
        user = self.request.user
        return Department.objects.filter(dept_code=user).exists()

    def get(self, request, unit_code):
        attendance_list_above_75 = {}
        attendance_list_less_than_75 = {}
        Lecturer_sessions = LecturerSession.objects.filter(unit_code=unit_code).count()
        attendance_by_unit = AttendanceList.objects.filter(unit_code=unit_code).values_list('adm_no', flat=True)
        if (Lecturer_sessions > 0):
            for each_student in attendance_by_unit:
                each_student_attendance = AttendanceList.objects.filter(adm_no=each_student,
                                                                        unit_code=unit_code).count()
                attendance_percent = (each_student_attendance / Lecturer_sessions) * 100
                if (attendance_percent >= 75):
                    student_name = Student.objects.values_list('full_name', flat=True).get(adm_no=each_student)
                    attendance_list_above_75[str(each_student)] = {
                        'attendance_percent': attendance_percent,

                        'student_name': student_name,
                        'lectures_attended': each_student_attendance,
                        'adm_no': each_student,
                    }
                else:
                    student_name = Student.objects.values_list('full_name', flat=True).get(adm_no=each_student)
                    attendance_list_less_than_75[str(each_student)] = {
                        'attendance_percent': attendance_percent,
                        'student_name': student_name,
                        'lectures_attended': each_student_attendance,
                        'adm_no': each_student,
                    }
            """
            lecturer = UnitAssign.objects.filter(unit_code=unit_code).select_related('staff_no')
            for lecturers in lecturer:
                name = lecturers.staff_no.full_name

            units = UnitAssign.objects.filter(unit_code=unit_code).select_related('unit_code')
            for unit in units:
                unit_name = unit.unit_code.unit_name
            """
            # return JsonResponse(attendance_list, safe=False)
            context = {
                'unit_code': unit_code,
                'lecturer_sessions': Lecturer_sessions,
                'attendance_list_above_75': attendance_list_above_75,
                'attendance_list_less_than_75': attendance_list_less_than_75
            }
            return render(request, self.template, context)


# class GetUnits(View):
#     # login_url = '/accounts/login/'
#     # redirect_field_name = 'redirect_to'
#     template = 'attendance/department/attendanceunits.html'
#
#     def get(self, request, course_code):
#         all_units = UnitAssign.objects.filter(course_code=course_code)
#         context = {
#             'all_units': all_units,
#         }
#         return render(request, self.template, context)


class GetReport(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    template = 'attendance/department/reports.html'
    print(template)

    def test_func(self):
        user = self.request.user
        return Department.objects.filter(dept_code=user).exists()

    def get(self, request, unit_code):
        attendance_list_above_75 = {}
        attendance_list_less_than_75 = {}
        Lecturer_sessions = LecturerSession.objects.filter(unit_code=unit_code).count()
        attendance_by_unit = AttendanceList.objects.filter(unit_code=unit_code).values_list('adm_no', flat=True)
        if (Lecturer_sessions > 0):
            for each_student in attendance_by_unit:
                each_student_attendance = AttendanceList.objects.filter(adm_no=each_student,
                                                                        unit_code=unit_code).count()
                attendance_percent = (each_student_attendance / Lecturer_sessions) * 100
                if (attendance_percent >= 75):
                    student_name = Student.objects.values_list('full_name', flat=True).get(adm_no=each_student)
                    attendance_list_above_75[str(each_student)] = {
                        'attendance_percent': attendance_percent,
                        'student_name': student_name,
                        'lectures_attended': each_student_attendance,
                        'adm_no': each_student,
                    }
                else:
                    student_name = Student.objects.values_list('full_name', flat=True).get(adm_no=each_student)
                    attendance_list_less_than_75[str(each_student)] = {
                        'attendance_percent': attendance_percent,
                        'student_name': student_name,
                        'lectures_attended': each_student_attendance,
                        'adm_no': each_student,
                    }

            # return JsonResponse(attendance_list, safe=False)
        context = {
            'unit_code': unit_code,
            'lecturer_sessions': Lecturer_sessions,
            'attendance_list_above_75': attendance_list_above_75,
            'attendance_list_less_than_75': attendance_list_less_than_75
        }
        return render(request, self.template, context)

#
# class ShowReport(View):
#     template = 'attendance/department/reports.html'
#
#     def get(self, request, unit_code):
#         attendance_list_above_75 = {}
#         attendance_list_less_than_75 = {}
#         Lecturer_sessions = LecturerSession.objects.filter(unit_code=unit_code).count()
#         attendance_by_unit = AttendanceList.objects.filter(unit_code=unit_code).values_list('adm_no', flat=True)
#         if (Lecturer_sessions > 0):
#             for each_student in attendance_by_unit:
#                 each_student_attendance = AttendanceList.objects.filter(adm_no=each_student,
#                                                                         unit_code=unit_code).count()
#                 attendance_percent = (each_student_attendance / Lecturer_sessions) * 100
#                 if (attendance_percent >= 75):
#                     student_name = Student.objects.values_list('full_name', flat=True).get(adm_no=each_student)
#                     attendance_list_above_75[str(each_student)] = {
#                         'attendance_percent': attendance_percent,
#
#                         'student_name': student_name,
#                         'lectures_attended': each_student_attendance,
#                         'adm_no': each_student,
#                     }
#                 else:
#                     student_name = Student.objects.values_list('full_name', flat=True).get(adm_no=each_student)
#                     attendance_list_less_than_75[str(each_student)] = {
#                         'attendance_percent': attendance_percent,
#                         'student_name': student_name,
#                         'lectures_attended': each_student_attendance,
#                         'adm_no': each_student,
#                     }
#             """
#             lecturer = UnitAssign.objects.filter(unit_code=unit_code).select_related('staff_no')
#             for lecturers in lecturer:
#                 name = lecturers.staff_no.full_name
#
#             units = UnitAssign.objects.filter(unit_code=unit_code).select_related('unit_code')
#             for unit in units:
#                 unit_name = unit.unit_code.unit_name
#             """
#             # return JsonResponse(attendance_list, safe=False)
#             context = {
#                 'unit_code': unit_code,
#                 'lecturer_sessions': Lecturer_sessions,
#                 'attendance_list_above_75': attendance_list_above_75,
#                 'attendance_list_less_than_75': attendance_list_less_than_75
#             }
#             return render(request, self.template, context)


class AddNewCourse(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    template = 'attendance/department/addcourse.html'
    form_class = forms.AddCourse

    def test_func(self):
        user = self.request.user
        return Department.objects.filter(dept_code=user).exists()

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            message = 'Course added successfully'
        return render(request, self.template, {'form': form, 'message': message})


class CoursesList(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    template = 'attendance/department/courses.html'

    def test_func(self):
        user = self.request.user
        return Department.objects.filter(dept_code=user).exists()

    def get(self, request):
        courses_list = Course.objects.all()
        return render(request, self.template, {'courses': courses_list})


class AddLecturer(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    template = 'attendance/department/addlecturer.html'
    form_class = forms.AddLecturer

    def test_func(self):
        user = self.request.user
        return Department.objects.filter(dept_code=user).exists()

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            message = 'Lecturer added successfully'
        return HttpResponseRedirect('lecturers', {'message': message})


class LecturersList(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    template = 'attendance/department/lecturers.html'

    def test_func(self):
        user = self.request.user
        return Department.objects.filter(dept_code=user).exists()

    def get(self, request):
        lecturers_list = Lecturer.objects.all()
        return render(request, self.template, {'lecturers': lecturers_list})


class UnitsList(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    template = 'attendance/department/units.html'

    def test_func(self):
        user = self.request.user
        return Department.objects.filter(dept_code=user).exists()

    def get(self, request):
        units_list = Unit.objects.all()
        return render(request, self.template, {'units': units_list})


class AddUnit(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    template = 'attendance/department/addunit.html'
    form_class = forms.AddUnit

    def test_func(self):
        user = self.request.user
        return Department.objects.filter(dept_code=user).exists()

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            message = 'Lecturer added successfully'
        return render(request, self.template, {'form': form, 'message': message})


class LecturerAssignUnit(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    form_class = forms.AssignUnit
    template = "attendance/department/addunitassign.html"

    def test_func(self):
        user = self.request.user
        return Department.objects.filter(dept_code=user).exists()

    def get(self, request):
        form = self.form_class(None)
        unitAssigned = UnitAssign.objects.all().values_list('unit_code', 'course_code')

        for checkUnit in unitAssigned:
            allUnits = Unit.objects.all().filter(unit_code=checkUnit)
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            unitCode = form.cleaned_data['unit_code']
            course = form.cleaned_data['course_code']
            assignedList = UnitAssign.objects.filter(unit_code=unitCode, course_code=course).count()
            # check if unit has already been assigned to another lecturer
            if assignedList > 0:
                error_message = str(unitCode) + ' has already been assigned'
                return render(request, self.template, {'error_message': error_message, 'form': form})
            else:
                instance = form.save(commit=False)
                instance.save()
                message = 'Unit assigned successfully'
                return HttpResponseRedirect('unitsassigned', {'form': form, 'message': message})


class AssignedUnits(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    template = "attendance/department/unitsassigned.html"

    def test_func(self):
        user = self.request.user
        return Department.objects.filter(dept_code=user).exists()

    def get(self, request):
        units = UnitAssign.objects.all().select_related('staff_no', 'unit_code')

        paginator = Paginator(units, 10)

        page = request.GET.get('page')
        unitsassigned = paginator.get_page(page)
        return render(request, self.template, {'units': unitsassigned})

# ===============================================lecturer views =========================


class LecturerIndex(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    template = 'attendance/lecturer/index.html'

    def test_func(self):
        user = self.request.user
        return Lecturer.objects.filter(staff_no=user).exists()

    def get(self, request):

        user = request.user
        # redirect(user)
        # lecturer = Lecturer.objects.filter(staff_no=user).exists()
        # lecturer instance

        if request.session.get('sessionId'):
            print('reached')
            session_id = request.session['sessionId']
            print(session_id)
            uuid_id = uuid.UUID(session_id)
            # print('uuid' + uuid_id)
            return redirect('attendance:takeattendance', sessionId=uuid_id)
        else:
            lecturer = Lecturer.objects.get(staff_no=user)
            lecturer_units = UnitAssign.objects.filter(staff_no=lecturer)
            context = {
                'lecturer_units': lecturer_units
            }
            # print(context)
            return render(request, self.template, context)


# uuid serializer
class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        return json.JSONEncoder.default(self, obj)


class EndSession(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'

    def test_func(self):
        user = self.request.user
        return Lecturer.objects.filter(staff_no=user).exists()

    def get(self, request):
        del request.session['sessionId']
        print(request.session.keys())
        return redirect('attendance:lecturerindex')


class StartSession(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    template = 'attendance/lecturer/session.html'
    form_class = forms.attendanceForm

    def test_func(self):
        user = self.request.user
        return Lecturer.objects.filter(staff_no=user).exists()

    def get(self, request, unit_code):
        # form = self.form_class(None)
        user = request.user
        # user = 1241
        staff_no = Lecturer.objects.get(staff_no=user)
        unit_code = Unit.objects.get(unit_code=unit_code)
        lecturerSession = LecturerSession(
            staff_no=staff_no,
            unit_code=unit_code
        )
        lecturerSession.save()
        session_id = lecturerSession.session_id
        # request.session['sessionId'] = json.dumps(session_id, cls=UUIDEncoder)
        request.session['sessionId'] = json.dumps(session_id, cls=UUIDEncoder)
        return redirect('attendance:takeattendance', sessionId=session_id)
        # return HttpResponseRedirect(reverse('attendance:takeattendance', args=(sessionId)))
    # return render(request, self.template, {'form': form})

    # def post(self, request):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         staff_no = Lecturer.objects.get(staff_no=request.user)
    #         session = form.save(commit=False)
    #         session.staff_no = staff_no
    #         session.date = timezone.now()
    #         session.save()
    #         session_id = session.session_id
    #         return HttpResponseRedirect(reverse('attendance:takeattendance', args=(session_id,)))
    #     # if form.is_valid():
    #     #     form.save(commit=True)
    #     #     return HttpResponseRedirect('attendance:takeattendance')


class SessionDetails(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    template = 'attendance/lecturer/previoussessions.html'

    def test_func(self):
        user = self.request.user
        return Lecturer.objects.filter(staff_no=user).exists()

    def get(self, request, unit_code):
        user = request.user

        # lecturer instance
        lecturer = Lecturer.objects.get(staff_no=user)
        lecturer_units = UnitAssign.objects.filter(staff_no=lecturer)
        sessions = LecturerSession.objects.filter(staff_no=lecturer, unit_code=unit_code)
        context = {
            'lecturer_units': lecturer_units,
            'sessions': sessions
        }

        return render(request, self.template, context)


class SessionAttendance(UserPassesTestMixin, LoginRequiredMixin, View):
    template = 'attendance/lecturer/sessionattendance.html'
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'

    def test_func(self):
        user = self.request.user
        return Lecturer.objects.filter(staff_no=user).exists()

    def get(self, request, sessionId):
        students = {}
        session_details = LecturerSession.objects.get(session_id=sessionId)
        signed_in_students_exists = AttendanceList.objects.filter(session_id=session_details.session_id).exists()
        if signed_in_students_exists:
            # signed_in_students = AttendanceList.objects.filter(session_id=session_details.session_id)
            student_details = AttendanceList.objects.filter(session_id=session_details.session_id).select_related('adm_no')
            for student in student_details:
                name = student.adm_no.full_name
                students[str(student.adm_no.full_name)] = {
                    'adm_no': student.adm_no.adm_no,
                    'name': name,
                    'date': student.date
                }
            # context = {
            #     'session_details': session_details,
            #     'signed_in_students': signed_in_students
            # }
            context = {
                'students': students
            }
        else:
            context = {
                'message': 'No student attended this lecture.'
            }
        return render(request, self.template, context)


class TakeAttendance(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    template = 'attendance/lecturer/takeattendance.html'
    form_class = forms.TakeAttendanceForm

    def test_func(self):
        user = self.request.user
        return Lecturer.objects.filter(staff_no=user).exists()

    def get(self, request, sessionId):
        session_details = LecturerSession.objects.get(session_id=sessionId)
        signed_in_students = AttendanceList.objects.filter(session_id=session_details.session_id)
        form = self.form_class
        context = {
            'session_details': session_details,
            'form': form,
            'signed_in_students': signed_in_students
        }
        return render(request, self.template, context)

    def post(self, request, sessionId):
        print(sessionId)
        session_details = LecturerSession.objects.get(session_id=sessionId)

        form = self.form_class(request.POST)
        if form.is_valid():
            adm_no = form.cleaned_data['admission_number']
            print(adm_no)
            already_signed_in = AttendanceList.objects.filter(adm_no=adm_no, session=session_details.session_id).exists()
            print(already_signed_in)
            if already_signed_in:
                messages.success(request, "student " + str(adm_no) + " has been signed in already")
                return redirect('attendance:takeattendance', sessionId=sessionId)
                # return HttpResponseRedirect(reverse('attendance:takeattendance', args=(sessionId,)))
            else:
                student = Student.objects.filter(adm_no=adm_no).exists()
                if student:
                    # model instances
                    adm_no = Student.objects.get(adm_no=adm_no)
                    staff_no = Lecturer.objects.get(staff_no=request.user)
                    unit_code = session_details.unit_code
                    # print(unit_code)
                    # course = Unit.objects.values_list('course_code', flat=True).get(unit_code=unit_code)
                    # print(course)
                    course_code = Course.objects.get(course_code='com')
                    attendanceList = AttendanceList(
                        adm_no=adm_no,
                        unit_code=unit_code,
                        staff_no=staff_no,
                        course_code=course_code,
                        session=session_details
                    )

                    attendanceList.save()
                    messages.success(request, "student " + str(adm_no) + "  has been signed in")
                    return redirect('attendance:takeattendance', sessionId=sessionId)
                else:
                    print('reached else')
                    messages.warning(request, "student " + str(adm_no) + " has not registered for this unit")
                    return redirect('attendance:takeattendance', sessionId=sessionId)
                # return HttpResponseRedirect(reverse('attendance:takeattendance', args=(sessionId,)))


class LecturerUnits(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    template = 'attendance/lecturer/reportunits.html'

    def test_func(self):
        user = self.request.user
        return Lecturer.objects.filter(staff_no=user).exists()

    def get(self, request):
        user = request.user
        # user = 1241
        # lecturer = Lecturer.objects.filter(staff_no=user).exists()
        # lecturer instance
        lecturer = Lecturer.objects.get(staff_no=user)
        lecturer_units = UnitAssign.objects.filter(staff_no=lecturer).select_related('unit_code')
        context = {
            'lecturer_units': lecturer_units
        }
        print(context)
        return render(request, self.template, context)


class LecturerReports(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    template = 'attendance/lecturer/attendance.html'

    def test_func(self):
        user = self.request.user
        return Lecturer.objects.filter(staff_no=user).exists()

    def get(self, request, unit_code):
        attendance_list_above_75 = {}
        attendance_list_less_than_75 = {}
        Lecturer_sessions = LecturerSession.objects.filter(unit_code=unit_code).count()
        attendance_by_unit = AttendanceList.objects.filter(unit_code=unit_code).values_list('adm_no', flat=True)
        if (Lecturer_sessions > 0):
            for each_student in attendance_by_unit:
                each_student_attendance = AttendanceList.objects.filter(adm_no=each_student,
                                                                        unit_code=unit_code).count()
                attendance_percent = (each_student_attendance / Lecturer_sessions) * 100
                if (attendance_percent >= 75):
                    student_name = Student.objects.values_list('full_name', flat=True).get(adm_no=each_student)
                    attendance_list_above_75[str(each_student)] = {
                        'attendance_percent': attendance_percent,
                        'student_name': student_name,
                        'lectures_attended': each_student_attendance,
                        'adm_no': each_student,
                    }
                else:
                    student_name = Student.objects.values_list('full_name', flat=True).get(adm_no=each_student)
                    attendance_list_less_than_75[str(each_student)] = {
                        'attendance_percent': attendance_percent,
                        'student_name': student_name,
                        'lectures_attended': each_student_attendance,
                        'adm_no': each_student,
                    }

            # return JsonResponse(attendance_list, safe=False)
        context = {
            'unit_code': unit_code,
            'lecturer_sessions': Lecturer_sessions,
            'attendance_list_above_75': attendance_list_above_75,
            'attendance_list_less_than_75': attendance_list_less_than_75
        }
        return render(request, self.template, context)

#============================================student views =====================================


class StudentIndex(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    template = 'attendance/student/index.html'

    def test_func(self):
        user = self.request.user
        return Student.objects.filter(adm_no=user).exists()

    def get(self, request):
        attendance = {}
        user = request.user
        # user = 'com/006/15'
        student = Student.objects.get(adm_no=user)
        all_registered_units = RegisteredUnit.objects.filter(adm_no=student).values_list('unit_code', flat=True)
        for unit in all_registered_units:
            total_sessions = LecturerSession.objects.filter(unit_code=unit).count()
            attended_sessions = AttendanceList.objects.filter(unit_code=unit, adm_no=student).count()
            if (total_sessions > 0):
                attendance_percent = (attended_sessions / total_sessions) * 100
                unit_name = Unit.objects.values_list('unit_name', flat=True).get(unit_code=unit)

                attendance[str(unit)] = {
                    'unit_code': unit,
                    'unit_name': unit_name,
                    'Total_sessions': total_sessions,
                    'attended_sessions': attended_sessions,
                    'attendance_percent': attendance_percent,
                }
        context = {
            'attendance': attendance
        }
        # return JsonResponse(attendance)
        return render(request, self.template,context)


class StudentRegisteredUnits(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    template = 'attendance/student/registeredunits.html'

    def test_func(self):
        user = self.request.user
        return Student.objects.filter(adm_no=user).exists()

    def get(self, request):
        user = request.user
        unit_details = {}
        student = Student.objects.get(adm_no=user)

        all_registered_units = RegisteredUnit.objects.filter(adm_no=student).values_list('unit_code', flat=True)

        for unit in all_registered_units:

            each_unit_details = Unit.objects.get(unit_code=unit)

            unit_details[str(unit)] = {
                'unit_code': each_unit_details.unit_code,
                'unit_name': each_unit_details.unit_name
            }

        context = {
            'unit_details': unit_details
        }
        # return JsonResponse(context)
        return render(request, self.template, context)


class StudentRegisterUnits(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    template = 'attendance/student/registerunits.html'

    def test_func(self):
        user = self.request.user
        return Student.objects.filter(adm_no=user).exists()

    def get(self, request):
        user = request.user

        # student instance
        courses = Student.objects.filter(adm_no=user).select_related('course_code')
        for course in courses:
            course = course.course_code.course_code
            all_units = Unit.objects.filter(course_code=course)
        return render(request, self.template, {'units': all_units})

    def post(self, request):
        pass
# ========================================== pdf views =========================================

# select al  courses stored in the database


class PdfCourses(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    template = 'attendance/department/pdfcourses.html'

    def test_func(self):
        user = self.request.user
        return Department.objects.filter(dept_code=user).exists()

    def get(self, request):
        all_courses = Course.objects.all()
        context = {
            'all_course': all_courses,
        }
        return render(request, self.template, context)

# get the units that a related to a given unit and have already been assigned to a lecture


class PdfUnits(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    template = 'attendance/department/pdfunits.html'

    def get(self, request, course_code):
        all_units = UnitAssign.objects.filter(course_code=course_code)
        context = {
            'all_units': all_units,
        }
        return render(request, self.template, context)

# generate reports for a given unit
# unit code is passed from @template pdfunits.html


class GetPdfReports(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    template = 'attendance/department/perunitpdf.html'

    def get(self, request, unit_code):
        attendance_list_above_75 = {}
        attendance_list_less_than_75 = {}
        Lecturer_sessions = LecturerSession.objects.filter(unit_code=unit_code).count()
        attendance_by_unit = AttendanceList.objects.filter(unit_code=unit_code).values_list('adm_no', flat=True)
        if (Lecturer_sessions > 0):
            for each_student in attendance_by_unit:
                each_student_attendance = AttendanceList.objects.filter(adm_no=each_student, unit_code=unit_code).count()
                attendance_percent = (each_student_attendance / Lecturer_sessions) * 100
                if (attendance_percent >= 75):
                    student_name = Student.objects.values_list('full_name', flat=True).get(adm_no=each_student)
                    attendance_list_above_75[str(each_student)] = {
                        'attendance_percent': attendance_percent,

                        'student_name': student_name,
                        'lectures_attended': each_student_attendance,
                        'adm_no': each_student,
                    }
                else:
                    student_name = Student.objects.values_list('full_name', flat=True).get(adm_no=each_student)
                    attendance_list_less_than_75[str(each_student)] = {
                        'attendance_percent': attendance_percent,
                        'student_name': student_name,
                        'lectures_attended': each_student_attendance,
                        'adm_no': each_student,
                    }
            lecturer = UnitAssign.objects.filter(unit_code = unit_code).select_related('staff_no')
            for lecturers in lecturer:
                name = lecturers.staff_no.full_name

            units = UnitAssign.objects.filter(unit_code=unit_code).select_related('unit_code')
            for unit in units:
                unit_name = unit.unit_code.unit_name


            # return JsonResponse(attendance_list, safe=False)
            context = {
                'Lecturer': name,
                'today': datetime.datetime.now(),
                'unitcode': unit_code,
                'unitname': unit_name,
                'course': '',
                'lecturer_sessions': Lecturer_sessions,
                'attendance_list_above_75': attendance_list_above_75,
                'attendance_list_less_than_75': attendance_list_less_than_75,
                'lecturer_details': ""
            }
        pdf = render_to_pdf('attendance/department/perunitpdf.html', context)
        return HttpResponse(pdf, content_type='application/pdf')

class LecturerPdfReports(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, unit_code):
        attendance_list_above_75 = {}
        attendance_list_less_than_75 = {}
        context = {}
        Lecturer_sessions = LecturerSession.objects.filter(unit_code=unit_code).count()
        attendance_by_unit = AttendanceList.objects.filter(unit_code=unit_code).values_list('adm_no', flat=True)
        if (Lecturer_sessions > 0):
            for each_student in attendance_by_unit:
                each_student_attendance = AttendanceList.objects.filter(adm_no=each_student, unit_code=unit_code).count()
                attendance_percent = (each_student_attendance / Lecturer_sessions) * 100
                if (attendance_percent >= 75):
                    student_name = Student.objects.values_list('full_name', flat=True).get(adm_no=each_student)
                    attendance_list_above_75[str(each_student)] = {
                        'attendance_percent': attendance_percent,

                        'student_name': student_name,
                        'lectures_attended': each_student_attendance,
                        'adm_no': each_student,
                    }
                else:
                    student_name = Student.objects.values_list('full_name', flat=True).get(adm_no=each_student)
                    attendance_list_less_than_75[str(each_student)] = {
                        'attendance_percent': attendance_percent,
                        'student_name': student_name,
                        'lectures_attended': each_student_attendance,
                        'adm_no': each_student,
                    }
            lecturer = UnitAssign.objects.filter(unit_code=unit_code).select_related('staff_no')
            for lecturers in lecturer:
                name = lecturers.staff_no.full_name

            units = UnitAssign.objects.filter(unit_code=unit_code).select_related('unit_code')
            for unit in units:
                unit_name = unit.unit_code.unit_name
            #getting the course name
            courses = UnitAssign.objects.filter(unit_code=unit_code).select_related('course_code')
            for course in courses:
                course_name = course.course_code.course_name
                # return JsonResponse(attendance_list, safe=False)
                context = {
                    'Lecturer': name,
                    'today': datetime.datetime.now(),
                    'unitcode': unit_code,
                    'unitname': unit_name,
                    'course': course_name,
                    'lecturer_sessions': Lecturer_sessions,
                    'attendance_list_above_75': attendance_list_above_75,
                    'attendance_list_less_than_75': attendance_list_less_than_75,
                    'lecturer_details': "",
                    }
        template = 'attendance/lecturer/lecturerpdf.html'
        pdf = render_to_pdf(template, context)
        return HttpResponse(pdf, content_type='application/pdf')


class Studentpdf(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    template = 'attendance/student/studentpdf.html'

    def get(self, request):
        attendance = {}
        user = request.user
        # user = 'com/006/15'
        student = Student.objects.get(adm_no=user)
        all_registered_units = RegisteredUnit.objects.filter(adm_no=student).values_list('unit_code', flat=True)
        for unit in all_registered_units:
            total_sessions = LecturerSession.objects.filter(unit_code=unit).count()
            attended_sessions = AttendanceList.objects.filter(unit_code=unit, adm_no=student).count()
            unit_name = Unit.objects.values_list('unit_name', flat=True).get(unit_code=unit)
            print(unit)
            if total_sessions > 0:
                attendance_percent = (attended_sessions / total_sessions) * 100
                attendance[str(unit)] = {
                    'unit_code': unit,
                    'unit_name': unit_name,
                    'Total_sessions': total_sessions,
                    'attended_sessions': attended_sessions,
                    'attendance_percent': attendance_percent,
                }
            #getting the name of the student
            student_name = Student.objects.values_list('full_name', flat=True).get(adm_no=user)
            #getting the course name
            course_code = Student.objects.values_list('course_code', flat=True).get(adm_no=user)
            course_name = Course.objects.values_list('course_name', flat=True).get(course_code=course_code)
        print(attendance)
        context = {
            'attendance': attendance,
            'adm_no' : user,
            'name' : student_name,
            'course' : course_name,
            'today': datetime.datetime.today()
        }
        # return JsonResponse(attendance)
        pdf = render_to_pdf('attendance/student/studentpdf.html', context)
        return HttpResponse(pdf, content_type='application/pdf')


class DepartmentPdfReports(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    template = 'attendance/department/perunitpdf.html'

    def get(self, request, unit_code):
        attendance_list_above_75 = {}
        attendance_list_less_than_75 = {}
        Lecturer_sessions = LecturerSession.objects.filter(unit_code=unit_code).count()
        attendance_by_unit = AttendanceList.objects.filter(unit_code=unit_code).values_list('adm_no', flat=True)
        if (Lecturer_sessions > 0):
            for each_student in attendance_by_unit:
                each_student_attendance = AttendanceList.objects.filter(adm_no=each_student, unit_code=unit_code).count()
                attendance_percent = (each_student_attendance / Lecturer_sessions) * 100
                if (attendance_percent >= 75):
                    student_name = Student.objects.values_list('full_name', flat=True).get(adm_no=each_student)
                    attendance_list_above_75[str(each_student)] = {
                        'attendance_percent': attendance_percent,

                        'student_name': student_name,
                        'lectures_attended': each_student_attendance,
                        'adm_no': each_student,
                    }
                else:
                    student_name = Student.objects.values_list('full_name', flat=True).get(adm_no=each_student)
                    attendance_list_less_than_75[str(each_student)] = {
                        'attendance_percent': attendance_percent,
                        'student_name': student_name,
                        'lectures_attended': each_student_attendance,
                        'adm_no': each_student,
                    }
            lecturer = UnitAssign.objects.filter(unit_code=unit_code).select_related('staff_no')
            for lecturers in lecturer:
                name = lecturers.staff_no.full_name

            units = UnitAssign.objects.filter(unit_code=unit_code).select_related('unit_code')
            for unit in units:
                unit_name = unit.unit_code.unit_name
            courses = UnitAssign.objects.filter(unit_code=unit_code).select_related('course_code')
            for course in courses:
                course_name = course.course_code.course_name
            # return JsonResponse(attendance_list, safe=False)
            context = {
                'Lecturer': name,
                'today': datetime.datetime.now(),
                'unitcode': unit_code,
                'unitname': unit_name,
                'course': course_name,
                'lecturer_sessions': Lecturer_sessions,
                'attendance_list_above_75': attendance_list_above_75,
                'attendance_list_less_than_75': attendance_list_less_than_75,
                'lecturer_details': ""
            }
        pdf = render_to_pdf('attendance/department/perunitpdf.html', context)
        return HttpResponse(pdf, content_type='application/pdf')
