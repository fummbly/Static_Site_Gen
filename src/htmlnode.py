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

