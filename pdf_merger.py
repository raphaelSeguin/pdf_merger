#! /usr/bin/python

from PyPDF2 import PdfFileReader, PdfFileWriter
from os import walk

pdf_dir = './pdfs/'

def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':    
    for root, dirs, files in walk(pdf_dir):
	paths = files
    paths.sort()
    rel_paths = []
    print('--- merged files ---')
    for path in paths:
        print(path)
        rel_paths.append(pdf_dir + path)
    rel_paths.sort()
    merge_pdfs(rel_paths, output='merged.pdf')
