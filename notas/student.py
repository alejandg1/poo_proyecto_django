
from datetime import datetime
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required
def init(request):
    print(request)
    context, students = None, None
    try:
        q = request.GET.get('q')  # ver
        if q:
            students = (Student.objects.filter(
                user=request.user, lastname__icontains=q) or
                Student.objects.filter
                (user=request.user, firstname__icontains=q))
        else:
            students = Student.objects.filter(user=request.user)
            # #  select * from Student  where user=1
        # Crea un paginador con los estudiantes
        paginator = Paginator(students, 2)
        # Obtén el número de página actual
        pagina = request.GET.get('page', 1)
        # Obtén los libros de la página actual
        students_paginados = paginator.get_page(pagina)
        # Envía el paginador con los estudiantes
        # y el número de páginas al contexto
        context = {
            'students': students_paginados,
            'title': 'Consulta de Estudiantes',
            'paginator': paginator,
            'num_pages': paginator.num_pages,
        }

        return render(request, 'students/students.html', context)
    except NameError:
        print(NameError)
        return render(request, 'students/students.html',
                      {'title': 'Consulta de Estudiantes',
                       'error': 'Ha ocurrido un error en la consulta'})


@login_required
def create_student(request):
    form = None
    if request.method == "GET":
        context = {'title': 'Registro de Estudiante',
                   'form': StudentForm, 'error': ''}
        return render(request, 'students/create_student.html', context)
    else:
        try:
            form = StudentForm(request.POST)
            if form.is_valid():
                student = form.save(commit=False)  # lo tiene en memoria
                student.user = request.user
                student.save()  # lo guarda en la BD
                return redirect('students')
            else:
                return render(request,
                              'students/create_student.html',
                              {"form": form,
                               "error": "Error de datos invalidos."})
        except:
            return render(request,
                          'students/create_student.html',
                          {"form": form,
                           "error": "Error al Crear Registro de Estudiante."})


@login_required
def detail_student(request, id):
    student = None
    try:
        student = Student.objects.get(user=request.user, pk=id)
        # select * from stident where user="admin" and id=2
        student.graduate = True
        student.dategraduate = datetime.now()
        student.save()
        return redirect('students')
    except:
        context = {'title': 'Datos del Estudiante', 'student': student,
                   'error': 'Error al seleccionar  estudiante'}
        return render(request, 'students/detail_student.html', context)


@login_required
def update_student(request, id):
    student = Student.objects.filter(user=request.user, pk=id).first()
    form = None
    print(student)
    if request.method == "GET":
        form = StudentForm(instance=student)
        context = {'title': 'Editar Estudiante', 'form': form, 'error': ''}
        return render(request, 'students/create_student.html', context)
    else:
        try:
            form = StudentForm(request.POST, instance=student)
            if form.is_valid():
                form.save()
                return redirect('students')
            else:
                return render(request, 'students/create_student.html',
                              {"form": form,
                               "error": "Error de datos invalidos."})
        except:
            return render(request, 'students/create_student.html',
                          {"form": form,
                           "error": "Error al actualizar registro de Estudiante."})


@login_required
def delete_student(request, id):
    student = None
    try:
        student = Student.objects.get(user=request.user, pk=id)
        if request.method == "GET":
            context = {'title': 'Estudiante a Eliminar',
                       'student': student, 'error': ''}
            return render(request, 'students/delete_student.html', context)
        else:
            student.delete()
            return redirect('students')
    except:
        context = {'title': 'Datos del Estudiante',
                   'student': student, 'error': 'Error al eliminar estudiante'}
        return render(request, 'students/delete_student.html', context)
