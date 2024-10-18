import os
import PyPDF2
from PIL import Image
from reportlab.pdfgen import canvas

def convert(png_file, pdf_file):
    image = Image.open(png_file)
    width, height = image.size
    pdf = canvas.Canvas(pdf_file, pagesize=(width, height))
    pdf.drawInlineImage(png_file, 0, 0, width, height)
    pdf.save()

def combine_pdfs(pdf_files, output_pdf):
    merger = PyPDF2.PdfMerger()
    
    for pdf_file in pdf_files:
        merger.append(pdf_file)
    
    merger.write(output_pdf)
    merger.close()

images = [file for file in os.listdir() if file.endswith('.png') or file.endswith('.jpg')]

for i in images:
    print(f'Converting {i}...')
    convert(i, i[:-3] + 'pdf')

print('Combining...')
pdf_files = [file for file in os.listdir() if file.endswith('.pdf')]
output_pdf = 'combined_files.pdf'

combine_pdfs(pdf_files, output_pdf)

print('Clearing temporary files...')
for i in pdf_files:
    os.remove(i)

print('All done!')