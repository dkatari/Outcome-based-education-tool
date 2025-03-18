from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Session)
admin.site.register(Semester)
admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(AssignSession)
admin.site.register(AssignSemester)
admin.site.register(AssignCourse)
admin.site.register(AssignStudent)
admin.site.register(AssignTeacher)
admin.site.register(AssignChairman)
admin.site.register(AssignExamCommittee)
admin.site.register(NonObeMark)
admin.site.register(ObeMark)
admin.site.register(CO_PO_Matrix)
admin.site.register(ObeSem)

