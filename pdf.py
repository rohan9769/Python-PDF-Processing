
import sys
import PyPDF2

#basic
#working with Dummy.pdf(Basics)
# with open('twopage.pdf','rb') as file: #rb means read as binary,converts file object to binary mode so that PyPDF2 filereader can read this binary object
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf','wb') as new_file:
#         writer.write(new_file)


#Merging PDF's (superPDF.pdf)
# inputs = sys.argv[1:]
# def PDF_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('superPDF.pdf')
#
# PDF_combiner(inputs)


#Adding Watermarks to the combined PDF that is superPDF (watermarked.pdf)

template = PyPDF2.PdfFileReader(open('superPDF.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermaked.pdf','wb') as file:
        output.write(file)



