from django.forms import ModelForm
from .models import Student, Faculty, UserProfile, Teacher


class profileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['photo']


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'graduate', 'photo']


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['firstname', 'lastname', 'photo']


class FacultadForm(ModelForm):
    class Meta:
        model = Faculty
        fields = ['name', 'code']
