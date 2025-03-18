from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users,admin_only
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.models import Group
# Create your views here.

def home(request):
    return render(request, 'OBEAPP/front.html')

@login_required(login_url='login')
@admin_only
def main(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    stdcnt = Student.objects.count()
    teacnt = Teacher.objects.count()
    dept_cnt = Department.objects.count()
    context = {'students':student, 'teacheres':teachers,'stdcnt':stdcnt,'teacnt':teacnt,'dept_cnt':dept_cnt}
    return render(request, 'OBEAPP/main.html',context)

@allowed_users(allowed_roles=['student'])
def studentAccount(request):

    student = request.user.student
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES,instance=student)
        if form.is_valid():
            form.save()


    context={'form':form}
    return render(request,'OBEAPP/studentAccount.html',context)
@allowed_users(allowed_roles=['teacher','chairman'])
def teacherAccount(request):

    teacher = request.user.teacher
    form = TeacherForm(instance=teacher)
    if request.method == 'POST':
        form = TeacherForm(request.POST,request.FILES,instance=teacher)
        if form.is_valid():
            form.save()


    context={'form':form}
    return render(request,'OBEAPP/teacherAccount.html',context)

def contact(request):
    return render(request,'OBEAPP/contact.html')

def about(request):
    return render(request,'OBEAPP/aboutus.html')

@unauthenticated_user
def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('main')
        else:
            messages.info(request,'Username or Password is incorrect')
    context = {}
    return render(request,'OBEAPP/login.html',context)
@unauthenticated_user
def signupPage(request):
    form = CreateUserForm()
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            #group = Group.objects.get()
            messages.success(request,'Account was created for '+user)
            return redirect('login')

    context={'form':form}
    return render(request,'OBEAPP/signup.html',context)

def logoutUser(request):
    logout(request)
    return redirect('/')

@login_required(login_url='login')
@admin_only
def student(request):
    students = Student.objects.all()
    student_cnt = students.count()

    context = {'students': students, 'student_cnt': student_cnt}
    return render(request,'OBEAPP/student.html',context)

@login_required(login_url='login')
@admin_only
def add_student(request):

    form = StudentForm()
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('student'))
    context = {'form':form}
    return render(request,'OBEAPP/course_form.html',context)

@login_required(login_url='login')
@admin_only
def update_student(request,pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)
    if request.method=='POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('student'))
    context = {'form':form}
    return render(request,'OBEAPP/course_form.html',context)

@login_required(login_url='login')
@admin_only
def delete_student(request,pk):
    student = Student.objects.get(id=pk)

    if request.method=='POST':
       student.delete()
       return HttpResponseRedirect(reverse('student'))
    context = {'item':student}
    return render(request,'OBEAPP/delete_student.html',context)

@login_required(login_url='login')
@admin_only
def teacher(request):
    teachers = Teacher.objects.all()
    teacher_cnt = teachers.count()

    context = {'teachers': teachers, 'teacher_cnt': teacher_cnt}
    return render(request,'OBEAPP/teacher.html',context)

@login_required(login_url='login')
@admin_only
def add_teacher(request):

    form = TeacherForm()
    if request.method=='POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teacher'))
    context = {'form':form}
    return render(request,'OBEAPP/course_form.html',context)

@login_required(login_url='login')
@admin_only
def update_teacher(request,pk):
    teacher = Teacher.objects.get(id=pk)
    form = TeacherForm(instance=teacher)
    if request.method=='POST':
        form = TeacherForm(request.POST,instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teacher'))
    context = {'form':form}
    return render(request,'OBEAPP/course_form.html',context)

@login_required(login_url='login')
@admin_only
def delete_teacher(request,pk):
    teacher = Teacher.objects.get(id=pk)

    if request.method=='POST':
       teacher.delete()
       return HttpResponseRedirect(reverse('teacher'))
    context = {'item':teacher}
    return render(request,'OBEAPP/delete_teacher.html',context)


def session(request):
    return render(request,'OBEAPP/session.html')

def semester(request):
    return render(request,'OBEAPP/semester.html')

def course(request):
    courses=Course.objects.all()
    course_cnt = courses.count()

    context = {'courses': courses,'course_cnt': course_cnt}
    return render(request,'OBEAPP/course.html',context)

@login_required(login_url='login')
@admin_only
def department(request):
    departments=Department.objects.all()
    dept_cnt=departments.count()
    context = {'departments':departments, 'dept_cnt':dept_cnt}
    return render(request,'OBEAPP/department.html',context)

@login_required(login_url='login')
@admin_only
def faculty(request):
    faculties=Faculty.objects.all()
    fac_cnt=faculties.count()
    context = {'faculties':faculties, 'fac_cnt':fac_cnt}
    return render(request,'OBEAPP/faculty.html',context)


@login_required(login_url='login')
@admin_only
def add_faculty(request):

    form = FacultyForm()
    if request.method=='POST':
        form =  FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('faculty'))
    context = {'form':form}
    return render(request,'OBEAPP/course_form.html',context)

