import unittest

from htmlnode import LeafNode
from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node2", "bold")
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", "italic", "https://www.google.com")
        node2 = TextNode("This is a text node", "italic", "https://www.google.com")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual("TextNode(This is a text node, bold, None)", repr(node))

    def test_text_to_html(self):
        node = TextNode("This is a bold text node", "bold")
        node2 = TextNode("This is a italic node", "italic")
        node3 = TextNode("This is an image node", "image", "https://dog.png")
        node4 = TextNode("This is a blank text node", "text")

        self.assertEqual("<b>This is a bold text node</b>", node.text_node_to_html_node().to_html())
        self.assertEqual("<i>This is a italic node</i>", node2.text_node_to_html_node().to_html())
        self.assertEqual('<img src="https://dog.png" alt="This is an image node"></img>', node3.text_node_to_html_node().to_html())
        self.assertEqual("This is a blank text node", node4.text_node_to_html_node().to_html())

    def test_invalid_text_type(self):
        node = TextNode("Another text node with incorrect type", "Big")

        self.assertRaises(Exception, node.text_node_to_html_node)


if __name__ == "__main__":
    unittest.main()



