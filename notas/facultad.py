from django.shortcuts import render, redirect
from .forms import FacultyForm
from .models import Faculty
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required
def init(request):
    print(request)
    context, Faculties = None, None
    try:
        query = request.GET.get('q')  # ver
        if query:
            Faculties = (Faculty.objects.filter(
                name__icontains=query) or
                Faculty.objects.filter
                (code__icontains=query))
        else:
            Faculties = Faculty.objects.all()
            # #  select * from Student  where user=1
        # Crea un paginador con los estudiantes
        paginator = Paginator(Faculties, 2)
        # Obtén el número de página actual
        pagina = request.GET.get('page', 1)
        # Obtén los libros de la página actual
        facultades_paginados = paginator.get_page(pagina)
        # Envía el paginador con los estudiantes
        # y el número de páginas al contexto
        context = {
            'facultades': facultades_paginados,
            'title': 'Consulta de Facultades',
            'paginator': paginator,
            'num_pages': paginator.num_pages,
        }

        return render(request, 'facultad/facultades.html', context)
    except ValueError:
        print(ValueError)
        return render(request, 'facultad/facultades.html',
                      {'title': 'Consulta de facultades',
                       'error': 'Ha ocurrido un error en la consulta'})


@login_required
def create_faculty(request):
    form = None
    if request.method == "GET":
        context = {'title': 'Crear Facultades',
                   'form': FacultyForm(), 'error': ''}
        return render(request, 'facultad/create_faculty.html', context)
    else:
        try:
            form = FacultyForm(request.POST)
            if form.is_valid():
                faculty = form.save(commit=False)  # lo tiene en memoria
                faculty.save()  # lo guarda en la BD
                return redirect('faculty')
            else:
                return render(request,
                              'facultad/create_faculty.html',
                              {"form": form,
                               "error": "Error de datos invalidos."})
        except ValueError:
            print(ValueError)
            return render(request,
                          'facultad/create_faculty.html',
                          {"form": form,
                           "error": "Error al Crear Registro de Estudiante."})


@login_required
def update_faculty(request, id):
    faculty = Faculty.objects.filter(id=id).first()
    form = None
    print(faculty)
    if request.method == "GET":
        form = FacultyForm(instance=faculty)
        context = {'title': 'Editar Facultad', 'form': form, 'error': ''}
        return render(request, 'facultad/create_faculty.html', context)
    else:
        try:
            form = FacultyForm(request.POST, instance=faculty)
            if form.is_valid():
                form.save()
                return redirect('faculty')
            else:
                return render(request, 'facultad/create_faculty.html',
                              {"form": form,
                               "error": "Error de datos invalidos."})
        except:
            return render(request, 'facultad/create_faculty.html',
                          {"form": form,
                           "error": "Error al actualizar registro de Estudiante."})


@login_required
def delete_faculty(request, id):
    facultad = None
    try:
        facultad = Faculty.objects.get(id=id)
        if request.method == "GET":
            context = {'title': 'Facultad a Eliminar',
                       'facultad': facultad, 'error': ''}
            return render(request, 'facultad/delete_faculty.html', context)
        else:
            facultad.delete()
            return redirect('faculty')
    except ValueError:
        print(ValueError)
        context = {'title': 'Datos de la facultad',
                   'facultad': facultad,
                   'error': 'Error al eliminar facultad'}
        return render(request, 'facultad/delete_faculty.html', context)
