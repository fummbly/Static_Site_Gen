
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, OtherTextNode):
        if self.text == OtherTextNode.text:
            if self.text_type == OtherTextNode.text_type:
                if self.url == OtherTextNode.url:
                    return True

        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
