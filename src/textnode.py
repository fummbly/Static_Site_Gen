from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    # TextNode constructor with string text, string text_type, string url
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    # Overide equals function where true if all properties of the 2 nodes are equal
    def __eq__(self, OtherTextNode):
        return (
            self.text == OtherTextNode.text
            and self.text_type ==  OtherTextNode.text_type
            and self.url == OtherTextNode.url
        )

    # String representation overide
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    # function for converting text nodes to html nodes
    def text_node_to_html_node(text_node):

        # if in defined types
        if text_node.text_type == text_type_text:
            return LeafNode(None, text_node.text)
        if text_node.text_type == text_type_bold:
            return LeafNode("b", text_node.text)
        if text_node.text_type == text_type_italic:
            return LeafNode("i", text_node.text)
        if text_node.text_type == text_type_code:
            return LeafNode("code", text_node.text)
        if text_node.text_type == text_type_link:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        if text_node.text_type == text_type_image:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        # raise if not found
        raise Exception("Invalid text type")
