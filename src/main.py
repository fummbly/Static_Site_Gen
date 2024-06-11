from htmlnode import ParentNode, LeafNode
from inline_markdown import extract_markdown_images


def main():
    text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
    extract_markdown_images(text)


main()
