# HTML Node for representing a single html tag
class HTMLNode:
    # Constructor that defaults to none on any of the properties
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    # to_html function for children to override
    def to_html(self):
        raise NotImplementedError("Not Implemented")

    # props_to_html function to format props into html format
    def props_to_html(self):
        if not self.props:
            return ""

        html_rep = ""
        for prop in self.props:
            html_rep += f' {prop}="{self.props[prop]}"'

        return html_rep


    # String representation of HTMLNode for debugging
    def __repr__(self):
        return f"HTMLNode(Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props})"


# Child of HTMLNode
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode(Tag: {self.tag}, Value: {self.value}, Props: {self.props})"

# ParentNode to hold other nodes inside it
class ParentNode(HTMLNode):
    # Init with requirement for children
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    # to html override with exceptions for tag and children
    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")

        if self.children is None:
            raise ValueError("Invalid HTML: no children")

        # Starting of formated output with parentnode tag and props
        html = f"<{self.tag}{self.props_to_html()}>"

        # For each child call the to_html function on it
        for child in self.children:
            html += child.to_html()

        # append the final parentnode tag
        html += f"</{self.tag}>"
        return html

