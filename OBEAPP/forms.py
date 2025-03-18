from django.forms import ModelForm,widgets
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class COPOMatrixForm(forms.ModelForm):
    class Meta:
        model = CO_PO_Matrix
        fields = ['course', 'co_code', 'po_code', 'strength']
        widgets = {
            'course': forms.Select(attrs={'class': 'form-control'}),
            'co_code': forms.Select(attrs={'class': 'form-control'}),
            'po_code': forms.Select(attrs={'class': 'form-control'}),
            'strength': forms.Select(attrs={'class': 'form-control'}),
        }


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class CourseForm(forms.ModelForm):
    class Meta:
        model= AssignCourse
        fields = '__all__'
        widgets = {
            'semester' : forms.Select(attrs={'class': 'form-input'}),
            'course' : forms.Select(attrs={'class': 'form-input'}),
            'format' : forms.Select(attrs={'class': 'form-input'}),
            'completion':forms.Select(attrs={'class': 'form-input'}),
           

        }



class SemesterForm(ModelForm):
    class Meta:
        model= AssignSemester
        fields = '__all__'
        #fields=['semester','result_status']
        widgets = {
            'session': forms.Select(attrs={'class': 'form-input'}),
            'semester': forms.Select(attrs={'class': 'form-input'}),
            'result_status': forms.Select(attrs={'class': 'form-input'}),
        }

class SessionForm(forms.ModelForm):
    class Meta:
        model= AssignSession
        fields = '__all__'
        widgets = {
            'department' : forms.Select(attrs={'class': 'form-input'}),
            'session' : forms.Select(attrs={'class': 'form-input'}),

        }
class DepartmentForm(ModelForm):
    class Meta:
        model= Department
        fields = '__all__'
        widgets={
        'name':forms.TextInput(attrs={'class':'form-input'}),
        'faculty_name' : forms.Select(attrs={'class': 'form-input'}),
        
        
        }

class FacultyForm(ModelForm):
    class Meta:
        model=Faculty
        fields = '__all__'
        widgets={
        'name':forms.TextInput(attrs={'class':'form-input'}),

        }
class NonObeForm(ModelForm):
    class Meta:
        model = NonObeMark
        fields = '__all__'
        widgets = {
            'course': forms.Select(attrs={'class': 'form-input'}),
            'student': forms.Select(attrs={'class': 'form-input'}),
            'tt1': forms.TextInput(attrs={'class': 'form-input'}),
            'tt2': forms.TextInput(attrs={'class': 'form-input'}),
            'tt3': forms.TextInput(attrs={'class': 'form-input'}),
            'att': forms.TextInput(attrs={'class': 'form-input'}),
            'sem': forms.Select(attrs={'class': 'form-input'}),
            'mark': forms.Select(attrs={'class': 'form-input'}),
            }

class ObeForm(ModelForm):
    class Meta:
      model = ObeMark
      fields = '__all__'
    fields = [
            'student'
            'course',  # Ensure this matches the field name in the model
            'Q1', 'Q2', 'Q3', 'Q4', 'Q5',
            'Assignment1', 'Assignment2',
            'Mid',
            'co1', 'co2', 'co3', 'co4', 'co5'
        ]

class AssignCourseForm(ModelForm):
    class Meta:
        model = AssignCourse
        fields = ['completion']
        widgets = {
            'completion': forms.Select(attrs={'class': 'form-input'}),
        }

class AssignSemesterForm(ModelForm):
    class Meta:
        model = AssignSemester
        fields = ['result_status']

class StudentForm(ModelForm):
    class Meta:
        model= Student
        fields='__all__'
        exclude = ['user']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-input'}),
            'registration_no': forms.TextInput(attrs={'class': 'form-input'}),
            'roll': forms.TextInput(attrs={'class': 'form-input'}),
            'exam_roll': forms.TextInput(attrs={'class': 'form-input'}),
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'batch': forms.TextInput(attrs={'class': 'form-input'}),
            'department': forms.Select(attrs={'class': 'form-input'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-input'}),


        }

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields='__all__'
        exclude =['user']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-input'}),
           
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'designation': forms.TextInput(attrs={'class': 'form-input'}),
            'department': forms.Select(attrs={'class': 'form-input'}),
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'class': 'form-input'}),
            'status': forms.Select(attrs={'class': 'form-input'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-input'}),
            

        }
class AssignTeacherForm(ModelForm):
    class Meta:
        model = AssignTeacher
        fields = '__all__'
        exclude =['user']
        widgets = {
            
            'course': forms.Select(attrs={'class': 'form-input'}),
            'teacher': forms.Select(attrs={'class': 'form-input'}),
            
        }
class AssignChairmanForm(ModelForm):
    class Meta:
        model = AssignChairman
        fields = '__all__'
        exclude =['user']
        widgets = {
            
            
            'department': forms.Select(attrs={'class': 'form-input'}),
            'chairman': forms.Select(attrs={'class': 'form-input'}),
            
        } 
class AssignTeacherForm(ModelForm):
    class Meta:
        model = AssignTeacher
        fields = '__all__'
        exclude =['user']
        widgets = {
            
            
            'course': forms.Select(attrs={'class': 'form-input'}),
            'teacher': forms.Select(attrs={'class': 'form-input'}),
            
        }      
