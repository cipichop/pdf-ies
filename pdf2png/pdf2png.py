import os
import fitz  # PyMuPDF
from PIL import Image

def pdf_to_png(pdf_path):
    pdf_document = fitz.open(pdf_path)

    if len(pdf_document) == 1:
        page = pdf_document.load_page(0)
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img.save(f"{pdf_path[:-4]}.png")
        return
    
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img.save(f"{pdf_path[:-4]}_page_{page_num + 1}.png")

pdfs = [file for file in os.listdir() if file.endswith('.pdf')]
for pdf in pdfs:
    print(f'Converting {pdf}...')
    pdf_to_png(pdf)
