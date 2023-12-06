from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Usuario, reportes, admintrar

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


from django.contrib.sessions.models import Session

def registrar(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        email = request.POST['email']
        numeroTelefono = request.POST['numeroTelefono']

        contraseña = request.POST['contraseña']

        nuevo_usuario = Usuario.objects.create(nombre=nombre, apellidos=apellidos,numeroTelefono=numeroTelefono, email=email, contraseña=contraseña)

        nuevo_usuario.save()

        return redirect('iniciarSecion')

    return render(request, 'registrarse.html')



def iniciarSesion(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        contraseña = request.POST.get('contraseña')

                
        try:
            usuario = Usuario.objects.get(email=email)

            if usuario.contraseña == contraseña:
                # Si el usuario es un admin, redirigir a una página especial para admins
                if usuario.email == email:
                    print("entro en usuario")
                    request.session['usuario_correo']=email
                    return render(request, 'menu.html')

            else:
                
                messages.error(request, 'Contraseña incorrecta. Inténtalo de nuevo.')
                return render(request, 'iniciarSecion.html')
                

        except Usuario.DoesNotExist:
            # Manejar el caso en el que no hay un usuario con el correo electrónico proporcionado
            pass

    return render(request, 'iniciarSecion.html')





def iniciarSecionAdmin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        contraseña = request.POST.get('contraseña')

                
        try:
            administracion = admintrar.objects.get(email=email)
            print("entro en admin")

            if administracion.contraseña == contraseña:
                # Si el usuario es un admin, redirigir a una página especial para admins
                if administracion.email == email:
                    print("entro en usuario")

                    return render(request, 'verReportesAmin.html')

            else:
                
                messages.error(request, 'Contraseña incorrecta. Inténtalo de nuevo.')
                return render(request, 'inicioSecionAdmin.html')
                

        except admintrar.DoesNotExist:
            # Manejar el caso en el que no hay un usuario con el correo electrónico proporcionado
            pass

    return render(request, 'inicioSecionAdmin.html')



def menu(request):
    return render(request, 'menu.html')

def hacerReportes(request):
    if request.method == 'POST':
        tipo = request.POST['reporte']
        descripcion = request.POST['Descripcion']
        ubicacion = request.POST['ubicacion']
        imagen = request.FILES.get('imagen')
        
        usuario_email = request.session.get('usuario_correo', None)  # Cambia 'user_email' a 'usuario_email'
        usuario = Usuario.objects.get(email=usuario_email)
        
        nuevo_reporte = reportes.objects.create(
            tipo=tipo,
            descripcion=descripcion,
            ubicacion=ubicacion,
            imagen=imagen,
            usuario_correo=usuario
        )

        return redirect('menu')

    return render(request, 'hacerReportes.html')


def verReportes(request):
    if request.method == 'GET':
        user_email = request.session.get('usuario_correo', None)
        
        if user_email:
            lista_reportes = reportes.objects.filter(usuario_correo__email=user_email)
        else:
            lista_reportes = reportes.objects.none()

    return render(request, 'verReportes.html', {'reportes': lista_reportes})



def menuAdmin(request):
    return render(request, 'menuAdmin.html')


def verReportesAdmin(request):
    if request.method == 'GET':
        # Obtén el parámetro 'filtro' de la URL
        filtro = request.GET.get('filtro')

        # Obtén los reportes según el filtro
        if filtro:
            reportesAdmin = reportes.objects.filter(tipo=filtro)
        else:
            reportesAdmin = reportes.objects.all()

        return render(request, 'verReportesAmin.html', {"reportesAdmin": reportesAdmin})


def editarReporte(request, codigo):
  

    editarReportes = reportes.objects.get(codigo=codigo)
    return render(request, 'edicionReportes',{"editarReportes":editarReportes})




def editarReporte(request, codigo):
    try:
        codigo = int(codigo)
        reporte = reportes.objects.get(codigo=codigo)

        if request.method == 'POST':
            estatus = request.POST.get('status')
            comentarios = request.POST.get('comentarios')

            if estatus is not None and comentarios is not None:
                reporte.estatus = estatus
                reporte.comentario = comentarios
                reporte.save()

                return redirect('verReportesAdmin')
            else:
                return HttpResponse("Parámetros de consulta incompletos")

        return render(request, 'edicionReportes.html', {'reporte': reporte})

    except ValueError:
        return HttpResponse("Código no válido")



def VisualizarReportesAdmin(request, codigo ):
    reporte = reportes.objects.get(codigo=codigo)
    return render(request, 'visualizarReportesAdmin.html', {'reporte': reporte})
