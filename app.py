from flask import Flask, request
from Clases.Animal import Animal as A
import xml.etree.ElementTree as ET


app = Flask(__name__)

Animales = []


@app.route('/cargarArchivo', methods=['POST'])
def cargarArchivo():
    if request.method == 'POST':
        archivo = request.files['archivo']
        if archivo:
            tree = ET.parse(archivo)
            root = tree.getroot()

            # Procesar los datos
            for cliente in root.findall('.//perro'):
                edad = cliente.find('edad').text.strip()
                raza = cliente.find('raza').text.strip()
                nuevoAnimal = A("Perro", raza, edad)
                Animales.append(nuevoAnimal)

            for cliente in root.findall('.//gato'):
                edad = cliente.find('edad').text.strip()
                raza = cliente.find('raza').text.strip()
                nuevoAnimal = A("Gato", raza, edad)
                Animales.append(nuevoAnimal)
            
            for cliente in root.findall('.//conejo'):
                edad = cliente.find('edad').text.strip()
                raza = cliente.find('raza').text.strip()
                nuevoAnimal = A("Conejo", raza, edad)
                Animales.append(nuevoAnimal)

            for animal in Animales:
                print(animal.getEspecie())
            return 'Archivo cargado correctamente'
        else:
            return 'Error al cargar el archivo'
    else:
        return 'Metodo no permitido'


@app.route('/procesarArchivo', methods=['GET'])
def procesarArchivo():
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<animales>\n'
    perros = 0
    gatos = 0
    conejos = 0
    for animal in Animales:
        if animal.getEspecie() == 'Perro':
            perros += 1
        elif animal.getEspecie() == 'Gato':
            gatos += 1
        elif animal.getEspecie() == 'Conejo':
            conejos += 1
    xml += '<perros>\n' 
    xml += '<cantidadTotal>' + str(perros) + '</cantidadTotal>\n'
    xml +='</perros>\n'
    xml += '<gatos>\n'
    xml += '<cantidadTotal>' + str(gatos) + '</cantidadTotal>\n'
    xml +='</gatos>\n'
    xml += '<conejos>\n'
    xml += '<cantidadTotal>' + str(conejos) + '</cantidadTotal>\n'
    xml +='</conejos>\n'
    xml += '</animales>'

  
    print(xml)
    return xml

@app.route('/borrarDatos', methods=['GET'])
def borrarDatos():
    if request.method == 'GET':
        Animales.clear()
    return 'Datos borrados correctamente'






app.run(debug=True, port=5000)

