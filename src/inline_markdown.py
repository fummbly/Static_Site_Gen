import re
from textnode import (
    TextNode,
    text_type_text,
)


# Function for splitting nodes into inline blocks of nodes
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # list of new split nodes
    new_nodes = []
    for node in old_nodes:
        # if a node isn't a text type node then add it to the list and continue
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        split_nodes = []
        # split the text of the node on the delimiter
        sections = node.text.split(delimiter)
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


# extract image links with re findall
def extract_markdown_images(text):
    images = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return images


# extrack links with re findall
def extract_markdown_links(text):
    links = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return links


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            continue
        # save a copy of the nodes text to manipulate
        original_text = node.text
        # extract the image data
        images = extract_markdown_images(original_text)
        # if there is no image data continue
        if not images:
            new_nodes.append(node)
            continue
        for image in images:
            # split the text on the image data
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            # if there is not 2 sections then the image wasn't closed right
            if len(sections) != 2:
                raise ValueError("Incorrect syntax missing closing for image")
            # if the section isn't an empty string append it to new nodes
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], "text"))
            # append the image to new_nodes
            new_nodes.append(TextNode(image[0], "image", image[1]))
            # make original_text the next section
            original_text = sections[1]
        # if original_text is not empty append the last piece
        if original_text != "":
            new_nodes.append(TextNode(original_text, "text"))

    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            continue

        original_text = node.text
        links = extract_markdown_links(original_text)
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})")
            if len(sections) != 2:
                raise ValueError("Incorrect syntax link was not closed")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], "text"))
            new_nodes.append(TextNode(link[0], "link", link[1]))

            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, "text"))
    return new_nodes

def text_to_text_nodes(text):
    nodes = [TextNode(text, "text")]
    nodes = split_nodes_delimiter(nodes, "**", "bold")
    nodes = split_nodes_delimiter(nodes, "*", "italic")
    nodes = split_nodes_delimiter(nodes, "`", "code")
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_links(nodes)
    return nodes







