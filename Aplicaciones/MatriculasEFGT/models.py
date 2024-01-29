from django.db import models

# Create your models here.

class CarreraEFGT(models.Model):
    #Creacion de Atributos
    id=models.AutoField(primary_key=True)
    nombreCarreraEFGT=models.CharField(max_length=100)
    directorCarreraEFGT=models.CharField(max_length=100)
    logoCarreraEFGT=models.FileField(upload_to='logos',null=True,blank=True)
    duracionCarreraEFGT=models.CharField(max_length=100)
    facultadCarreraEFGT=models.CharField(max_length=100)



class CursoEFGT(models.Model):
    #Creacion de Atributos
    id=models.AutoField(primary_key=True)
    nivelCursoEFGT=models.CharField(max_length=50)
    descripcionCursoEFGT=models.TextField()
    aulaCursoEFGT=models.PositiveIntegerField()
    horarioCursoEFGT=models.CharField(max_length=20, help_text='Formato HH:MM - HH:MM')
    periodoCursoEFGT=models.CharField(max_length=150)

    carrera=models.ForeignKey(CarreraEFGT,null=True,blank=True,on_delete=models.PROTECT)


class AsignaturaEFGT(models.Model):
    id=models.AutoField(primary_key=True)
    nombreAsignaturaEFGT=models.CharField(max_length=150)
    creditosAsignaturaEFGT=models.PositiveIntegerField()
    fechaInicioAsignaturaEFGT=models.DateField()
    fechaFinalizacionAsignaturaEFGT=models.DateField()
    profesorAsignaturaEFGT=models.CharField(max_length=150)
    silaboAsignaturaEFGT=models.CharField(max_length=150)
    tipoAsignaturaEFGT=models.CharField(max_length=150)
    requisitosAsignaturaEFGT=models.CharField(max_length=150)

    curso=models.ForeignKey(CursoEFGT,null=True,blank=True,on_delete=models.PROTECT)