@login_required(login_url='login')
@admin_only
def update_faculty(request,pk):
    faculty =  Faculty.objects.get(id=pk)
    form =  FacultyForm(instance=faculty)
    if request.method=='POST':
        form = FacultyForm(request.POST,instance=faculty)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('faculty'))
    context = {'form':form}
    return render(request,'OBEAPP/course_form.html',context)

@login_required(login_url='login')
@admin_only
def delete_faculty(request,pk):
    faculty = Faculty.objects.get(id=pk)

    if request.method=='POST':
       faculty.delete()
       return HttpResponseRedirect(reverse('faculty'))
    context = {'item':faculty}
    return render(request,'OBEAPP/delete_faculty.html',context)


@login_required(login_url='login')
def assign_session(request,pk):
    dept = Department.objects.get(id=pk)
    sessions = dept.assignsession_set.all()
    session_cnt = sessions.count()
    context={'sessions':sessions,'session_cnt':session_cnt,'dept':dept}
    return render(request,'OBEAPP/session.html',context)

def assign_semester(request,pk2):
    session = AssignSession.objects.get(id=pk2)
    semesters = session.assignsemester_set.all()
    semester_cnt = semesters.count()
    context = {'semesters':semesters,'semester_cnt':semester_cnt,'session':session}
    return render(request,'OBEAPP/semester.html',context)

def assign_course(request,pk3):
    semester = AssignSemester.objects.get(id=pk3)
    courses = semester.assigncourse_set.all()
    course_cnt = courses.count()
    context = {'courses':courses, 'course_cnt':course_cnt,'semester':semester}
    return render(request,'OBEAPP/course.html',context)

def assign_student(request):
    return render(request,'OBEAPP/student.html')

# def assign_teacher(request):
#     return render(request,'OBEAPP/teacher.html')

def assign_chairman(request):
    return render(request,'OBEAPP/teacher.html')
def assign_examcommittee(request):
    return render(request,'OBEAPP/teacher.html')

def add_assigncourse(request,pk4):
    semester = AssignSemester.objects.get(id=pk4)
    form = CourseForm(initial={'semester':semester})
    if request.method=='POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('assigncourse', args=(pk4,)))
    context = {'form':form}
    return render(request,'OBEAPP/course_form.html',context)
def markasdone(request,pk):
    course = AssignCourse.objects.get(id=pk)
    form = AssignCourseForm(instance=course)
    if request.method == 'POST':
        form = AssignCourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teacher_page',))
    context = {'form': form}
    return render(request, 'OBEAPP/course_form.html', context)

def resultdone(request,pk):
    semester = AssignSemester.objects.get(id=pk)
    form = AssignSemesterForm(instance=semester)
    if request.method == 'POST':
        form = AssignSemesterForm(request.POST,instance=semester)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('assigncourse',args=(semester.id,)))
    context = {'form':form}
    return render(request,'OBEAPP/course_form.html',context)
def viewresult(request,pk):
    semester = AssignSemester.objects.get(id=pk)
    students = semester.assignstudent_set.all()
    student_cnt = students.count()
    context = {'semester': semester,'students': students,'student_cnt':student_cnt}
    return render(request, 'OBEAPP/view_result.html', context)

