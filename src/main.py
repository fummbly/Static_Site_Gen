from htmlnode import ParentNode, LeafNode
from inline_markdown import extract_markdown_images, split_nodes_image, split_nodes_links, text_to_text_nodes
from textnode import TextNode

def main():
    text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
    print(text_to_text_nodes(text))


main()
