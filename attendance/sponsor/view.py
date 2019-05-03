from django.shortcuts import render, redirect
from django.views import View
from . import forms
from .models import Lecturer, Student, Department
from django.contrib.auth.models import User

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