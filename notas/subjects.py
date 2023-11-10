from django.shortcuts import render, redirect
from .forms import SubjectForm
from .models import Subject
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required
def init(request):
    print(request)
    context, subjects = None, None
    try:
        query = request.GET.get('q')  # ver
        if query:
            subjects = (Subject.objects.filter(
                name__icontains=query) or
                Subject.objects.filter
                (code__icontains=query))
        else:
            subjects = Subject.objects.all()
            # #  select * from Student  where user=1
        # Crea un paginador con los estudiantes
        paginator = Paginator(subjects, 4)
        # Obtén el número de página actual
        pagina = request.GET.get('page', 1)
        # Obtén los libros de la página actual
        asignaturas_paginadas = paginator.get_page(pagina)
        # Envía el paginador con los estudiantes
        # y el número de páginas al contexto
        context = {
            'asignaturas': asignaturas_paginadas,
            'title': 'Consulta de Asignaturas',
            'paginator': paginator,
            'num_pages': paginator.num_pages,
        }

        return render(request, 'asignaturas/subjects.html', context)
    except ValueError:
        print(ValueError)
        return render(request, 'asignaturas/subjects.html',
                      {'title': 'Consulta de Asignaturas',
                       'error': 'Ha ocurrido un error en la consulta'})


@login_required
def create_subject(request):
    form = None
    if request.method == "GET":
        context = {'title': 'Crear Asignatura',
                   'form': SubjectForm(), 'error': ''}
        return render(request, 'asignaturas/create_subject.html', context)
    else:
        try:
            form = SubjectForm(request.POST)
            if form.is_valid():
                subject = form.save(commit=False)  # lo tiene en memoria
                subject.save()  # lo guarda en la BD
                return redirect('subjects')
            else:
                return render(request,
                              'asignaturas/create_subject.html',
                              {"form": form,
                               "error": "Error de datos invalidos."})
        except ValueError:
            print(ValueError)
            return render(request,
                          'Asignaturas/create_subject.html',
                          {"form": form,
                           "error": "Error al Crear Registro de Asignatura."})


@login_required
def update_subject(request, id):
    subject = Subject.objects.filter(id=id).first()
    form = None
    print(subject)
    if request.method == "GET":
        form = SubjectForm(instance=subject)
        context = {'title': 'Editar Asignatura', 'form': form, 'error': ''}
        return render(request, 'asignaturas/create_subject.html', context)
    else:
        try:
            form = SubjectForm(request.POST, instance=subject)
            if form.is_valid():
                form.save()
                return redirect('subjects')
            else:
                return render(request, 'asignaturas/create_subject.html',
                              {"form": form,
                               "error": "Error de datos invalidos."})
        except:
            return render(request, 'asignaturas/create_subject.html',
                          {"form": form,
                           "error": "Error al actualizar registro de asignatura."})


@login_required
def delete_subject(request, id):
    subject = None
    try:
        subject = Subject.objects.get(id=id)
        if request.method == "GET":
            context = {'title': 'Asignatura a Eliminar',
                       'asignatura': subject, 'error': ''}
            return render(request, 'asignaturas/delete_subject.html', context)
        else:
            subject.delete()
            return redirect('subjects')
    except ValueError:
        print(ValueError)
        context = {'title': 'Datos de la asignatura',
                   'asignatura': subject,
                   'error': 'Error al eliminar asignaruta'}
        return render(request, 'asignaturas/delete_subject.html', context)
