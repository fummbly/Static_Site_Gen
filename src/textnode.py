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
