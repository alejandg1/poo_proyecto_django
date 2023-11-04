from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/', blank=False, null=False)


class Faculty(models.Model):
    name = models.CharField(verbose_name="name", max_length=200)
    code = models.CharField(verbose_name="code", max_length=20)
    is_active = models.BooleanField(verbose_name="is_active", default=True)

    class Meta:
        verbose_name = ('Faculty')
        verbose_name_plural = ('Faculties')
        ordering = ('name',)

    def __str__(self):
        return f"{self.name} {self.code} {self.is_active}"


class carrer(models.Model):
    codigo_carrera = models.CharField(verbose_name="code", max_length=20)
    nombre = models.CharField(verbose_name="name", max_length=200)
    Facultad = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('carrer')
        verbose_name_plural = ('carrers')
        ordering = ('nombre',)

    def __str__(self):
        return f"{self.nombre}"


class Teacher(models.Model):
    firstname = models.CharField('Nombres', max_length=200)
    lastname = models.CharField(verbose_name="Apellidos", max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('Teacher')
        verbose_name_plural = ('Teachers')
        ordering = ('-lastname',)

    def __str__(self):
        return f"{self.lastname} {self.firstname} -  {self.user.username}"


class Student(models.Model):
    firstname = models.CharField('Nombres', max_length=200)
    lastname = models.CharField(verbose_name="Apellidos", max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    dategraduate = models.DateTimeField(
        'Fecha Graduacion', null=True, blank=True)
    graduate = models.BooleanField('Graduado', default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('Estudiante')
        verbose_name_plural = ('Estudiantes')
        ordering = ('-lastname',)

    def __str__(self):
        return f"{self.lastname} {self.firstname} -  {self.user.username}"


class Subject(models.Model):
    name = models.CharField(verbose_name="name", max_length=200)
    code = models.CharField(verbose_name="code", max_length=20)
    is_active = models.BooleanField(verbose_name="is_active", default=True)
    teacher = models.ManyToManyField(Teacher, through='teacher_subject')


class teacher_subject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


class Notas(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    n1 = models.IntegerField('n1', default=0)
    n2 = models.IntegerField('n2', default=0)
    n3 = models.IntegerField('n3', default=0)
    n4 = models.IntegerField('n4', default=0)
    ex1 = models.IntegerField('ex1', default=0)
    ex2 = models.IntegerField('ex2', default=0)
    p1 = models.IntegerField('p1', default=0)
    p2 = models.IntegerField('p2', default=0)
    final = models.IntegerField('final', default=0)
    fecha = models.DateTimeField(auto_now_add=True)


class paralell(models.Model):
    name = models.CharField(verbose_name="name", max_length=200)
    code = models.CharField(verbose_name="code", max_length=20)
    is_active = models.BooleanField(verbose_name="is_active", default=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student, through='matricula')


class matricula(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    paralell = models.ForeignKey(paralell, on_delete=models.CASCADE)

# class Asignatura:
#   pass
# class profesor:
#   pass
# class Semestre:
#   pass
# class Notas:
#   pass
#   # guardar user: user = models.ForeignKey(User, on_delete=models.CASCADE)
