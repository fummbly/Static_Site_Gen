from os import listdir, path, mkdir
from shutil import rmtree, copy



def copy_dir(current_directory, dest_directory):

    if not path.isdir(current_directory) or not path.exists(current_directory):
        raise Exception(
            f"{current_directory} doesn't exist or isn't a directory ")

    if not path.exists(dest_directory):
        mkdir(dest_directory)


    # loop through each item
    for file in listdir(current_directory):
        # get the full file path
        from_path = path.join(current_directory, file)
        to_path = path.join(dest_directory, file)
        # if it is a file
        if path.isfile(from_path):
            # copy to destination directory
            copy(from_path, to_path)
        # if the item is a directory
        else:
            copy_dir(from_path, to_path)
