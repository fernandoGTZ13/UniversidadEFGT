from django.shortcuts import render,redirect

# Create your views here.
from .models import AsignaturaEFGT, CursoEFGT, CarreraEFGT

# Create your views here.
from django.contrib import messages


#Vista para el correo
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
#####################################################################################
######################################################################################

def listadoAsignatura(request):
    asignatura=AsignaturaEFGT.objects.all()
    cursosBdd=CursoEFGT.objects.all()
    return render(request,'listadoAsignatura.html',{'asignaturas':asignatura,'cursos':cursosBdd})
#
#definir funcion guardar Provincia
def guardarAsignatura(request):
    id_curso=request.POST["id_curso"]
    #Capturar tipo seleccionado por el usuario
    cursoSeleccionado=CursoEFGT.objects.get(id=id_curso)
    #capturar valores mediante el metodo POST que es mas seguro

    nombreAsignaturaEFGT=request.POST["nombreAsignaturaEFGT"]
    creditosAsignaturaEFGT=request.POST["creditosAsignaturaEFGT"]
    fechaInicioAsignaturaEFGT=request.POST["fechaInicioAsignaturaEFGT"]
    fechaFinalizacionAsignaturaEFGT=request.POST["fechaFinalizacionAsignaturaEFGT"]
    profesorAsignaturaEFGT=request.POST["profesorAsignaturaEFGT"]
    silaboAsignaturaEFGT=request.POST["silaboAsignaturaEFGT"]
    tipoAsignaturaEFGT=request.POST["tipoAsignaturaEFGT"]
    requisitosAsignaturaEFGT=request.POST["requisitosAsignaturaEFGT"]



    #Crear cualquier objeto
    nuevoAsignatura=AsignaturaEFGT.objects.create(nombreAsignaturaEFGT=nombreAsignaturaEFGT,creditosAsignaturaEFGT=creditosAsignaturaEFGT,
    fechaInicioAsignaturaEFGT=fechaInicioAsignaturaEFGT,fechaFinalizacionAsignaturaEFGT=fechaFinalizacionAsignaturaEFGT,profesorAsignaturaEFGT=profesorAsignaturaEFGT,
    silaboAsignaturaEFGT=silaboAsignaturaEFGT,tipoAsignaturaEFGT=tipoAsignaturaEFGT,requisitosAsignaturaEFGT=requisitosAsignaturaEFGT,curso=cursoSeleccionado)

    #Crear mensaje de guardado de cliente antes del return

    messages.success(request,'Asignatura Guardado Exitosamente')

    return  redirect('/')


    ## definir funcion eliminar llamando al ORM
def eliminarAsignatura(request,id): #en este caso se elimina por ide por eso se pone ,id
    #crear objeto cualquiera en este caso cliente Eliminar
    asignaturaEliminar=AsignaturaEFGT.objects.get(id=id) # este id se relaciona con models
    asignaturaEliminar.delete()
    messages.success(request,'Asignatura eliminado Exitosamente')
    return redirect('/')   #redirecciona a la pag principal


    #Crear la funcion editar cliente
def editarAsignatura(request,id):
    asignaturaEditar=AsignaturaEFGT.objects.get(id=id)
    cursosBdd=CursoEFGT.objects.all()
    return render(request,'editarAsignatura.html',{'asignatura':asignaturaEditar,'cursos':cursosBdd})

