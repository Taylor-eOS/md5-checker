import os
import hashlib

#Calculates the MD5 checksum for the given file.
def calculate_md5(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

#Checks if the file name contains the MD5 checksum.
def check_filename_contains_md5(file_name, md5_checksum):
    return md5_checksum in file_name

def main():
    folder_path = os.path.dirname(os.path.abspath(__file__))
    files_in_directory = os.listdir(folder_path)
    
    for file_name in files_in_directory:
        file_path = os.path.join(folder_path, file_name)
        if file_name == os.path.basename(__file__): #Exclude the script itself
            continue
        if os.path.isfile(file_path):
            md5_checksum = calculate_md5(file_path)
            if check_filename_contains_md5(file_name, md5_checksum):
                print(f"ok")
            else:
                print(f"Warning: File {file_name} does NOT contain the MD5 checksum.")

if __name__ == "__main__":
    main()
