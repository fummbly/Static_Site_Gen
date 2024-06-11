import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_links,
    split_nodes_image,
    text_to_text_nodes
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_code,
    text_type_italic
)


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text)
            ],
            new_nodes
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This text has two **bolded** text and the other is **here**", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This text has two ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" text and the other is ", text_type_text),
                TextNode("here", text_type_bold)
            ],
            new_nodes
        )

    def test_delim_italic(self):
        node = TextNode("This text has *italic* text", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This text has ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" text", text_type_text),
            ],
            new_nodes
        )

    def test_delim_code(self):
        node = TextNode("This text has a `code` block", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This text has a ", text_type_text),
                TextNode("code", text_type_code),
                TextNode(" block", text_type_text)
            ],
            new_nodes
        )

    def test_extract_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        extracted_images = extract_markdown_images(text)
        self.assertListEqual(
            [
                ('image', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png'), ('another',
                                                                                                                     'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png')
            ],
            extracted_images
        )

    def test_extract_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        extracted_links = extract_markdown_links(text)
        self.assertListEqual(
            [
                ('link', 'https://www.example.com'), ('another',
                                                      'https://www.example.com/another')
            ],
            extracted_links
        )

    def test_split_nodes_images(self):
        node = TextNode("This is text with an ![image](https://www.google.com/dog)", text_type_text)
        extracted_images = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", "image", "https://www.google.com/dog"),
            ],
            extracted_images
        )
        

    def test_split_nodes_links(self):
        node = TextNode("This is text with a [link](https://www.boot.dev)", text_type_text)
        extracted_links = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("link", "link", "https://www.boot.dev"),
            ],
            extracted_links
        )

    def test_split_nodes_multiple(self):
        node = TextNode("This is a normal text block", text_type_text)
        node2 = TextNode("This text block has a [link](https://www.google.com)", text_type_text)
        extracted_links = split_nodes_links([node, node2])
        self.assertListEqual(
            [
                TextNode("This is a normal text block", text_type_text),
                TextNode("This text block has a ", text_type_text),
                TextNode("link", "link", "https://www.google.com")
            ],
            extracted_links
        )

    def test_text_to_text_nodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        nodes = text_to_text_nodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code), 
                TextNode(" and an ", text_type_text),
                TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", "link", "https://boot.dev"),
            ],
            nodes
        )




if __name__ == "__main__":
    unittest.main()
