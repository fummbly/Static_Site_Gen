from os import listdir, path, mkdir
from shutil import rmtree, copy


def check_directory(dest_directory):
    # if the directory isn't a directory and it exists then raise exception
    if not path.isdir(dest_directory) and path.exists(dest_directory):
        raise Exception(f"{dest_directory} is not a directory")
    # if the path exists and the len is > 0 remove the directory
    if path.exists(dest_directory) and len(listdir(dest_directory)) > 0:
        rmtree(dest_directory)
    # if the path doesn't exist create directory
    if not path.exists(dest_directory):
        mkdir(dest_directory)


def copy_dir(current_directory, dest_directory):
    # if the current directory isn't a directory or it doesn't exist raise error
    if not path.isdir(current_directory) or not path.exists(current_directory):
        raise Exception(
            f"{current_directory} doesn't exist or isn't a directory ")

    items = listdir(current_directory)
    # loop through each item
    for item in items:
        # get the full file path
        file_path = path.join(current_directory, item)
        # if it is a file
        if path.isfile(file_path):
            # copy to destination directory
            copy(file_path, dest_directory)
        # if the item is a directory
        if path.isdir(file_path):
            # create the folder path
            folder_path = path.join(dest_directory, item)
            # if it doesn't already exist create the directory
            if not path.exists(folder_path):
                mkdir(folder_path)
            # recursively loop through that directory
            copy_dir(file_path, folder_path)


def main():
    check_directory("./public")
    copy_dir("./src", "./public")


main()
