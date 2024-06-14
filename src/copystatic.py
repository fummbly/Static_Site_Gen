from os import listdir, path, mkdir
from shutil import copy


def copy_dir(current_directory, dest_directory):
    # if the current_directory doesn't exist then raise exception
    if not path.exists(current_directory) or not path.isdir(current_directory):
        raise Exception(f"{current_directory} doesn't exist or isn't a directory")

    # if the destination path doesn't exist make it
    if not path.exists(dest_directory):
        mkdir(dest_directory)

    # loop through each file in the directory
    for file in listdir(current_directory):
        from_path = path.join(current_directory, file)
        to_path = path.join(dest_directory, file)
        # if it is a file copy it 
        if path.isfile(from_path):
            print(f"Copying {from_path} -> {to_path}")
            copy(from_path, to_path)
        # otherwise recursively go through 
        else:
            copy_dir(from_path, to_path)
