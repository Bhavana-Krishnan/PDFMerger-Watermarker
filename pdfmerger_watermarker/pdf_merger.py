import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(f"Adding: {pdf}")
        merger.append(pdf)
    merger.write('super.pdf')
    merger.close()
    return "Merged!"


pdf_combiner(inputs)
