from django.forms import ModelForm
from .models import Student, Facultad, UserProfile, Teacher


class profileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['photo']


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