def procesarActualizacionAsignatura(request):
    id=request.POST["id"]
    id_curso=request.POST["id_curso"]
    #Capturar tipo seleccionado por el usuario
    cursoSeleccionado=CursoEFGT.objects.get(id=id_curso)

    nombreAsignaturaEFGT=request.POST["nombreAsignaturaEFGT"]
    creditosAsignaturaEFGT=request.POST["creditosAsignaturaEFGT"]
    fechaInicioAsignaturaEFGT=request.POST["fechaInicioAsignaturaEFGT"]
    fechaFinalizacionAsignaturaEFGT=request.POST["fechaFinalizacionAsignaturaEFGT"]
    profesorAsignaturaEFGT=request.POST["profesorAsignaturaEFGT"]
    silaboAsignaturaEFGT=request.POST["silaboAsignaturaEFGT"]
    tipoAsignaturaEFGT=request.POST["tipoAsignaturaEFGT"]
    requisitosAsignaturaEFGT=request.POST["requisitosAsignaturaEFGT"]

    #Insertando datos mediante el ORM de DJANGO
    asignaturaEditar=AsignaturaEFGT.objects.get(id=id)
    asignaturaEditar.curso=cursoSeleccionado
    asignaturaEditar.nombreAsignaturaEFGT=nombreAsignaturaEFGT
    asignaturaEditar.creditosAsignaturaEFGT=creditosAsignaturaEFGT
    asignaturaEditar.fechaInicioAsignaturaEFGT=fechaInicioAsignaturaEFGT
    asignaturaEditar.fechaFinalizacionAsignaturaEFGT=fechaFinalizacionAsignaturaEFGT
    asignaturaEditar.profesorAsignaturaEFGT=profesorAsignaturaEFGT
    asignaturaEditar.silaboAsignaturaEFGT=silaboAsignaturaEFGT
    asignaturaEditar.tipoAsignaturaEFGT=tipoAsignaturaEFGT
    asignaturaEditar.requisitosAsignaturaEFGT=requisitosAsignaturaEFGT

    asignaturaEditar.save()
    messages.success(request,
      'Asignatura ACTUALIZADO Exitosamente')
    return redirect('/')


################################################################################
################################################################################


def listadoCurso(request):
    curso=CursoEFGT.objects.all()
    carrerasBdd=CarreraEFGT.objects.all()
    return render(request,'listadoCurso.html',{'cursos':curso,'carreras':carrerasBdd})
#
#definir funcion guardar Provincia
def guardarCurso(request):
    #capturar valores mediante el metodo POST que es mas seguro
    id_carrera=request.POST["id_carrera"]
    #Capturar tipo seleccionado por el usuario
    carreraSeleccionado=CarreraEFGT.objects.get(id=id_carrera)


    nivelCursoEFGT=request.POST["nivelCursoEFGT"]
    descripcionCursoEFGT=request.POST["descripcionCursoEFGT"]
    aulaCursoEFGT=request.POST["aulaCursoEFGT"]
    horarioCursoEFGT=request.POST["horarioCursoEFGT"]
    periodoCursoEFGT=request.POST["periodoCursoEFGT"]

    #Crear cualquier objeto
    nuevoCurso=CursoEFGT.objects.create(nivelCursoEFGT=nivelCursoEFGT,descripcionCursoEFGT=descripcionCursoEFGT,
    aulaCursoEFGT=aulaCursoEFGT,horarioCursoEFGT=horarioCursoEFGT,periodoCursoEFGT=periodoCursoEFGT,carrera=carreraSeleccionado)

    #Crear mensaje de guardado de cliente antes del return

    messages.success(request,'Curso Guardado Exitosamente')

    return  redirect('listado_cursos')


    ## definir funcion eliminar llamando al ORM
def eliminarCurso(request,id): #en este caso se elimina por ide por eso se pone ,id
    #crear objeto cualquiera en este caso cliente Eliminar
    cursoEliminar=CursoEFGT.objects.get(id=id) # este id se relaciona con models
    cursoEliminar.delete()
    messages.success(request,'Curso eliminado Exitosamente')
    return redirect('listado_cursos')


    #Crear la funcion editar cliente
def editarCurso(request,id):
    cursoEditar=CursoEFGT.objects.get(id=id)
    carrerasBdd=CarreraEFGT.objects.all()
    return render(request,'editarCurso.html',{'curso':cursoEditar,'carreras':carrerasBdd})

def procesarActualizacionCurso(request):
    id=request.POST["id"]
    id_carrera=request.POST["id_carrera"]
    #Capturar tipo seleccionado por el usuario
    carreraSeleccionado=CarreraEFGT.objects.get(id=id_carrera)

    nivelCursoEFGT=request.POST["nivelCursoEFGT"]
    descripcionCursoEFGT=request.POST["descripcionCursoEFGT"]
    aulaCursoEFGT=request.POST["aulaCursoEFGT"]
    horarioCursoEFGT=request.POST["horarioCursoEFGT"]
    periodoCursoEFGT=request.POST["periodoCursoEFGT"]

    #Insertando datos mediante el ORM de DJANGO
    cursoEditar=CursoEFGT.objects.get(id=id)
    cursoEditar.carrera=carreraSeleccionado
    cursoEditar.nivelCursoEFGT=nivelCursoEFGT
    cursoEditar.descripcionCursoEFGT=descripcionCursoEFGT
    cursoEditar.aulaCursoEFGT=aulaCursoEFGT
    cursoEditar.horarioCursoEFGT=horarioCursoEFGT
    cursoEditar.periodoCursoEFGT=periodoCursoEFGT
    cursoEditar.save()
    messages.success(request,
      'Curso ACTUALIZADO Exitosamente')
    return redirect('listado_cursos')


