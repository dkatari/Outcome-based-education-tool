from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('teacher_page/', views.teacher_page, name='teacher_page'),
    path('student_page/', views.student_page, name='student_page'),
    path('chairman_page/', views.chairman_page, name='chairman_page'),
    path('studentaccount/', views.studentAccount, name='studentaccount'),
    path('teacheraccount/', views.teacherAccount, name='teacheraccount'),
    path('main/', views.main, name='main'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('signup/', views.signupPage, name='signup'),

    path('student/', views.student, name='student'),
    path('student/add/', views.add_student, name='addstudent'),
    path('student/updatestudent/<str:pk>/', views.update_student, name='updatestudent'),
    path('student/deletestudent/<str:pk>/', views.delete_student, name='deletestudent'),

    path('teacher/', views.teacher, name='teacher'),
    path('teacher/add/', views.add_teacher, name='addteacher'),
    path('teacher/updateteacher/<str:pk>/', views.update_teacher, name='updateteacher'),
    path('teacher/deleteteacher/<str:pk>/', views.delete_teacher, name='deleteteacher'),

    path('session/', views.session, name='session'),
    path('semester/', views.semester, name='semester'),
    path('course/', views.course, name='course'),
    path('department/', views.department, name='department'),

    path('faculty/', views.faculty, name='faculty'),
    path('faculty/add/', views.add_faculty, name='addfaculty'),
    path('faculty/updatefaculty/<str:pk>/', views.update_faculty, name='updatefaculty'),
    path('faculty/deletefaculty/<str:pk>/', views.delete_faculty, name='deletefaculty'),

    path('assignchairman/<str:pk>/', views.assign_chairman, name='assignchairman'),
    path('assignteacher/<str:pk>/', views.assign_teacher, name='assignteacher'),
    path('assignstudent/', views.assign_student, name='assignstudent'),
    path('assignchairman/', views.assign_teacher, name='assignchairman'),
    path('assignexamcommittee/', views.assign_teacher, name='assignexamcommittee'),

    path('department/add/', views.add_department, name='adddepartment'),
    path('department/updatedepartment/<str:pk>/', views.update_department, name='updatedepartment'),
    path('department/deletedepartment/<str:pk>/', views.delete_department, name='deletedepartment'),

    path('department/assignsession/<str:pk>/', views.assign_session, name='assignsession'),
    path('department/assignsession/assignsemester/<str:pk2>/', views.assign_semester, name='assignsemester'),
    path('department/assignsession/assignsemester/assigncourse/<str:pk3>/', views.assign_course, name='assigncourse'),

    path('department/addassignsession/<str:pk4>/', views.add_assignsession, name='addassignsession'),
    path('department/assignsession/updateassignsession/<str:pk>/', views.update_assignsession, name='updateassignsession'),
    path('department/assignsession/deleteassignsession/<str:pk>/', views.delete_assignsession, name='deleteassignsession'),

    path('department/assignsession/addassignsemester/<str:pk4>/', views.add_assignsemester, name='addassignsemester'),
    path('department/assignsession/assignsemester/updateassignsemester/<str:pk>/', views.update_assignsemester, name='updateassignsemester'),
    path('department/assignsession/assignsemester/deleteassignsemester/<str:pk>/', views.delete_assignsemester, name='deleteassignsemester'),

    path('department/assignsession/assignsemester/resultdone/<str:pk>/', views.resultdone, name='resultdone'),
    path('department/assignsession/assignsemester/viewresult/<str:pk>/', views.viewresult, name='viewresult'),
    path('department/assignsession/assignsemester/viewresult/individualresult/<str:pk>/', views.individualResult, name='individualresult'),
    path('department/assignsession/assignsemester/viewresult/individualresult/pdf/<str:pk>/', views.render_pdf_view, name='renderpdf'),

    path('department/assignsession/assignsemester/addassigncourse/<str:pk4>/', views.add_assigncourse, name='addassigncourse'),
    path('department/assignsession/assignsemester/assigncourse/updateassigncourse/<str:pk>/', views.update_assigncourse, name='updateassigncourse'),
    path('department/assignsession/assignsemester/assigncourse/deleteassigncourse/<str:pk>/', views.delete_assigncourse, name='deleteassigncourse'),

    path('department/assignsession/assignsemester/assigncourse/resultoptionpage/<str:pk>/', views.resultOptionPage, name='resultoptionpage'),
    path('teacher_page/assigncourse/resultoptionpage/<str:pk>/', views.resultOptionPage, name='resultoptionpage'),
    path('department/assignsession/assignsemester/assigncourse/resultoptionpage/obemark/markasdone/<str:pk>/', views.markasdone, name='markasdone'),

    path('department/assignsession/assignsemester/assigncourse/resultoptionpage/nonobemark/<str:pk>/', views.non_obemark, name='nonobemark'),
    path('department/assignsession/assignsemester/assigncourse/resultoptionpage/obemark/<str:pk>/', views.obemark, name='obemark'),
    path('department/assignsession/assignsemester/assigncourse/resultoptionpage/coattgraph/<str:pk>/', views.co_graph, name='coattgraph'),
    path('department/assignsession/assignsemester/assigncourse/resultoptionpage/copomatrix/<int:pk>/', views.co_po_matrix, name='copomatrix'),
    path('department/assignsession/assignsemester/assigncourse/resultoptionpage/pograph/<int:pk>/', views.po_graph, name='pograph'),


    path('department/assignsession/assignsemester/assigncourse/resultoptionpage/nonobemark/assnonobemark/<str:pk>/', views.ass_nonobemark, name='assnonobemark'),
    path('department/assignsession/assignsemester/assigncourse/resultoptionpage/obemark/assobemark/<str:pk>/', views.ass_obemark, name='assobemark'),

    path('department/assignsession/assignsemester/assigncourse/resultoptionpage/shownonobemark/<str:pk>/', views.show_nonobemarks, name='shownonobemark'),
    path('department/assignsession/assignsemester/assigncourse/resultoptionpage/showobemark/<str:pk>/', views.show_obemarks, name='showobemark'),
]
