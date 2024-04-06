# This is PDF manager application. It has following functionalities:
# 1. Merge PDF documents into a single document when user provides the input path of the PDFs.
# 2. User input the path of a PDF file and list of page numbers of the file. The application create a new
# PDF document using the page numbers.
# 3. User input the path of a PDF file. The application extract all the text from the file and write them
# into a text file.

# This application is desktop application using text base input/output.

from pdf_manage import PDFManager

def convert_page_number(in_list):
    """This function converts the range into page numbers."""

    out_list = []
    for item in in_list:
        if type(item) is list:
            for num in range(item[0], item[1] + 1, 1):
                out_list.append(num)
        else:
            out_list.append(item)
    
    return out_list


def get_user_choice():
    print('\n\t\tWelcome to PDF Application')
    print('\t\t--------------------------')

    print('\n\t1. Extract Text from a PDF File.')
    print('\t2. Crop a PDF File to create new PDF file.')
    print('\t3. Merge multiple of PDF files into a single PDF file.')
    choice = int(input('\n\tEnter Your Choice: '))


choice = get_user_choice()

# page_num = convert_page_number([1,3,5, [10, 17], 23])
# print(page_num)

# pdf : PDFManager = PDFManager(r'D:/MyLearning/AWS/AWS Notes/PDF Notes/Developer Associate Services')

# pdf.extract_pdf_text(r'D:/Personal/My Resume/resume.txt')

# pdf.crop_pdf_file([0,1,4], r'D:/Personal/My Resume/346863_short_resume.pdf')

# pdf.merge_pdf(r'D:/MyLearning/AWS/AWS Notes/PDF Notes/all.pdf')

