from os import listdir, path, mkdir
from shutil import rmtree, copy

check_directory(dest_directory):


def copy_static(current_directory, dest_directory):
    
    if not path.isdir(current_directory) or not path.exists(current_directory):
        raise Exception(f"{current_directory} doesn't exist or isn't a directory ")

        

    if not path.exists(public_path):
        print("Making dir")
        mkdir(public_path)

    items = listdir(current_directory)
    for item in items:
        file_path = path.join(current_directory, item)
        if path.isfile(file_path):
            print(f"Copying file {file_path}")
            copy(file_path, public_path)
        if path.isdir(file_path):
           copy_static(file_path) 



def main():
    copy_static(".")
main()