def individualResult(request,pk):
    student = AssignStudent.objects.get(id=pk)
    #obestudent = ObeMark.objects.get(student = student)
    courses = student.obemark_set.all()
    noncourses = student.nonobemark_set.all()
    sum = 0.0
    total_hr=0.0
    for course in courses:
        tmp = 0.0
        tmp+= course.co1+course.co2+course.co3+course.co4+course.co5
        tt=0.0
        tt=(course.tt1+course.tt2+course.tt3)/3
        tt+=course.att
        tmp+=tt

        pt=0
        if(tmp>=80):
            pt=4
        elif tmp>=75:
            pt=3.75
        elif tmp>=70:
            pt=3.50
        elif tmp>=65:
            pt=3.25
        elif tmp>=60:
            pt=3.00
        elif tmp>=55:
            pt=2.75
        elif tmp>=50:
            pt=2.50
        elif tmp>=45:
            pt=2.25
        elif tmp>=40:
            pt=2.00
        else:
            pt=0.0
        sum+=(pt*course.course.course.credit)
        total_hr+=course.course.course.credit
    
    for course in noncourses:
        tmp = 0.0
        tmp+= course.sem
        tt=0.0
        tt=(course.tt1+course.tt2+course.tt3)/3
        tt+=course.att
        tmp+=tt

        pt=0
        if(tmp>=80):
            pt=4
        elif tmp>=75:
            pt=3.75
        elif tmp>=70:
            pt=3.50
        elif tmp>=65:
            pt=3.25
        elif tmp>=60:
            pt=3.00
        elif tmp>=55:
            pt=2.75
        elif tmp>=50:
            pt=2.50
        elif tmp>=45:
            pt=2.25
        elif tmp>=40:
            pt=2.00
        else:
            pt=0.0
        sum+=(pt*course.course.course.credit)
        total_hr+=course.course.course.credit
    sum=sum/total_hr
    sum=round(sum,2)


    context = {'student':student,'courses':courses,'noncourses':noncourses,'sum':sum}
    return render(request,'OBEAPP/individual_result.html',context)
def update_assigncourse(request,pk):
    course = AssignCourse.objects.get(id=pk)
    form = CourseForm(instance=course)
    if request.method=='POST':
        form = CourseForm(request.POST,instance=course)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('assigncourse', args=(course.semester.id,)))
    context = {'form':form}
    return render(request,'OBEAPP/course_form.html',context)

def delete_assigncourse(request,pk):
    course = AssignCourse.objects.get(id=pk)

    if request.method=='POST':
       course.delete()
       return HttpResponseRedirect(reverse('assigncourse', args=(course.semester.id,)))
    context = {'item':course}
    return render(request,'OBEAPP/delete_course.html',context)

def add_assignsemester(request,pk4):
    session = AssignSession.objects.get(id=pk4)
    form = SemesterForm(initial={'session':session})
    if request.method=='POST':
        form = SemesterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('assignsemester', args=(pk4,)))
    context = {'form':form}
    return render(request,'OBEAPP/course_form.html',context)

def update_assignsemester(request,pk):
    semester = AssignSemester.objects.get(id=pk)
    form = SemesterForm(instance=semester)
    if request.method=='POST':
        form = SemesterForm(request.POST,instance=semester)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('assignsemester', args=(semester.session.id,)))
    context = {'form':form}
    return render(request,'OBEAPP/course_form.html',context)


def delete_assignsemester(request,pk):
    semester = AssignSemester.objects.get(id=pk)

    if request.method=='POST':
       semester.delete()
       return HttpResponseRedirect(reverse('assignsemester', args=(semester.session.id,)))
    context = {'item':semester}
    return render(request,'OBEAPP/delete_course.html',context)


def add_assignsession(request,pk4):
    department = Department.objects.get(id=pk4)
    form = SessionForm(initial={'department':department})
    if request.method=='POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('assignsession', args=(pk4,)))
    context = {'form':form}
    return render(request,'OBEAPP/course_form.html',context)

def update_assignsession(request,pk):
    session = AssignSession.objects.get(id=pk)
    form = SessionForm(instance=session)
    if request.method=='POST':
        form = SessionForm(request.POST,instance=session)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('assignsession', args=(session.department.id,)))
    context = {'form':form}
    return render(request,'OBEAPP/course_form.html',context)

