from django import forms
from django.contrib.auth.models import User
from .models import AttendanceList, Course, Lecturer, Unit, LecturerSession, UnitAssign


class AddCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class AddLecturer(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = '__all__'


class AddUnit(forms.ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'


class ChangePasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'name': 'password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'name': 'confirm_password'}))

    class Meta:
        model = User
        fields = ['username', 'password']

    def validate_password(self):
        password1 = self.cleaned_data['password']
        password2 = self.cleaned_data['confirm_password']
        if password1 != password2:
            raise forms.ValidationError('The two passwords do not match')


class LoginForm(forms.ModelForm):
    username = forms.CharField(label='Employee/Reg No.', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employee/Reg No.', 'autofocus': 'True'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))

    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first name'}))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last name'}))
    email = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'email address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class Filter(forms.ModelForm):
    class Meta:
        model = AttendanceList
        fields = ['course_code', 'unit_code']


class SessionStart(forms.ModelForm):
    class Meta:
        model = LecturerSession
        fields = ['unit_code']


class TakeAttendanceForm(forms.Form):
    admission_number = forms.CharField(label='Admission Number', max_length=50, widget=forms.TextInput(attrs={'autofocus': True}))

class Course_Form(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_code', 'course_name']

class lec_session_Form(forms.ModelForm):
    class Meta:
        model = LecturerSession
        fields = ['unit_code']

class attendanceForm(forms.Form):
    adm_no = forms.CharField(label='Admission Number')


class signUpForm(forms.Form):
    username = forms.CharField(max_length=150, label='Employee/Reg No.',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employee/Reg No.'}))
    email = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'email address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))


class AssignUnit(forms.ModelForm):
    class Meta:
        model = UnitAssign
        fields = '__all__'
