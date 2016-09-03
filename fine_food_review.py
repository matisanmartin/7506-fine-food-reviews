import argparse

import data_frame_processing
import file_reading
import utils

parser = argparse.ArgmumentParser(description='Fine food reviews')
parser.add_argument('i', '--input', help='Archivo a procesar', required=True)
parser.add_argument('o', '--output', help='Archivo de salida', required=True)
parser.add_argument("m", '--mode', help='Modo: train/test', required=False, default='train')

args = vars(parser.parse_args())

if args['mode'] == 'train':
    data_frame_train = file_reading.leer_archivo(args.i, utils.header_train)
    data_frame_processing.procesar_data_frame_train(data_frame_train)
elif args['mode'] == 'test':
    data_frame_test = file_reading.leer_archivo(args.i, utils.header_test)
    data_frame_processing.procesar_data_frame_test(data_frame_test)



# Obtener estructuras con datos relevantes

# Procesar datos relevantes

# Generar archivo de salida
