import PyPDF2
import sys
import os

# Command-line arguments: watermark file and input PDFs
watermark_pdf = sys.argv[1]
input_pdf_list = sys.argv[2:]


def watermark(watermark_pdf, input_pdf):
    # Load the watermark and template PDFs
    template = PyPDF2.PdfReader(input_pdf)
    watermark = PyPDF2.PdfReader(watermark_pdf)

    # Prepare a writer for the output
    output = PyPDF2.PdfWriter()
    output_file_name = os.path.splitext(
        input_pdf)[0] + '_watermarked_output.pdf'

    # Apply the watermark to each page
    for page in template.pages:
        watermark_page = watermark.pages[0]
        page.merge_page(watermark_page)
        output.add_page(page)

    # Write the watermarked PDF to disk
    with open(output_file_name, 'wb') as output_file:
        output.write(output_file)
    print(f"Watermarked: {input_pdf} -> {output_file_name}")


# Process each input PDF
for file in input_pdf_list:
    watermark(watermark_pdf, file)
