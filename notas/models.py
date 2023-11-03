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
        return f"{self.name}"


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


class Facultad(models.Model):
    description = models.CharField('Descripcion', max_length=200)
    isactive = models.BooleanField('Estado', default=True)

    class Meta:
        verbose_name = ('Facultad')
        verbose_name_plural = ('Facultades')
        ordering = ('description',)

    def __str__(self):
        return f"{self.description}"


class Carrera(models.Model):
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    description = models.CharField('Descripcion', max_length=200)
    isactive = models.BooleanField('Estado', default=True)

    class Meta:
        verbose_name = ('Carrera')
        verbose_name_plural = ('Carreras')
        ordering = ('description',)

    def __str__(self):
        return f"{self.description}"

# class Asignatura:
#   pass
# class profesor:
#   pass
# class Semestre:
#   pass
# class Notas:
#   pass
#   # guardar user: user = models.ForeignKey(User, on_delete=models.CASCADE)
