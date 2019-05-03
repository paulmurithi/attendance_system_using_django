from django.urls import path, include
from . import views, apiviews
from django.contrib.auth import views as auth_views

app_name = "attendance"
urlpatterns = [
    # # signup views
    # path('student/signup', views.StudentLogin.as_view(), name='studentlogin'),
    # path('lecturer/signup', views.LecturerLogin.as_view(), name='lecturerlogin'),
    # path('department/signup', views.DepartmentLogin.as_view(), name='departmentlogin'),
    #
    # #logins urls
    # path('student/login', views.StudentLogin.as_view(), name='studentlogin'),
    # path('lecturer/login', views.LecturerLogin.as_view(), name='lecturerlogin'),
    # path('department/login', views.DepartmentLogin.as_view(), name='departmentlogin'),
    #
    # # signup urls
    # path('student/signup', views.StudentLogin.as_view(), name='studentregister'),
    # path('lecturer/signup', views.LecturerLogin.as_view(), name='lecturerregister'),
    # path('department/signup', views.DepartmentLogin.as_view(), name='departmentregister'),

    # namu views
    path('logout/', views.Logout.as_view(), name='customlogout'),
    path('signup/', views.SignUp.as_view(), name='sign_up'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view()),
    path('passwordchange/', auth_views.PasswordChangeView.as_view()),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view()),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
    # path('lec_module', views.lec_module, name='lec_module'),
    # path('stud_module', views.stud_module, name='stud_module'),
    # path('start_session/<str:unit_code>', views.start_seesion, name='start_session'),
    # path('session/<uuid:session_id>', views.session_details, name='session'),

    # # department urls
    # path('department/', views.DepartmentIndex.as_view(), name='departmentindex'),
    # path('department/units/<str:course_code>', views.GetUnits.as_view(), name='department_get_units'),
    # path('department/report/<str:unit_code>', views.GetReport.as_view(), name='department_get_reports'),
    path('department/', views.DepartmentIndex.as_view(), name='departmentindex'),
    path('department/units/<str:course_code>', views.GetUnits.as_view(), name='department_get_units'),
    path('department/report/<str:unit_code>', views.ShowReport.as_view(), name='department_get_reports'),

    # pdf
    path('department/pdf', views.PdfCourses.as_view(), name='pdfcourses'),
    path('department/pdf/units/<str:course_code>', views.PdfUnits.as_view(), name='pdfunits'),
    path('department/pdf/reports/<str:unit_code>', views.GetPdfReports.as_view(), name='pdf_per_unit_reports'),

    path('department/addcourse', views.AddNewCourse.as_view(), name='addcourse'),
    path('department/courses', views.CoursesList.as_view(), name='courses'),
    path('department/lecturers', views.LecturersList.as_view(), name='lecturers'),
    path('department/addlecturer', views.AddLecturer.as_view(), name='addlecturer'),
    path('department/addunit', views.AddUnit.as_view(), name='addunit'),
    path('department/units', views.UnitsList.as_view(), name='units'),
    path('department/addunitassign', views.LecturerAssignUnit.as_view(), name='addunitassign'),
    path('department/unitsassigned', views.AssignedUnits.as_view(), name='unitsassigned'),
    path('department/reports/<str:unit_code>', views.DepartmentPdfReports.as_view(), name='departmentpdf'),
    # path('api/filter', views.filter, name='filter'),
    # path('api/attendance', apiviews.AttendanceList.as_view(), name='attendance_list'),
    # path('api/filter', apiviews.filter, name='filter'),

    # lecturer views
    path('lecturer/', views.LecturerIndex.as_view(), name='lecturerindex'),
    path('lecturer/units', views.LecturerUnits.as_view(), name='reportunits'),
    path('lecturer/units/<str:unit_code>', views.LecturerReports.as_view(), name='attendanceanalysis'),
    path('lecturer/session/<str:unit_code>', views.StartSession.as_view(), name='lecturersession'),
    path('lecturer/sessiondetails/<str:unit_code>', views.SessionDetails.as_view(), name='sessiondetails'),
    path('lecturer/sessionattendance/<uuid:sessionId>', views.SessionAttendance.as_view(), name='sessionattendance'),
    path('lecturer/endsession/', views.EndSession.as_view(), name='endsession'),
    path('lecturer/reports/<str:unit_code>', views.LecturerPdfReports.as_view(), name='lecturerpdf'),
    path('lecturer/takeattendance/<uuid:sessionId>', views.TakeAttendance.as_view(), name='takeattendance'),

    # student urls
    path('student/', views.StudentIndex.as_view(), name='studentindex'),
    path('student/units', views.StudentRegisteredUnits.as_view(), name='registered_units'),
    path('student/register', views.StudentRegisterUnits.as_view(), name='register_units'),
    path('student/reports', views.Studentpdf.as_view(),name='student_pdf'),

    #pdf urls

    # path('department/pdf/', views.GetPdfReports.as_view(), name='generatepdf'),
    path('', views.Index.as_view(), name='index'),
]
