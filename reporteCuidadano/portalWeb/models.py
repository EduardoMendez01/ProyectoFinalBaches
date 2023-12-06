from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    numeroTelefono = models.PositiveBigIntegerField()
    contraseña = models.CharField(max_length=128)  

class reportes(models.Model):
    usuario_correo = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)        
    codigo = models.AutoField(primary_key=True, db_column='id', null=False)
    tipo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="reportes", null=True)
    estatus = models.CharField(max_length=50, default="En Proceso")
    comentario = models.CharField(max_length=200, default="sin comentarios")

    def __str__(self):
        return f"{self.codigo} - {self.tipo}({self.estatus})"

class admintrar(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)  
