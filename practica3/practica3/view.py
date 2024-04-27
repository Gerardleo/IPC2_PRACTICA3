from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from requests import post,get
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

url = 'http://localhost:5000/'


def index(request):
    return render(request, 'index.html')

def CargarArchivo(request):
    return render(request, 'cargarArchivo.html')

def procesarDatos(request):
    return render(request, 'procesarDatos.html')

def datosPersonales(request):
    return render(request, 'datosPersonales.html')

def borrar_Datos(request):
    return render(request, 'borrarDatos.html')

@csrf_exempt
def cargarArchivoMascotas(request):
    global url
    mensaje = None  # Mensaje de respuesta inicialmente vacío

    if request.method == 'POST':
        archivo = request.FILES.get('archivo')
        if archivo:
            # Crear una solicitud POST al backend de Flask
            url_flask = url + '/cargarArchivo'
            files = {'archivo': archivo}
            response = post(url_flask, files=files)

            if response.status_code == 200:
                mensaje = 'Archivo cargado correctamente'
            else:
                mensaje = 'Error al cargar el archivo'

    return render(request, 'cargarArchivo.html', {'mensaje': mensaje})
    
@csrf_exempt  # Agrega csrf_exempt para evitar el token CSRF en esta vista
def procesarDatosSalida(request):
    global url
    mensaje = None
    response_text = None  # Inicializa la respuesta de la API como None

    if request.method == 'GET':
        url_flask = url + '/procesarArchivo'
        response = get(url_flask)
        if response.status_code == 200:
            print(response.text)
            response_text = response.text  # Obtiene el texto de la respuesta
            mensaje = 'Archivo procesado correctamente'
        else:
            mensaje = 'Error al obtener la respuesta de la API Flask'

    # Renderizar la plantilla con el resultado y el botón
    return render(request, 'procesarDatos.html', {'xml': response_text, 'mensaje': mensaje, 'respuesta': response_text})

@csrf_exempt
def borrarDatos(request):
    global url
    mensaje = None
    response_text = None

    if request.method == 'GET':
        url_flask = url + '/borrarDatos'
        response = get(url_flask)
        if response.status_code == 200:
            response_text = response.text
            mensaje = 'Datos borrados correctamente'
        else:
            mensaje = 'Error al borrar los datos'
    
    return render(request, 'borrarDatos.html', {'mensaje': mensaje, 'respuesta': response_text})
