from shutil import rmtree
from generate_html import generate_pages_recursive
from copystatic import copy_dir


def main():

    rmtree("./public")
    copy_dir("./static", "./public")
    generate_pages_recursive("./content", "./template.html", "./public")

main()
