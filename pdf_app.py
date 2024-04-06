# This is PDF manager application. It has following functionalities:
# 1. Merge PDF documents into a single document when user provides the input path of the PDFs.
# 2. User input the path of a PDF file and list of page numbers of the file. The application create a new
# PDF document using the page numbers.
# 3. User input the path of a PDF file. The application extract all the text from the file and write them
# into a text file.

# This application is desktop application using text base input/output.

from pdf_manage import PDFManager

pdf : PDFManager = PDFManager(r'D:/Personal/My Resume/Debaditya_Bhar_Resume.pdf')

# pdf.extract_pdf_text(r'D:/Personal/My Resume/resume.txt')

pdf.crop_pdf_file([0,1,4], r'D:/Personal/My Resume/346863_short_resume.pdf')