
from django.urls import path
from . import facultad, carrer, teacher, student, views, subjects, enroll
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

    path('carrer/', carrer.init, name='carrers'),
    path('carrer/create/', carrer.create_carrer, name='create_carrer'),
    path('carrer/update/<int:id>/',
         carrer.update_carrer, name='update_carrer'),
    path('carrer/delete/<int:id>/',
         carrer.delete_carrer, name='delete_carrer'),

    path('enroll/', enroll.init, name='enroll'),
    path('enroll/create/', enroll.create_enroll, name='create_enroll'),
    path('enroll/update/<int:id>/',
         enroll.update_enroll, name='update_enroll'),
    path('enroll/delete/<int:id>/',
         enroll.delete_enrroll, name='delete_enroll'),

    path('subject/', subjects.init, name='subjects'),
    path('subject/create/', subjects.create_subject, name='create_subject'),
    path('subject/update/<int:id>/',
         subjects.update_subject, name='update_subject'),
    path('subject/delete/<int:id>/',
         subjects.delete_subject, name='delete_subject'),

    path('register/', views.register, name='register'),
    path('login/', views.iniciarSesion, name='login'),
    path('logout/', views.cerrarSesion, name='logout'),
]
