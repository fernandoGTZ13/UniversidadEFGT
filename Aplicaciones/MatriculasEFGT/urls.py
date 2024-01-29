from django.urls import path
from . import views

urlpatterns = [
    path('',views.listadoAsignatura, name='listado_asignaturas'),
    path('guardarAsignatura/',views.guardarAsignatura),
    path('eliminarAsignatura/<id>',views.eliminarAsignatura),
    path('editarAsignatura/<id>',views.editarAsignatura),
    path('procesarActualizacionAsignatura/',views.procesarActualizacionAsignatura),


    path('curso',views.listadoCurso, name='listado_cursos'),
    path('guardarCurso/',views.guardarCurso),
    path('eliminarCurso/<id>',views.eliminarCurso),
    path('editarCurso/<id>',views.editarCurso),
    path('procesarActualizacionCurso/',views.procesarActualizacionCurso),

    path('carrera',views.listadoCarrera, name='listado_carreras'),
    path('guardarCarrera/',views.guardarCarrera),
    path('eliminarCarrera/<id>',views.eliminarCarrera),
    path('editarCarrera/<id>',views.editarCarrera),
    path('procesarActualizacionCarrera/',views.procesarActualizacionCarrera),

    path('enviar-correo/',views.enviar_correo, name='enviar_correo'),

    path('vistal/',views.vistal, name='vistal')
]
