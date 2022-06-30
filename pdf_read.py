#!/usr/bin/python3

import argparse
from PyPDF4 import PdfFileReader

def print_meta(filename):
    with open(filename, 'rb') as pdf:
        pdf_file = PdfFileReader(pdf)
        pdf_info = pdf_file.getDocumentInfo()
        print(f'[*] PDF MetaData for: {str(filename)}')
        for meta_item in pdf_info:
            print(f'[+] {meta_item}: {pdf_info[meta_item]}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage='python3 pdf_read.py PDF_FILENAME'
    )
    parser.add_argument('pdf_file_name', type=str, metavar='PDF_FILENAME',
    help='specify the name of the pdf file')

    args = parser.parse_args()
    print_meta(args.pdf_file_name)
