from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

# Create your models here.

from django.db import models

class CO_PO_Matrix(models.Model):
    """
    Represents the mapping between Course Outcomes (COs) and Program Outcomes (POs).
    """
    course = models.ForeignKey('Course', on_delete=models.CASCADE)  # Foreign key to the Course table
    co_code = models.CharField(max_length=10, choices=[  # CO code constraint
        ('CO1', 'CO1'),
        ('CO2', 'CO2'),
        ('CO3', 'CO3'),
        ('CO4', 'CO4'),
        ('CO5', 'CO5'),
    ])
    po_code = models.CharField(max_length=10, choices=[  # PO code constraint
        ('PO1', 'PO1'),
        ('PO2', 'PO2'),
        ('PO3', 'PO3'),
        ('PO4', 'PO4'),
        ('PO5', 'PO5'),
        ('PO6', 'PO6'),
        ('PO7', 'PO7'),
        ('PO8', 'PO8'),
        ('PO9', 'PO9'),
        ('PO10', 'PO10'),
        ('PO11', 'PO11'),
        ('PO12', 'PO12'),
    ])
    strength = models.IntegerField(choices=[  # Strength constraint
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ])

    def __str__(self):
        return f"{self.course.course_code} - {self.co_code} -> {self.po_code} (Strength: {self.strength})"

