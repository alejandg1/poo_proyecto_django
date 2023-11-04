
from django.urls import path
from . import teacher
from . import student
from . import facultad
from . import views
urlpatterns = [
    path('', views.home, name='home'),

    path('students/', student.init, name='students'),
    path('students/create/', student.create_student, name='create_student'),
    path('students/<int:id>/', student.detail_student, name='detail_student'),
    path('students/update/<int:id>/',
         student.update_student, name='update_student'),
    path('students/delete/<int:id>/',
         student.delete_student, name='delete_student'),

    path('teachers/', teacher.init, name='teachers'),
    path('teachers/create/', teacher.create_teacher, name='create_teacher'),
    path('teachers/update/<int:id>/',
         teacher.update_teacher, name='update_teacher'),
    path('teachers/delete/<int:id>/',
         teacher.delete_teacher, name='delete_teacher'),

    path('faculty/', facultad.init, name='faculty'),
    path('faculty/create/', facultad.create_faculty, name='create_faculty'),
    path('faculty/update/<int:id>/',
         facultad.update_faculty, name='update_faculty'),
    path('faculty/delete/<int:id>/',
         facultad.delete_faculty, name='delete_faculty'),

    path('register/', views.register, name='register'),
    path('login/', views.iniciarSesion, name='login'),
    path('logout/', views.cerrarSesion, name='logout'),
]