def delete_assignsession(request,pk):
    session = AssignSession.objects.get(id=pk)

    if request.method=='POST':
       session.delete()
       return HttpResponseRedirect(reverse('assignsession', args=(session.department.id,)))
    context = {'item':session}
    return render(request,'OBEAPP/delete_session.html',context)

def add_department(request):

    form = DepartmentForm()
    if request.method=='POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('department'))
    context = {'form':form}
    return render(request,'OBEAPP/course_form.html',context)

def update_department(request,pk):
    department = Department.objects.get(id=pk)
    form = DepartmentForm(instance=department)
    if request.method=='POST':
        form = DepartmentForm(request.POST,instance=department)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('department'))
    context = {'form':form}
    return render(request,'OBEAPP/course_form.html',context)

def delete_department(request,pk):
    department = Department.objects.get(id=pk)

    if request.method=='POST':
       department.delete()
       return HttpResponseRedirect(reverse('department'))
    context = {'item':department}
    return render(request,'OBEAPP/delete_department.html',context)

def assign_chairman(request,pk):
    department = Department.objects.get(id=pk)
    try:
        chairman = department.assignchairman_set.all()[0]
        form = AssignChairmanForm(instance=chairman)
        
    except:
        form = AssignChairmanForm(initial={'department':department})
   
    if request.method=='POST':
        form = AssignChairmanForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('department'))
    context = {'form':form}
    return render(request,'OBEAPP/course_form.html',context)

def assign_teacher(request,pk):
    course = AssignCourse.objects.get(id=pk)
    try:
        teacher = course.assignteacher_set.all()[0]
        form = AssignTeacherForm(instance=teacher)
        
    except:
        form = AssignTeacherForm(initial={'course':course})
   
    if request.method=='POST':
        form = AssignTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('department'))
    context = {'form':form}
    return render(request,'OBEAPP/course_form.html',context)

def non_obemark(request,pk):
    course= AssignCourse.objects.get(id=pk)
    students = NonObeMark.objects.filter(course = course)

    context={'students':students,'course':course}
    return render(request,'OBEAPP/nonobemark.html',context)
def obemark(request,pk):
    course= AssignCourse.objects.get(id=pk)
    students = ObeMark.objects.filter(course = course)

    context={'students':students,'course':course}
    return render(request,'OBEAPP/obemark.html',context)

def co_graph(request,pk):
    course = AssignCourse.objects.get(id=pk)

    # Fetch internal and external assessments
    internal_objs = ObeMark.objects.filter(course=course)
    external_objs = ObeSem.objects.filter(course=course)

    ara = [0, 0, 0, 0, 0]  # Stores total attainment scores for CO1-CO5
    cnt = max(internal_objs.count(), external_objs.count())  # Total students considered

    # Processing Internal Assessments (40%)
    for ob in internal_objs:
        for i in range(5):
            co_value = getattr(ob, f"co{i+1}", 0)  # Fetch co1, co2,... dynamically
            percentage = (co_value * 100) / 12.0  # Assuming 12 is full marks for each CO

            if percentage >= 70:
                ara[i] += 3 * 0.4  # 40% weightage
            elif 60 <= percentage < 70:
                ara[i] += 2 * 0.4
            elif 50 <= percentage < 60:
                ara[i] += 1 * 0.4

    # Processing External Assessments (60%)
    for ob in external_objs:
        for i in range(5):
            co_value = getattr(ob, f"co{i+1}", 0)  # Fetch co1, co2,... dynamically
            percentage = (co_value * 100) / 12.0  

            if percentage >= 70:
                ara[i] += 3 * 0.6  # 60% weightage
            elif 60 <= percentage < 70:
                ara[i] += 2 * 0.6
            elif 50 <= percentage < 60:
                ara[i] += 1 * 0.6

    context = {'ara': ara, 'course': course, 'cnt': cnt}
    return render(request, 'OBEAPP/co_graph.html', context)


def resultOptionPage(request,pk):
    course = AssignCourse.objects.get(id=pk)

    context={'course':course}
    return render(request, 'OBEAPP/result_option_page.html', context)


