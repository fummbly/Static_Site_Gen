from shutil import rmtree
from copystatic import copy_dir

def main():
    rmtree("./public")
    copy_dir("./static", "./public")


main()
