import re
from textnode import (
    TextNode,
    text_type_text,
)


# Function for splitting nodes into inline blocks of nodes
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # list of new split nodes
    new_nodes = []
    for old_node in old_nodes:
        # if a node isn't a text type node then add it to the list and continue
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue

        split_nodes = []
        # split the text of the node on the delimiter
        sections = old_node.text.split(delimiter)
        # if the length is even then the delimiter isn't closed and raise value error
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            # if a section of the text is blank just ignore it
            if sections[i] == "":
                continue
            # if the index is even it has to be outside of the delimiter
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    # return the new nodes
    return new_nodes
