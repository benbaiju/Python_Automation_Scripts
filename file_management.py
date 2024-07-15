import os
import shutil

def organize_files(source_dir):
    file_types = {
        'txt': 'TextFiles',
        'pdf': 'PDFs',
        'jpg': 'Images',
        'png': 'Images',
        'xlsx': 'Spreadsheets',
        'docx': 'Documents',
        'mp4': 'Videos',
        'mp3': 'Music',
        'csv': 'Excel'
    }
    
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        
        if os.path.isfile(file_path):
            _, file_extension = os.path.splitext(filename)
            file_extension = file_extension.lstrip('.').lower()
            
            if file_extension in file_types:
                destination_folder = os.path.join(source_dir, file_types[file_extension])
            else:
                destination_folder = os.path.join(source_dir, 'OtherFiles')
            
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            
            shutil.move(file_path, os.path.join(destination_folder, filename))
            print(f"Moved {filename} to {destination_folder}")

if __name__ == "__main__":
    source_directory = input("Enter the path of the directory to organize: ")
    organize_files(source_directory)
