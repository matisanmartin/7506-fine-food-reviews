import csv


# Genera un arreglo donde cada elemento es un par {clave, valor}
# nombreArchivo = String con el path del archivo a leer
# header = las columnas que posee el archivo.

def leer_archivo(nombre_archivo, header):
    with open(nombre_archivo, 'rb') as archivo:
        # Los datos del archivo quedan en dataFrame que es un []
        data_frame = csv.DictReader(archivo, fieldnames=header)
        # Elimino el primer elemento del dataFrame, ya que contiene el header
        data_frame.pop()

    return data_frame
