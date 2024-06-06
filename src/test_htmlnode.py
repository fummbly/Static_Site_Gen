import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    # Testing props_to_html function for proper formating
    def test_props_to_html(self):
        node = HTMLNode("a", "Link to image", None, {"href": "https://www.google.com", "target": "_blank"})
    
        self.assertEqual(' href="https://www.google.com" target="_blank"', node.props_to_html())

    # Testing that nodes are created correctly
    def test_repr(self):
        node = HTMLNode("p", "This is a paragraph")
        node2 = HTMLNode("a", "This is a link", None, {"href": "https://www.google.com"})

        self.assertEqual("HTMLNode(Tag: p, Value: This is a paragraph, Children: None, Props: None)", repr(node))
        self.assertEqual("HTMLNode(Tag: a, Value: This is a link, Children: None, Props: {'href': 'https://www.google.com'})", repr(node2))
