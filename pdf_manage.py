# This module is the PDF manager module. It contains all the codes responsible for handling PDF files.

from pypdf import PdfReader, PdfWriter
import os

class PDFManager:

    def __init__(self, path) -> None:
        self.pdf_path = path

    def get_file_ext(self, file_path):
        """This function returns the file extension when a file path is input."""
        return os.path.splitext(file_path)[1].replace('.', '').lower()


    def extract_pdf_text(self, out_file_path):
        """This function takes output text file path and extract all the text from PDF file into it."""

        if os.path.isdir(self.pdf_path) or self.get_file_ext(self.pdf_path) != 'pdf':
            print('Error: The PDFManager is not initialize with PDF file.')
            return None
        
        if self.get_file_ext(out_file_path) != 'txt':
            print('Error: Please enter output file path of a text file with .txt extension.')
            return None
        
        
        # Initialize the PDF reader and extract text
        reader = PdfReader(self.pdf_path)
        extract_text = []

        print('\n\tExtracting text from PDF file..')
        # For all the pages, extract the text.
        for page in reader.pages:
            extract_text.append(page.extract_text())

        with open(out_file_path, 'w', encoding='utf-8') as output:
            output.writelines(extract_text)
        print('\tText is saved successfully into output file.\n')

    
    def crop_pdf_file(self, page_list, out_pdf_file):
        """The user input the list of pages and output PDF file. This function gets the specific pages
        from the pdf and save those pages into output PDF file."""

        if os.path.isdir(self.pdf_path) or self.get_file_ext(self.pdf_path) != 'pdf':
            print('Error: The PDFManager is not initialize with PDF file.')
            return None
        
        if self.get_file_ext(out_pdf_file) != 'pdf':
            print('Error: Please enter output file as PDF file with .pdf extension.')
            return None
        
        # Initialize the PDF Reader and Writer.
        reader = PdfReader(self.pdf_path)
        writer = PdfWriter()
        
        # Get the pages to be written into new file.
        for pagenum in page_list:
            writer.add_page(reader.pages[pagenum])

        with open(out_pdf_file, 'wb') as fp:
            writer.write(fp)

        print('\n\tPages are saved successfully into output file.\n')

    def merge_pdf(self, out_pdf_file):
        """This function takes input the output pdf file full path. It merges all the pdf file in
        the specific path and write it into output pdf file."""

        if os.path.isfile(self.pdf_path):
            print('Error: The PDFManager is not initialize Directory path where all input PDF files reside.')
            return None
        else:
            # Change the current working directory
            os.chdir(self.pdf_path)

        
        if self.get_file_ext(out_pdf_file) != 'pdf':
            print('Error: Please enter output file as PDF file with .pdf extension.')
            return None
        
        # Get the list of PDF files.
        pdf_files = [file for file in os.listdir(self.pdf_path) 
                     if self.get_file_ext(file) == 'pdf']
        
        if len(pdf_files) == 0:
            print(f'Error: There is no PDF file in Directory - {self.pdf_path}')
            return None

        # Initialize the merger object.
        merger = PdfWriter()

        # Merge the pdf files in the pdf file list.
        print('\n')
        for pdf in pdf_files:
            merger.append(pdf)
            print(f'\tMerging PDF file - {pdf}')

        # Write the merged output into the file and close the merger.
        print(f'\n\tMerged all PDF Files into {out_pdf_file}\n')
        merger.write(out_pdf_file)
        merger.close()

        
        


        
        



          





