import PyPDF2
import os

def merge_pdfs(folder_path, num_pdfs, output_filename):
    merger = PyPDF2.PdfMerger()
    pdf_files = [file for file in os.listdir(folder_path) if file.endswith(".pdf")]

    if num_pdfs > len(pdf_files):
        print(f"Number of PDFs to merge exceeds available PDFs in the folder ({len(pdf_files)}). Merging all available PDFs.")
        num_pdfs = len(pdf_files)

    for file in pdf_files[:num_pdfs]:
        merger.append(os.path.join(folder_path, file))

    merger.write(output_filename)
    merger.close()
    print(f"Merged {num_pdfs} PDFs into {output_filename}")

folder_path = input("Enter the folder path containing the PDFs: ")
num_pdfs = int(input("Enter the number of PDFs to merge: "))
output_filename = input("Enter the output filename (including .pdf extension): ")

merge_pdfs(folder_path, num_pdfs, output_filename)
