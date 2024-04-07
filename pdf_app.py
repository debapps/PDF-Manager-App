# PDF Manager Application

# This is PDF manager application. It has following functionalities:
# 1. User input the path of a PDF file. The application extracts all the text from the file 
#    and write them into a text file.
# 2. User input the path of a PDF file and list of page numbers of the file. 
#    The application creates a new PDF document using the page numbers.
# 3. Merge PDF documents into a single document when user provides the input path of the PDFs.

# This application is desktop application using text base input/output.

from pdf_manage import PDFManager
import os

# All the functions.
def clear_screen():
    """This function clears the console."""
    os.system('clear' if os.name == 'posix' else 'cls')


def get_user_choice():
    print('\n\t\tWelcome to PDF Application')
    print('\t\t--------------------------')

    print('\n\t1. Extract Text from a PDF File.')
    print('\t2. Crop a PDF File to create new PDF file.')
    print('\t3. Merge multiple of PDF files into a single PDF file.')
    print('\t4. Exit application.')
    choice = int(input('\n\tEnter Your Choice: '))
    return choice


def extract():
    print('\n\tExtract Text from PDF file')
    print('\t--------------------------\n')
    input_pdf_file = input('\tFull path of your PDF file: ').replace('\\', '/')
    output_text_file = input('\tFull path of the output text file: ').replace('\\', '/')

    pdf = PDFManager(input_pdf_file)
    pdf.extract_pdf_text(output_text_file)


def crop():
    print('\n\tCrop PDF file')
    print('\t-------------\n')
    input_pdf_file = input('\tFull path of your PDF file: ').replace('\\', '/')
    page_list_prompt = """\n\tNow you will enter list of pages to crop from your PDF file. The page number
    is you enter in whole number. When you finish entering page numbers, just enter any keyboard character
    to stop input.\n"""
    print(page_list_prompt)
    page_list = []

    will_input = True
    while will_input: 
        try: 
            page = int(input('\tEnter page number - '))
            page_list.append(page)
        except ValueError:
            will_input = False
    
    output_pdf_file = input('\tFull path of Output PDF file: ').replace('\\', '/')

    pdf = PDFManager(input_pdf_file)
    pdf.crop_pdf_file(page_list, output_pdf_file)


def merge():
    print('\n\tMerge multiple PDF files')
    print('\t------------------------\n')
    input_pdf_path = input('\tFull path where your PDF files reside: ').replace('\\', '/')
    output_pdf_file = input('\tFull path of the Output PDF file (After Merge): ').replace('\\', '/')

    pdf = PDFManager(input_pdf_path)
    pdf.merge_pdf(output_pdf_file)


def stop():
    print('\n\tGood Bye!\n')
    global app_active 
    app_active = False
    clear_screen()

# Main Program flow.
app_active = True
while app_active:
    choice = get_user_choice()

    match choice:
        case 1:
            extract()
        case 2:
            crop()
        case 3:
            merge()
        case 4:
            stop()

