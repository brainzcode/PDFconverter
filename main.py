from PyPDF2 import PdfFileMerger, PdfFileReader
merger = PdfFileMerger()

merger.append(PdfFileReader(open("dummy.pdf", 'rb')))
merger.append(PdfFileReader(open("twopage.pdf", 'rb')))

merger.write("merged.pdf")



# import PyPDF2
# import sys
#
# inputs = sys.argv[1:]
#
#
# def pdf_combiner(pdf_list):
#     for pdf in pdf_list:
#         print(pdf)
#
# pdf_combiner(inputs)