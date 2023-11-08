from django.forms import ModelForm
from .models import Student, Faculty, UserProfile, Teacher, Carrer, Subject


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
        fields = ['name', 'code']


class CarrerForm(ModelForm):
    class Meta:
        model = Carrer
        fields = ['nombre', 'codigo_carrera', 'Facultad', 'materias']
