import os
import PyPDF2

print('Combining...')
pdf_files = [file for file in os.listdir() if file.startswith('page_') and file.endswith('.pdf')]
output_pdf = 'combined_files.pdf'

merger = PyPDF2.PdfMerger()
    
for pdf_file in pdf_files:
    print(f"Adding: {pdf_file}")
    merger.append(pdf_file)

merger.write(output_pdf)
merger.close()