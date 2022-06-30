#!/usr/bin/python3

import argparse
from PyPDF4 import PdfFileReader

sample_pdf = 'sample.pdf'

def print_meta(filename):
    with open(filename, 'rb') as pdf:
        pdf_file = PdfFileReader(pdf)
        pdf_info = pdf_file.getDocumentInfo()
        print(f'[*] PDF MetaData for: {str(filename)}')
        for meta_item in pdf_info:
            print(f'[+] {meta_item}: {pdf_info[meta_item]}')


print_meta(sample_pdf)
