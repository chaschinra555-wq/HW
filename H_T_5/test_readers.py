import sys
import argparse

from HT5.utils.reader import csv_reader, json_reader
from HT5.utils.reader import bin_reader, txt_reader, image_reader as imread
from HT5.utils.processor import histogram
from HT5.utils.writer import image_writer

from HT5.utils.image_toner import equalization, gamma_correction, stat_correction


def print_args_1():
    print(type(sys.argv))
    if (len(sys.argv) > 1):
        for param in sys.argv[1:]:
            print(param, type(param))
    return sys.argv[1:]

def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-img','--img_path', default ='', help='Path to image')
    parser.add_argument('-jjj', '--jjj_jjj')
    parser.add_argument('-a', '--alpha', type = float)
    parser.add_argument('-b', '--beta', type = float)
    parser.add_argument ('-p','--path', default ='', help='Input file path ')
    # parser.add_argument('-t','--type', default='txt', help='Input file format ') TODO delete

    parser.add_argument('-o', '--output', help='Save file path')

    return parser

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = init_parser()
    args = parser.parse_args(sys.argv[1:])

    image = None
    hist = None

    image = imread.read_data(args.img_path)
    hist = histogram.image_processing(image)

    hist_template = None

    match args.path.split('.')[-1]:
        case 'jpg' | 'png':
            img2 = imread.read_data(args.path)
            hist_template = histogram.image_processing(img2)
        case 'csv':
            hist_template = csv_reader.read_data(args.path)
        case 'bin':
            hist_template = bin_reader.read_data(args.path)
        case 'txt':
            hist_template = txt_reader.read_data(args.path)
        case 'json':
            hist_template = json_reader.read_data(args.path)
        case _:
            pass


    match args.jjj_jjj:
        case 'equalization':

            res = equalization.equalization(image)
        case 'gamma-correction':
            res = gamma_correction.apply_gamma_cor(
                image, args.alpha, args.beta)
        case _:
            pass

    if args.jjj_jjj is None:
        res_image = stat_correction.processing(hist_template, image)
    else:
        res_image = res

    image_writer.write_data(args.output, res_image)