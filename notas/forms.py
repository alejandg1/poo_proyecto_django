from django.forms import ModelForm
from .models import Student, Faculty, enrollment, UserProfile, Teacher, Carrer, Subject, calification


class profileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['photo']


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'graduate', 'carrera', 'photo']


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['firstname', 'lastname', 'photo']


class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        fields = ['name', 'code']


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'code', 'semestre']


class CarrerForm(ModelForm):
    class Meta:
        model = Carrer
        fields = ['nombre', 'codigo_carrera', 'Facultad', 'materias']


class Enrollform(ModelForm):
    class Meta:
        model = enrollment
        fields = ['student', 'subject', 'teacher', 'paralell']


class calificationForm(ModelForm):
    class Meta:
        mode = calification
        fields = ['enroll', 'n1', 'n2', 'ex1', 'n3', 'n4', 'ex2', 're']
