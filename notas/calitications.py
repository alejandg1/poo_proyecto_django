from django.shortcuts import render, redirect
from .forms import Enrollform
from .models import enrollment
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required
def init(request):
    print(request)
    context, Enrolls = None, None
    try:
        query = request.GET.get('q')  # ver
        if query:
            Enrolls = (enrollment.objects.filter(
                student__firstname__icontains=query) or
                enrollment.objects.filter
                (student__lastname__icontains=query) or
                enrollment.objects.filter
                (subject__name__icontains=query))
        else:
            Enrolls = enrollment.objects.all()
            # #  select * from Student  where user=1
        # Crea un paginador con los estudiantes
        paginator = Paginator(Enrolls, 2)
        # Obtén el número de página actual
        pagina = request.GET.get('page', 1)
        # Obtén los libros de la página actual
        matriculas_paginadas = paginator.get_page(pagina)
        # Envía el paginador con los estudiantes
        # y el número de páginas al contexto
        context = {
            'matriculas': matriculas_paginadas,
            'title': 'Consulta de matriculas',
            'paginator': paginator,
            'num_pages': paginator.num_pages,
        }

        return render(request, 'matricula/enrolls.html', context)
    except ValueError:
        print(ValueError)
        return render(request, 'matricula/enrolls.html',
                      {'title': 'Consulta de matriculas',
                       'error': 'Ha ocurrido un error en la consulta'})


@ login_required
def create_enroll(request):
    form = None
    if request.method == "GET":
        context = {'title': 'Crear matricula',
                   'form': Enrollform(), 'error': ''}
        return render(request, 'matricula/create_enroll.html', context)
    else:
        try:
            form = Enrollform(request.POST)
            if form.is_valid():
                matricula = form.save(commit=False)  # lo tiene en memoria
                matricula.save()  # lo guarda en la BD
                return redirect('enroll')
            else:
                return render(request,
                              'matricula/create_enroll.html',
                              {"form": form,
                               "error": "Error de datos invalidos."})
        except ValueError:
            print(ValueError)
            return render(request,
                          'matricula/create_enroll.html',
                          {"form": form,
                           "error": "Error al Crear Registro de matricula."})


@ login_required
def update_enroll(request, id):
    matricula = enrollment.objects.filter(id=id).first()
    form = None
    print(matricula)
    if request.method == "GET":
        form = Enrollform(instance=matricula)
        context = {'title': 'Editar matriculas',
                   'form': form, 'error': ''}
        return render(request, 'matricula/create_enroll.html', context)
    else:
        try:
            form = Enrollform(request.POST, instance=matricula)
            if form.is_valid():
                form.save()
                return redirect('enroll')
            else:
                return render(request, 'matricula/create_enroll.html',
                              {"form": form,
                               "error": "Error de datos invalidos."})
        except:
            return render(request, 'matricula/create_enroll.html',
                          {"form": form,
                           "error": "Error al actualizar registro de matricula."})


@ login_required
def delete_enrroll(request, id):
    matricula = None
    try:
        matricula = enrollment.objects.get(id=id)
        if request.method == "GET":
            context = {'title': 'matricula a Eliminar',
                       'matricula': matricula, 'error': ''}
            return render(request, 'matricula/delete_enroll.html', context)
        else:
            matricula.delete()
            return redirect('enroll')
    except ValueError:
        print(ValueError)
        context = {'title': 'Datos de la matricula',
                   'matricula': matricula,
                   'error': 'Error al eliminar matricula'}
        return render(request, 'matricula/delete_enroll.html', context)
