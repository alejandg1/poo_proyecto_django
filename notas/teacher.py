from .forms import TeacherForm
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Teacher
from django.contrib.auth.decorators import login_required


@login_required
def init(request):
    context, teachers = None, None
    try:
        q = request.GET.get('q')  # ver
        if q:
            teachers = (Teacher.objects.filter(
                lastname__icontains=q) or
                Teacher.objects.filter
                (firstname__icontains=q))
        else:
            teachers = Teacher.objects.all()
        # Crea un paginador con los estudiantes
        paginator = Paginator(teachers, 2)
        print(teachers)
        # Obtén el número de página actual
        pagina = request.GET.get('page', 1)
        # Obtén los libros de la página actual
        teachers_paginados = paginator.get_page(pagina)
        # Envía el paginador con los estudiantes
        # y el número de páginas al contexto
        context = {
            'teachers': teachers_paginados,
            'title': 'Consulta de profesores',
            'paginator': paginator,
            'num_pages': paginator.num_pages,
        }
        return render(request, 'teachers/teachers.html', context)
    except NameError:
        print(NameError)
        return render(request, 'teachers/teachers.html',
                      {'title': 'Consulta de profesores',
                       'error': 'Ha ocurrido un error en la consulta'})


@login_required
def create_teacher(request):
    form = None
    if request.method == "GET":
        context = {'title': 'Registro de Docente',
                   'form': TeacherForm, 'error': ''}
        return render(request, 'teachers/create_teacher.html', context)
    else:
        try:
            form = TeacherForm(request.POST)
            print(form)
            print(request.POST)
            print(request.user)
            if form.is_valid():
                teacher = form.save(commit=False)  # lo tiene en memoria
                teacher.user = request.user
                teacher.save()  # lo guarda en la BD
                return redirect('teachers')
            else:
                return render(request,
                              'teachers/create_teacher.html',
                              {"form": form,
                               "error": "Error de datos invalidos."})
        except NameError:
            print(NameError)
            return render(request,
                          'teachers/create_teacher.html',
                          {"form": form,
                           "error": "Error al Crear Registro de Docente."})
#
#
# @login_required
# def detail_teacher(request, id):
#     teacher = None
#     try:
#         teacher = Teacher.objects.get(user=request.user, pk=id)
#         # select * from stident where user="admin" and id=2
#         teacher.save()
#         return redirect('teachers')
#     except NameError:
#         print(NameError)
#         context = {'title': 'Datos del docente', 'teacher': teacher,
#                    'error': 'Error al seleccionar  docente'}
#         return render(request, 'detail_teacher.html', context)
#


@login_required
def update_teacher(request, id):
    teacher = Teacher.objects.filter(user=request.user, pk=id).first()
    form = None
    print(teacher)
    if request.method == "GET":
        form = TeacherForm(instance=teacher)
        context = {'title': 'Editar Docente', 'form': form, 'error': ''}
        return render(request, 'teachers/create_teacher.html', context)
    else:
        try:
            form = TeacherForm(request.POST, instance=teacher)
            if form.is_valid():
                form.save()
                return redirect('teachers')
            else:
                return render(request, 'teachers/create_teacher.html',
                              {"form": form,
                               "error": "Error de datos invalidos."})
        except:
            return render(request, 'teachers/create_teacher.html',
                          {"form": form,
                           "error": "Error al actualizar registro de Docente."})


@login_required
def delete_teacher(request, id):
    teacher = None
    try:
        teacher = Teacher.objects.get(user=request.user, pk=id)
        if request.method == "GET":
            context = {'title': 'Docente a Eliminar',
                       'teacher': teacher, 'error': ''}
            return render(request, 'teachers/delete_teacher.html', context)
        else:
            teacher.delete()
            return redirect('teachers')
    except:
        context = {'title': 'Datos del Docente',
                   'teacher': teacher, 'error': 'Error al eliminar Docente'}
        return render(request, 'teachers/delete_teacher.html', context)
