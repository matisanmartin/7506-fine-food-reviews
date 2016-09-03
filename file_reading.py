import csv


# Genera un arreglo donde cada elemento es un par {clave, valor}
# nombreArchivo = String con el path del archivo a leer
# header = las columnas que posee el archivo.

def leer_archivo(nombre_archivo):
    data_frame_vec = []
    with open(nombre_archivo, 'rt') as archivo:
        data_frame = csv.DictReader(archivo)
        for frame in data_frame:
            data_frame_vec.append(frame)

    archivo.close()
    return data_frame_vec


def generar_archivo(data):
    with open('submission.csv', 'wb') as outfile:
        submission_writer = csv.writer(outfile, delimiter=',')
