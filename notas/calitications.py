from django.shortcuts import render, redirect
from .forms import calificationForm
from .models import Calification
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required
def init(request):
    print(request)
    context, califications = None, None
    try:
        query = request.GET.get('q')  # ver
        if query:
            califications = (Calification.objects.filter(
                enroll__student__firstname__icontains=query) or
                califications.objects.filter
                (enroll__student__lastname__icontains=query) or
                califications.objects.filter
                (enroll__subject__name__icontains=query))
        else:
            califications = Calification.objects.all()
            # #  select * from Student  where user=1
        # Crea un paginador con los estudiantes
        paginator = Paginator(califications, 2)
        # Obtén el número de página actual
        pagina = request.GET.get('page', 1)
        # Obtén los libros de la página actual
        calificaciones_paginadas = paginator.get_page(pagina)
        # Envía el paginador con los estudiantes
        # y el número de páginas al contexto
        context = {
            'calificaciones': calificaciones_paginadas,
            'title': 'Consulta de calificaciones',
            'paginator': paginator,
            'num_pages': paginator.num_pages,
        }

        return render(request, 'calificaciones/calification.html', context)
    except ValueError:
        print(ValueError)
        return render(request, 'calificaciones/calification.html',
                      {'title': 'Consulta de calificaciones',
                       'error': 'Ha ocurrido un error en la consulta'})


@ login_required
def create_calification(request):
    form = None
    if request.method == "GET":
        context = {'title': 'registrar calificación',
                   'form': calificationForm(), 'error': ''}
        return render(request, 'calificaciones/create_calification.html', context)
    else:
        try:
            form = calificationForm(request.POST)
            if form.is_valid():
                calification = form.save(commit=False)  # lo tiene en memoria
                calification.save()  # lo guarda en la BD
                return redirect('calification')
            else:
                return render(request,
                              'calificaciones/create_calification.html',
                              {"form": form,
                               "error": "Error de datos invalidos."})
        except ValueError:
            print(ValueError)
            return render(request,
                          'calificaciones/create_calification.html',
                          {"form": form,
                           "error": "Error al registrar la calificación."})


@ login_required
def update_calification(request, id):
    calificacion = Calification.objects.filter(id=id).first()
    form = None
    print(calificacion)
    if request.method == "GET":
        form = calificationForm(instance=calificacion)
        context = {'title': 'Editar calificación',
                   'form': form, 'error': ''}
        return render(request, 'calificaciones/create_calification.html', context)
    else:
        try:
            form = calificationForm(request.POST, instance=calificacion)
            if form.is_valid():
                form.save()
                return redirect('calification')
            else:
                return render(request, 'calificaciones/create_calification.html',
                              {"form": form,
                               "error": "Error de datos invalidos."})
        except:
            return render(request, 'calificaciones/create_calification.html',
                          {"form": form,
                           "error": "Error al actualizar calificacion."})


@ login_required
def delete_calification(request, id):
    calificacion = None

    try:
        calificacion = Calification.objects.get(id=id)
        if request.method == "GET":
            context = {'title': 'calificacion a Eliminar',
                       'calificacion': calificacion, 'error': ''}
            return render(request, 'calificaciones/delete_calification.html', context)
        else:
            calificacion.delete()
            return redirect('calification')
    except ValueError:
        print(ValueError)
        context = {'title': 'Datos de la calificacion',
                   'calificacion': calificacion,
                   'error': 'Error al eliminar calificacion'}
        return render(request, 'calificaciones/delete_calification.html', context)
