from os import listdir, curdir
import PyPDF2

merger = PyPDF2.PdfFileMerger()

for file in listdir(curdir):
    if file.endswith('.pdf'): 
        merger.append(file)
    merger.write(f"Merged {file}")