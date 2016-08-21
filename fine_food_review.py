import getopt
import sys

import data_frame_processing
import file_reading
import utils


def main(argv):
    # Leo los argumentos que se pasaron por cmdline
    try:
        opciones, argumentos = getopt.getopt(argv, 'hi:o:', ['help', 'in=', 'out='])
    except getopt.GetoptError:
        print
        'FineFodReview.py -i <infile> -o <outfile>'
        sys.exit(2)

    files = {}
    for o, a in opciones:
        if o in ('-h', '--help'):
            print
            "fine_food_review.py -i <infile> -o <outfile>"
            sys.exit()
        elif o in ('-i', '--in'):
            files['inputFile'] = a
        elif o in ('-o', '--out'):
            files['outputFile'] = a

    data_frame_train = file_reading.leer_archivo(files['inputFile'], utils.header_train)
    data_frame_processing.procesar_data_frame(data_frame_train)


if __name__ == '__main__':
    main(sys.argv[1:])


# Obtener estructuras con datos relevantes

# Procesar datos relevantes

# Generar archivo de salida
