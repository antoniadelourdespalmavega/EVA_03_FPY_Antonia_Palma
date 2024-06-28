from pathlib import Path
import json
import csv
pinturas = []
menup = ['Ver listado de pinturas', 'Buscar pinturas', 'Agregar pintura', 'Eliminar pintura', 'Exportar pintura']


def respuesta():
    resp = input('Seleccione una opción:\n')
    return resp

def listar(iterable):
    if iterable == []:
        print('No hay contenido para mostrar\n')
    elif isinstance(iterable, list):
        for ind, opt in enumerate(iterable):
            print(f'{ind + 1}. {opt}')
    elif isinstance(iterable, dict):
        for llave, valor in iterable.items():
            print(f'{llave.upper} : {valor}')
        print()
    else:
        print('Error inesperado')


def existencia(ruta):
    '''Verifica si la ruta existe.
    Si no existe, la crea.
    '''
    if not ruta.exists():
        ruta.touch()
        print('La base de datos no existe, pero ahora ha sido creada')

def recuperar_data(ruta):
    if ruta.state().st_size == 0:
        return []
    else:
        with open(ruta, 'r') as stream:
            contenido = json.load(stream)





def ver_listado():
    pass



def buscar_pinturas(ruta, filtro):
    existencia(ruta)
    contenido = recuperar_data(ruta)
    if contenido != []:
        for pintura in contenido:
            if str(pintura['codigo']) == filtro or filtro.upper()



def agregar_pint():
    
    nombre = input('Indique el nombre del color')
    tipo = input('Indique si es Acrílico o Látex')
    Valor = int(input('Ingrese el valor de la pintura'))
    Stock = int(input('Ingrese el stock '))
    n_pint = [nombre, tipo, Valor, Stock]

def eliminar_pint():
    pass



def exportar_pint(rutaj):
    if not rutaj.exists():
        print('no existente la base de datos\n')
    else:
        if rutaj.exists():


while True:
    listar(menup)
    ans = input('Seleccione una opción:\n')
    if ans == '1':
        ver_listado()
    elif ans == '2':
        buscar_pinturas()
    elif ans == '3':
        agregar_pint()
    elif ans == '4':
        eliminar_pint()
    elif ans == '5':
        exportar_pint
    else:
        print('Opción inválida')