class Faculty(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Department(models.Model):

    name = models.CharField(max_length=200, null=True)
    faculty_name = models.ForeignKey(
        Faculty, max_length=200, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    registration_no = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    # department = models.CharField(max_length=200, null=True)
    department = models.ForeignKey(
        Department, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        null=True, default="propic1.jpg", blank=True)

    def __str__(self):
        # return "%s %s %s %s" % (self.registration_no, self.name,self.email,self.department)
        return self.name


class Teacher(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    STATUS = [
        ('Active', 'Active'),
        ('LPR', 'LPR'),
        ('Leave', 'Leave'),
        ('Retired', 'Retired')
    ]
    # registration_no = models.CharField(max_length=20,null=True)
    name = models.CharField(max_length=200, null=True)
    designation = models.CharField(max_length=200, null=True)
    # department = models.CharField(max_length=200, null=True)
    department = models.ForeignKey(
        Department, null=True, on_delete=models.CASCADE)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=11, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    profile_pic = models.ImageField(
        null=True, default="propic1.jpg", blank=True)

    def __str__(self):
        return self.name


class Session(models.Model):
    STATUS = [
        ('Running', 'Running'),
        ('Finished', 'Finished'),
    ]
    # registration_no = models.CharField(max_length=20,null=True)
    startYear = models.CharField(max_length=200, null=True)
    endYear = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.startYear


class AssignSession(models.Model):
    department = models.ForeignKey(
        Department, null=True, on_delete=models.SET_NULL)
    session = models.ForeignKey(Session, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "%s %s" % (self.department, self.session)


class Semester(models.Model):
    STATUS = [
        ('1st Year 1st Semester', '1st Year 1st Semester'),
        ('1st Year 2nd Semester', '1st Year 2nd Semester'),
        ('2nd Year 1st Semester', '2nd Year 1st Semester'),
        ('2nd Year 2nd Semester', '2nd Year 2nd Semester'),
        ('3rd Year 1st Semester', '3rd Year 1st Semester'),
        ('3rd Year 2nd Semester', '3rd Year 2nd Semester'),
        ('4th Year 1st Semester', '4th Year 1st Semester'),
        ('4th Year 2nd Semester', '4th Year 2nd Semester'),

    ]

    semester = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.semester


class AssignSemester(models.Model):
    session = models.ForeignKey(
        AssignSession, max_length=300, null=True, on_delete=models.SET_NULL)
    semester = models.ForeignKey(
        Semester, max_length=300, null=True, on_delete=models.SET_NULL)
    result_status = models.CharField(default='PENDING', null=True, max_length=20,
                                     choices=[('PUBLISHED', 'PUBLISHED'), ('PENDING', 'PENDING')])

    def __str__(self):
        return "%s %s" % (self.session, self.semester)


class Course(models.Model):
    STATUS = [
        (1, 1),
        (2, 2),
        (3, 3),

    ]

    TYPE = [
        ('Lab', 'Lab'),
        ('Theory', 'Theory'),
    ]

    course_code = models.CharField(max_length=200, null=True)
    course_name = models.CharField(max_length=200, null=True)
    credit = models.IntegerField(null=True, choices=STATUS)
    course_type = models.CharField(max_length=200, null=True, choices=TYPE)

    def __str__(self):
        return self.course_name


class AssignCourse(models.Model):

    semester = models.ForeignKey(
        AssignSemester, max_length=200, null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey(
        Course, max_length=200, null=True, on_delete=models.SET_NULL)
    format = models.CharField(max_length=200, null=True, choices=[
                              ('OBE', 'OBE'), ('NonOBE', 'NonOBE')])
    completion = models.CharField(default='PENDING', max_length=20, null=True, choices=[
                                  ('ASSIGNED', 'ASSIGNED'), ('PENDING', 'PENDING')])

    def __str__(self):
        return "%s  %s %s" % (self.semester, self.course, self.format)


class AssignStudent(models.Model):
    semester = models.ForeignKey(
        AssignSemester, max_length=200, null=True, on_delete=models.SET_NULL)
    student = models.ForeignKey(
        Student, max_length=200, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "%s  %s" % (self.semester, self.student)


class AssignTeacher(models.Model):
    course = models.ForeignKey(
        AssignCourse, null=True, on_delete=models.SET_NULL)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "%s  %s" % (self.course, self.teacher)


class AssignChairman(models.Model):
    chairman = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL)
    department = models.ForeignKey(
        Department, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "%s  %s" % (self.chairman, self.department)


class AssignExamCommittee(models.Model):
    member = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL)
    semester = models.ForeignKey(
        AssignSemester, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "%s %s" % (self.member, self.semester)


class NonObeMark(models.Model):
    course = models.ForeignKey(
        AssignCourse, null=True, on_delete=models.SET_NULL)
    student = models.ForeignKey(
        AssignStudent, null=True, on_delete=models.SET_NULL)
    # course = models.ForeignKey(AssignCourse,null=True,on_delete=models.SET_NULL)
    tt1 = models.IntegerField(default=-1, null=True)
    tt2 = models.IntegerField(default=-1, null=True)
    tt3 = models.IntegerField(default=-1, null=True)
    att = models.IntegerField(default=-1, null=True)
    sem = models.IntegerField(default=-1, null=True)
    mark = models.CharField(default='PENDING', null=True, max_length=20, choices=[
                            ('ASSIGNED', 'ASSIGNED'), ('PENDING', 'PENDING')])

    def avg(self):
        return (self.tt1+self.tt2+self.tt3)/3

    def total(self):
        tt = self.avg(self)
        return tt+self.att+self.sem

    def __str__(self):
        return "%s %s %d %d %d %d %d" % (self.student.student.name, self.course.course.course_name, self.tt1, self.tt2, self.tt3, self.att, self.sem)


class ObeMark(models.Model):
    student = models.ForeignKey(
        'AssignStudent', null=True, on_delete=models.CASCADE, blank=True)
    course = models.ForeignKey(
        'AssignCourse', null=True, on_delete=models.CASCADE, blank=True)

    Q1 = models.FloatField(null=True, blank=True,
                           validators=[MaxValueValidator(4)])
    Q2 = models.FloatField(null=True, blank=True,
                           validators=[MaxValueValidator(4)])
    Q3 = models.FloatField(null=True, blank=True,
                           validators=[MaxValueValidator(4)])
    Q4 = models.FloatField(null=True, blank=True,
                           validators=[MaxValueValidator(4)])
    Q5 = models.FloatField(null=True, blank=True,
                           validators=[MaxValueValidator(4)])

    Assignment1 = models.FloatField(
        null=True, blank=True, validators=[MaxValueValidator(10)])
    Assignment2 = models.FloatField(
        null=True, blank=True, validators=[MaxValueValidator(10)])

    Mid = models.FloatField(null=True, blank=True, validators=[
                            MaxValueValidator(30)])
    

    co1 = models.FloatField(null=True, blank=True)  # New field
    co2 = models.FloatField(null=True, blank=True)  # New field
    co3 = models.FloatField(null=True, blank=True)  # New field
    co4 = models.FloatField(null=True, blank=True)  # New field
    co5 = models.FloatField(null=True, blank=True)  # New field

    def __str__(self):
        return f"OBEMark {self.id}"



class ObeSem(models.Model):
    sem = models.FloatField(null=True, blank=True)
    co1 = models.FloatField(null=True, blank=True)
    co2 = models.FloatField(null=True, blank=True)
    co3 = models.FloatField(null=True, blank=True)
    co4 = models.FloatField(null=True, blank=True)
    co5 = models.FloatField(null=True, blank=True)
    
    # ForeignKey fields
    course = models.ForeignKey(
        'AssignCourse',  # Replace with the actual model name if different
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='obesem_course'  # Optional: Add a related name for reverse access
    )
    student = models.ForeignKey(
        'AssignStudent',  # Replace with the actual model name if different
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='obesem_student'  # Optional: Add a related name for reverse access
    )

    def __str__(self):
        return f"ObeSem {self.id}"