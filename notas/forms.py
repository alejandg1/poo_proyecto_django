from django.forms import ModelForm
from .models import Student, Facultad, UserProfile, Teacher, custom_user


class profileForm(ModelForm):
    class Meta:
        model = custom_user
        fields = ['username', 'password', 'photo']


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'graduate']


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['firstname', 'lastname']


class FacultadForm(ModelForm):
    class Meta:
        model = Facultad
        fields = ['description', 'isactive']
