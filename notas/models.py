from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to='notas_userPhoto', blank=True, null=True)

    def __str__(self):
        return self.user


class Faculty(models.Model):
    name = models.CharField(verbose_name="name", max_length=200)
    code = models.CharField(verbose_name="code", max_length=20)
    is_active = models.BooleanField(verbose_name="is_active", default=True)

    class Meta:
        verbose_name = ('Faculty')
        verbose_name_plural = ('Faculties')
        ordering = ('name',)

    def __str__(self):
        return f"{self.name}"


class Subject(models.Model):
    name = models.CharField(verbose_name="name", max_length=200)
    code = models.CharField(verbose_name="code", max_length=20)
    semestre = models.IntegerField('semestre', default=1)
    is_active = models.BooleanField(verbose_name="is_active", default=True)

    def __str__(self):
        return f"{self.name, self.code}"


class Carrer(models.Model):
    codigo_carrera = models.CharField(verbose_name="code", max_length=20)
    nombre = models.CharField(verbose_name="name", max_length=200)
    Facultad = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    materias = models.ManyToManyField(Subject)

    class Meta:
        verbose_name = ('carrer')
        verbose_name_plural = ('carrers')
        ordering = ('nombre',)

    def __str__(self):
        return f"{self.nombre, self.codigo_carrera}"


class Student(models.Model):
    firstname = models.CharField(
        'Nombres', max_length=200, null=False, blank=False)
    lastname = models.CharField(
        verbose_name="Apellidos", max_length=200, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    dategraduate = models.DateTimeField(
        'Fecha Graduacion', null=True, blank=True)
    graduate = models.BooleanField('Graduado', default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrer, default=None, on_delete=models.PROTECT)
    photo = models.ImageField(
        upload_to='notas_studentPhoto', blank=True, null=True)

    class Meta:
        verbose_name = ('Estudiante')
        verbose_name_plural = ('Estudiantes')
        ordering = ('-lastname',)

    def __str__(self):
        return f"{self.lastname} {self.firstname} -  {self.user.username}"


class Teacher(models.Model):
    firstname = models.CharField('Nombres', max_length=200)
    lastname = models.CharField(verbose_name="Apellidos", max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(
        upload_to='notas_teacherPhoto', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('Teacher')
        verbose_name_plural = ('Teachers')
        ordering = ('-lastname',)

    def __str__(self):
        return f"{self.lastname} {self.firstname} -  {self.user.username}"


class Paralell(models.Model):
    name = models.CharField(verbose_name="name", max_length=200)
    code = models.CharField(verbose_name="code", max_length=20)
    is_active = models.BooleanField(verbose_name="is_active", default=True)


class enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now_add=True)
    paralell = models.ForeignKey(Paralell, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.student, self.subject, self.teacher}"


class calification(models.Model):
    n1 = models.IntegerField('n1', default=0)
    n2 = models.IntegerField('n2', default=0)
    n3 = models.IntegerField('n3', default=0)
    n4 = models.IntegerField('n4', default=0)
    ex1 = models.IntegerField('ex1', default=0)
    ex2 = models.IntegerField('ex2', default=0)
    p1 = models.IntegerField('p1', default=0)
    p2 = models.IntegerField('p2', default=0)
    re = models.IntegerField('re', default=0)
    final = models.IntegerField('final', default=0)
    enroll = models.OneToOneField(enrollment, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.p1, self.p2, self.final, self.enroll.__str__()}"
