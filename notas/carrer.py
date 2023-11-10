from django.shortcuts import render, redirect
from .forms import CarrerForm
from .models import Carrer, Subject
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required
def init(request):
    print(request)
    context, carrers = None, None
    try:
        query = request.GET.get('q')  # ver
        if query:
            carrers = (Carrer.objects.filter(
                name__icontains=query) or
                Carrer.objects.filter
                (Facultad__icontains=query))
        else:
            carrers = Carrer.objects.all()
            # #  select * from Student  where user=1
        # Crea un paginador con los estudiantes
        paginator = Paginator(carrers, 4)
        # Obtén el número de página actual
        pagina = request.GET.get('page', 1)
        # Obtén los libros de la página actual
        carreras_paginadas = paginator.get_page(pagina)
        # Envía el paginador con los estudiantes
        # y el número de páginas al contexto
        context = {
            'carreras': carreras_paginadas,
            'title': 'Consulta de Carreras',
            'paginator': paginator,
            'num_pages': paginator.num_pages,
        }

        return render(request, 'carrera/carrers.html', context)
    except ValueError:
        print(ValueError)
        return render(request, 'carrera/carrers.html',
                      {'title': 'Consulta de carreras',
                       'error': 'Ha ocurrido un error en la consulta'})


@login_required
def create_carrer(request):
    form = None
    if request.method == "GET":
        context = {'title': 'Crear Carrera',
                   'form': CarrerForm(), 'error': ''}
        return render(request, 'carrera/create_carrer.html', context)
    else:
        try:
            form = CarrerForm(request.POST)
            print(request.POST)
            # materias = request.POST['Subjects']
            if form.is_valid():
                carrer = form.save(commit=False)  # lo tiene en memoria
                # for materia in materias:
                #     subjec = Subject.objects.get(id=materia)
                #     print(subjec)
                #     Carrer.Subjects.add(subjec)

                carrer.save()  # lo guarda en la BD
                return redirect('carrers')
            else:
                return render(request,
                              'carrera/create_carrer.html',
                              {"form": form,
                               "error": "Error de datos invalidos."})
        except ValueError:
            print(ValueError)
            return render(request,
                          'carrera/create_carrer.html',
                          {"form": form,
                           "error": "Error al Crear Registro de Carrera."})


@login_required
def update_carrer(request, id):
    carrera = Carrer.objects.filter(id=id).first()
    form = None
    print(carrera)
    if request.method == "GET":
        form = CarrerForm(instance=carrera)
        context = {'title': 'Editar Facultad', 'form': form, 'error': ''}
        return render(request, 'carrera/create_carrer.html', context)
    else:
        try:
            form = CarrerForm(request.POST, instance=carrera)
            if form.is_valid():
                form.save()
                return redirect('carrers')
            else:
                return render(request, 'carrera/create_carrer.html',
                              {"form": form,
                               "error": "Error de datos invalidos."})
        except:
            return render(request, 'carrera/create_carrer.html',
                          {"form": form,
                           "error": "Error al actualizar registro de Carrera."})


@login_required
def delete_carrer(request, id):
    carrera = None
    try:
        carrera = Carrer.objects.get(id=id)
        if request.method == "GET":
            context = {'title': 'Carrera a Eliminar',
                       'carrera': carrera, 'error': ''}
            return render(request, 'carrera/delete_carrer.html', context)
        else:
            carrera.delete()
            return redirect('carrers')
    except ValueError:
        print(ValueError)
        context = {'title': 'Datos de la carrera',
                   'carrera': carrera,
                   'error': 'Error al eliminar carrera'}
        return render(request, 'carrera/delete_carrer.html', context)
