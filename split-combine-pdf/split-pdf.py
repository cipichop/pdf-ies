import os
import PyPDF2
import argparse

parser = argparse.ArgumentParser(description='Locally split your PDF file')
parser.add_argument('pdf_file', type=str, help='PDF file to split')
args = parser.parse_args()

print('Splitting...')

with open(args.pdf_file, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    num_pages = len(pdf_reader.pages)
    for num in range(num_pages):
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[num])
        output_pdf = f"page_{num + 1}.pdf"

        with open(output_pdf, 'wb') as output_pdf_file:
            pdf_writer.write(output_pdf_file)

        print(f"Created: {output_pdf}")