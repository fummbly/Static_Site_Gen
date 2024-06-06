import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

    # Testing LeafNode for proper html formating
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")

        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    # Testing no tag html formating
    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")

        self.assertEqual(node.to_html(), "Hello, world!")

    # Testing tag with props
    def test_to_html_props(self):
        node = LeafNode("a", "Google", {"href": "https://www.google.com"})

        self.assertEqual('<a href="https://www.google.com">Google</a>', node.to_html())

    # Testing exception for no value
    def test_to_html_no_value(self):
        node = LeafNode(None, None)

        self.assertRaises(ValueError, node.to_html)


    def test_parent_with_leafs(self):
        node = ParentNode(
            "p",
            [
                LeafNode("a", "Link text"),
                LeafNode("b", "Bold text"),
                LeafNode("i", "Italic text"),
            ]
        )

        self.assertEqual("<p><a>Link text</a><b>Bold text</b><i>Italic text</i></p>", node.to_html())

    def test_nested_parents(self):
        node = ParentNode(
            "p",
            [
                ParentNode("div", [
                    ParentNode("p", [
                        LeafNode("a", "Link text"),
                        LeafNode("a", "Link text"),
                        LeafNode("a", "Link text"),
                    ]),
                ]),
            ]
        )

        self.assertEqual("<p><div><p><a>Link text</a><a>Link text</a><a>Link text</a></p></div></p>", node.to_html())

    def test_parent_props(self):
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "div",
                    [
                        LeafNode("a", "Click here", {"href": "https://www.google.com"}),
                        LeafNode("img", "Image", {"alt-text": "An image of a dog"}),
                        LeafNode("p", "Paragraph")
                    ],
                    {
                        "class": "nav",     
                    }
                ),
                LeafNode("a", "Link to boot.dev", {"href": "https://www.boot.dev"}),
                LeafNode("p", "Second Paragraph"),
            ],
            {
                "class": "center",
            }
        )

        self.assertEqual('<p class="center"><div class="nav"><a href="https://www.google.com">Click here</a><img alt-text="An image of a dog">Image</img><p>Paragraph</p></div><a href="https://www.boot.dev">Link to boot.dev</a><p>Second Paragraph</p></p>', node.to_html())



if __name__ == "__main__":
    unittest.main()