################################################################################
################################################################################


def listadoCarrera(request):
    carrera=CarreraEFGT.objects.all()
    return render(request,'listadoCarrera.html',{'carreras':carrera})
#
#definir funcion guardar Provincia
def guardarCarrera(request):
    #capturar valores mediante el metodo POST que es mas seguro
    nombreCarreraEFGT=request.POST["nombreCarreraEFGT"]
    directorCarreraEFGT=request.POST["directorCarreraEFGT"]
    duracionCarreraEFGT=request.POST["duracionCarreraEFGT"]
    facultadCarreraEFGT=request.POST["facultadCarreraEFGT"]

    logoCarreraEFGT=request.FILES.get("logoCarreraEFGT")

    #Crear cualquier objeto
    nuevoCarrera=CarreraEFGT.objects.create(nombreCarreraEFGT=nombreCarreraEFGT,directorCarreraEFGT=directorCarreraEFGT,
    duracionCarreraEFGT=duracionCarreraEFGT,facultadCarreraEFGT=facultadCarreraEFGT,logoCarreraEFGT=logoCarreraEFGT)

    #Crear mensaje de guardado antes del return

    messages.success(request,'Carrera Guardado Exitosamente')

    return  redirect('listado_carreras')


    ## definir funcion eliminar llamando al ORM
def eliminarCarrera(request,id): #en este caso se elimina por ide por eso se pone ,id
    #crear objeto cualquiera en este caso carrera Eliminar
    carreraEliminar=CarreraEFGT.objects.get(id=id) # este id se relaciona con models
    carreraEliminar.delete()
    messages.success(request,'Carrera eliminado Exitosamente')
    return redirect('listado_carreras')


    #Crear la funcion editar
def editarCarrera(request,id):
    carreraEditar=CarreraEFGT.objects.get(id=id)
    return render(request,'editarCarrera.html',{'carrera':carreraEditar})

def procesarActualizacionCarrera(request):
    id=request.POST["id"]
    nombreCarreraEFGT=request.POST["nombreCarreraEFGT"]
    directorCarreraEFGT=request.POST["directorCarreraEFGT"]
    duracionCarreraEFGT=request.POST["duracionCarreraEFGT"]
    facultadCarreraEFGT=request.POST["facultadCarreraEFGT"]

    logoCarreraEFGT=request.FILES.get("logoCarreraEFGT")

    #Insertando datos mediante el ORM de DJANGO
    carreraEditar=CarreraEFGT.objects.get(id=id)

    carreraEditar.nombreCarreraEFGT=nombreCarreraEFGT
    carreraEditar.directorCarreraEFGT=directorCarreraEFGT
    carreraEditar.duracionCarreraEFGT=duracionCarreraEFGT
    carreraEditar.facultadCarreraEFGT=facultadCarreraEFGT
    carreraEditar.logoCarreraEFGT=logoCarreraEFGT
    carreraEditar.save()
    messages.success(request,
      'Carrera ACTUALIZADO Exitosamente')
    return redirect('listado_carreras')


################################################################################

def vistal(request):
    return render(request, 'enviar_correo.html')

def enviar_correo(request):
    if request.method == 'POST':
        destinatario = request.POST.get('destinatario')
        asunto = request.POST.get('asunto')
        cuerpo = request.POST.get('cuerpo')

        send_mail(asunto, cuerpo, settings.EMAIL_HOST_USER, [destinatario], fail_silently=False)

        messages.success(request, 'se ha enviado tu correo')
        return HttpResponseRedirect('/vistal')

    return render(request, 'enviar_correo.html')