def ass_nonobemark(request,pk):
    #student = AssignStudent.objects.get(id = pk)
    nonobj = NonObeMark.objects.get(id=pk)
    form = NonObeForm(instance=nonobj)
    if request.method=='POST':
        form = NonObeForm(request.POST,instance=nonobj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('nonobemark',args=(nonobj.course.id,)))
    context = {'form':form}
    return render(request,'OBEAPP/course_form.html',context)
def ass_obemark(request,pk):
    #student = AssignStudent.objects.get(id = pk)
    obj = ObeMark.objects.get(id=pk)
    form = ObeForm(instance=obj)
    if request.method=='POST':
        form = ObeForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('obemark',args=(obj.course.id,)))
    context = {'form':form}
    return render(request,'OBEAPP/course_form.html',context)

def show_nonobemarks(request,pk):
    course= AssignCourse.objects.get(id=pk)
    nonobj = NonObeMark.objects.filter(course=course)
    context = {'nonobj':nonobj,'course':course}
    return render(request,'OBEAPP/show_nonobemark.html',context)


from .models import AssignCourse, ObeMark, ObeSem, Student

def show_obemarks(request, pk):
    course = AssignCourse.objects.get(id=pk)  # Get AssignCourse instance
    obemark_entries = ObeMark.objects.filter(course=course)  # Internal assessment
    obesem_entries = ObeSem.objects.filter(course=course)  # Semester marks

    # Map Semester marks to students using Student ID
    sem_marks_dict = {obesem.student.id: obesem for obesem in obesem_entries}

    student_data = []  # List to store formatted student marks

    for obemark in obemark_entries:
        assign_student = obemark.student  # Get AssignStudent instance
        student = assign_student.student  # Get Student instance
        sem_marks_obj = sem_marks_dict.get(assign_student.id)  # Get sem marks object if available

        # Prepare CO marks for Internal and External
        co_marks = {
            'CO1': {'Internal': obemark.co1 or 0, 'External': sem_marks_obj.co1 if sem_marks_obj else 0},
            'CO2': {'Internal': obemark.co2 or 0, 'External': sem_marks_obj.co2 if sem_marks_obj else 0},
            'CO3': {'Internal': obemark.co3 or 0, 'External': sem_marks_obj.co3 if sem_marks_obj else 0},
            'CO4': {'Internal': obemark.co4 or 0, 'External': sem_marks_obj.co4 if sem_marks_obj else 0},
            'CO5': {'Internal': obemark.co5 or 0, 'External': sem_marks_obj.co5 if sem_marks_obj else 0},
        }

        student_data.append({
            'reg_no': student.registration_no,  # ✅ Student registration number
            'name': student.name,  # ✅ Student name
            'Q1': obemark.Q1 or 0,
            'Q2': obemark.Q2 or 0,
            'Q3': obemark.Q3 or 0,
            'Q4': obemark.Q4 or 0,
            'Q5': obemark.Q5 or 0,
            'Assignment1': obemark.Assignment1 or 0,
            'Assignment2': obemark.Assignment2 or 0,
            'Mid': obemark.Mid or 0,
            'Sem': sem_marks_obj.sem if sem_marks_obj else 0,  # ✅ External marks
            'CO_Marks': co_marks  # ✅ CO wise marks matrix
        })

    context = {'student_data': student_data, 'course': course}
    return render(request, 'OBEAPP/show_obemark.html', context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher','chairman'])

def teacher_page(request):
    courses = request.user.teacher.assignteacher_set.all()
    course_cnt = courses.count

    context = {'courses':courses,'course_cnt':course_cnt}
    return render(request,'OBEAPP/teacher_page.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles='student')

def student_page(request):
    semesters = request.user.student.assignstudent_set.all()

    context = {'semesters':semesters}
    return render(request, 'OBEAPP/student_page.html',context)
@login_required(login_url='login')

def chairman_page(request):
    department = request.user.teacher.assignchairman_set.all()
    courses = request.user.teacher.assignteacher_set.all()
    course_cnt = courses.count
    context ={'department':department,'courses':courses,'course_cnt':course_cnt}
    return render(request, 'OBEAPP/chairman.html',context)

@login_required(login_url='login')
def render_pdf_view(request,pk):
    template_path = 'OBEAPP/pdf1.html'
    #context = {'myvar': 'this is your template context'}
    student = AssignStudent.objects.get(id=pk)
    #obestudent = ObeMark.objects.get(student = student)
    courses = student.obemark_set.all()
    noncourses=student.nonobemark_set.all()
    sum = 0.0
    total_hr=0.0
    for course in courses:
        tmp = 0.0
        tmp+= course.co1+course.co2+course.co3+course.co4+course.co5
        tt=0.0
        tt=(course.tt1+course.tt2+course.tt3)/3
        tt+=course.att
        tmp+=tt

        pt=0
        if(tmp>=80):
            pt=4
        elif tmp>=75:
            pt=3.75
        elif tmp>=70:
            pt=3.50
        elif tmp>=65:
            pt=3.25
        elif tmp>=60:
            pt=3.00
        elif tmp>=55:
            pt=2.75
        elif tmp>=50:
            pt=2.50
        elif tmp>=45:
            pt=2.25
        elif tmp>=40:
            pt=2.00
        else:
            pt=0.0
        sum+=(pt*course.course.course.credit)
        total_hr+=course.course.course.credit
    for course in noncourses:
        tmp = 0.0
        tmp+= course.sem
        tt=0.0
        tt=(course.tt1+course.tt2+course.tt3)/3
        tt+=course.att
        tmp+=tt

        pt=0
        if(tmp>=80):
            pt=4
        elif tmp>=75:
            pt=3.75
        elif tmp>=70:
            pt=3.50
        elif tmp>=65:
            pt=3.25
        elif tmp>=60:
            pt=3.00
        elif tmp>=55:
            pt=2.75
        elif tmp>=50:
            pt=2.50
        elif tmp>=45:
            pt=2.25
        elif tmp>=40:
            pt=2.00
        else:
            pt=0.0
        sum+=(pt*course.course.course.credit)
        total_hr+=course.course.course.credit

    sum=sum/total_hr
    sum=round(sum,2)




    context = {'student':student,'courses':courses,'sum':sum,'noncourses':noncourses}

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #if want to download
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# @login_required(login_url='login')
# @allowed_users(allowed_roles=['teacher', 'admin'])
def co_po_matrix(request, pk):
    try:
        assign_course = AssignCourse.objects.get(id=pk)  # ✅ Get AssignCourse instance
        course = assign_course.course  # ✅ Get the actual Course instance
    except AssignCourse.DoesNotExist:
        return HttpResponse("Course not found", status=404)

    cos = ['CO1', 'CO2', 'CO3', 'CO4', 'CO5']
    pos = ['PO1', 'PO2', 'PO3', 'PO4', 'PO5', 'PO6', 'PO7', 'PO8', 'PO9', 'PO10', 'PO11', 'PO12']
    strength_choices = {1: "Low", 2: "Medium", 3: "High"}  # Dropdown choices

    # **Retrieve existing mappings**
    mappings = CO_PO_Matrix.objects.filter(course=course)
    mapping_dict = {(m.co_code, m.po_code): m for m in mappings}  # Store entire object

    if request.method == 'POST':
        for co in cos:
            for po in pos:
                strength = request.POST.get(f"{co}_{po}")

                if strength and strength in ['1', '2', '3']:  # ✅ Allow only valid choices
                    strength = int(strength)

                    if (co, po) in mapping_dict:
                        # **Update existing mapping**
                        mapping = mapping_dict[(co, po)]
                        mapping.strength = strength
                        mapping.save()
                    else:
                        # **Create new mapping**
                        CO_PO_Matrix.objects.create(course=course, co_code=co, po_code=po, strength=strength)

         # **Redirect to teacher_page/assigncourse/resultoptionpage/<str:pk>/**
        return redirect(reverse('resultoptionpage', kwargs={'pk': pk}))

    # **Convert matrix to a list of tuples (co_code, po_code, strength)**
    matrix = []
    for co in cos:
        row = []
        for po in pos:
            row.append((co, po, mapping_dict.get((co, po), None).strength if (co, po) in mapping_dict else None))
        matrix.append(row)

    context = {
        'course': assign_course,  # ✅ Keep AssignCourse for display
        'cos': cos,
        'pos': pos,
        'matrix': matrix,  # ✅ Now matrix is a list of tuples
        'strength_choices': strength_choices  # ✅ Pass dropdown options to the template
    }
    return render(request, 'OBEAPP/copomatrix.html', context)
import matplotlib.pyplot as plt
import numpy as np
import io
import urllib
import base64
from django.shortcuts import render
from .models import AssignCourse, CO_PO_Matrix, ObeMark, ObeSem

def po_graph(request, pk):
    assign_course = AssignCourse.objects.get(id=pk)  # ✅ Get AssignCourse instance
    course = assign_course.course  # ✅ Get actual Course instance

    # Step 1: Calculate CO Attainment (Automatically)
    internal_objs = ObeMark.objects.filter(course=assign_course)
    external_objs = ObeSem.objects.filter(course=assign_course)

    co_attainment = [0, 0, 0, 0, 0]  # CO1 to CO5
    total_students = max(internal_objs.count(), external_objs.count())

    # Internal Assessment (40% weight)
    for ob in internal_objs:
        for i in range(5):
            co_value = getattr(ob, f"co{i+1}", 0)
            percentage = (co_value * 100) / 12.0

            if percentage >= 70:
                co_attainment[i] += 3 * 0.4
            elif 60 <= percentage < 70:
                co_attainment[i] += 2 * 0.4
            elif 50 <= percentage < 60:
                co_attainment[i] += 1 * 0.4

    # External Assessment (60% weight)
    for ob in external_objs:
        for i in range(5):
            co_value = getattr(ob, f"co{i+1}", 0)
            percentage = (co_value * 100) / 12.0

            if percentage >= 70:
                co_attainment[i] += 3 * 0.6
            elif 60 <= percentage < 70:
                co_attainment[i] += 2 * 0.6
            elif 50 <= percentage < 60:
                co_attainment[i] += 1 * 0.6

    # Normalize CO Attainment
    if total_students > 0:
        co_attainment = [round(c / total_students, 2) for c in co_attainment]

    # Step 2: Calculate PO Attainment Using CO-PO Mapping
    mappings = CO_PO_Matrix.objects.filter(course=course)
    po_attainment = {f"PO{i}": 0 for i in range(1, 13)}
    articulation_sums = {f"PO{i}": 0 for i in range(1, 13)}

    # Compute PO Attainment using the correct formula:
    for mapping in mappings:
        po_code = mapping.po_code  # Example: 'PO1', 'PO2', etc.
        co_index = int(mapping.co_code[-1]) - 1  # Convert 'CO1' → 0, 'CO2' → 1, ...
        articulation_value = mapping.strength  # 1 (Low), 2 (Medium), 3 (High)

        po_attainment[po_code] += (co_attainment[co_index] * articulation_value)
        articulation_sums[po_code] += articulation_value  # Sum of articulation values for PO

    # Normalize PO Attainment: PO = (Σ CO * Articulation) / Σ Articulation
    for po, value in po_attainment.items():
        total_articulation = articulation_sums[po]
        po_attainment[po] = round(value / total_articulation, 2) if total_articulation else 0

    # Ensure PO Attainment does not exceed 3
    for po in po_attainment:
        po_attainment[po] = min(po_attainment[po], 3)

    # Step 3: Generate Bar Graph
    po_labels = list(po_attainment.keys())
    po_values = list(po_attainment.values())

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(po_labels, po_values, color='skyblue')
    ax.set_xlabel("Program Outcomes (POs)")
    ax.set_ylabel("Attainment Level")
    ax.set_title(f"PO Attainment Graph for {course.course_name}")
    ax.set_ylim(0, 3)

    # Convert Graph to Image URL
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    string = urllib.parse.quote(base64.b64encode(buf.read()))
    image_url = f"data:image/png;base64,{string}"

    context = {
        'course': assign_course,  # ✅ Use AssignCourse for display
        'po_attainment': po_attainment,
        'image_url': image_url
    }
    return render(request, 'OBEAPP/po_graph.html', context)
