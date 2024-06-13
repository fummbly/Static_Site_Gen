import re
from typing import ParamSpec
from htmlnode import ParentNode, LeafNode 
from inline_markdown import text_to_text_nodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    # split each block on a line break
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        # omit empty strings
        if block == "":
            continue
        # strip whitespace from the block
        block = block.strip()
        new_blocks.append(block)

    return new_blocks


def block_to_block_type(block):
    # split block up into lines
    lines = block.split("\n")
    # if the starts with 1-6 # it has to be a header
    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
            ):
        return block_type_heading
    # if there is more than one line
    if len(lines) > 1:
        # check if the block starts and ends with ```
        if lines[0] == "```" and lines[-1] == "```":
            return block_type_code
    # if the block starts with >
    if block.startswith(">"):
        # check every line for >
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    # if the block starts with '* '
    if block.startswith("* "):
        # check every line for it
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_unordered_list
    # if the block starts with '- '
    if block.startswith("- "):
        # check every line for it
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_unordered_list
    # if the block starts with "1. "
    if block.startswith("1. "):
        # check every line for asseding numbers
        for i in range(len(lines)):
            if not lines[i].startswith(f"{i + 1}. "):
                return block_type_paragraph
        return block_type_ordered_list
    return block_type_paragraph

def create_children_nodes(line):
    # create a list of children
    children = []
    # split the text into indiviual nodes
    text_nodes = text_to_text_nodes(line)
    for node in text_nodes:
        # append each node into the children list
        children.append(text_node_to_html_node(node))
    return children

def create_quote_block(block):
    new_lines = []
    lines = block.split("\n")
    for line in lines:
        # remove the quote character from the text and append it to new lines
        new_lines.append(line[1:])
    # join the lines together for a continus line
    quotes = " ".join(new_lines)
    children = create_children_nodes(quotes)
    quote = ParentNode("blockquote", children)
    return quote


def create_heading(block):
    new_lines = []
    lines = block.split("\n")
    # count the amount # occuring
    heading_number = lines[0].count("#")
    # if the number is greater than 6, invalid heading 
    if heading_number > 6:
        raise ValueError("Invalid heading level")
    for line in lines:
        # loop through the lines and remove the # character and any whitespace
        line = line.lstrip("#")
        line = line.lstrip()
        new_lines.append(line)

    headings = " ".join(new_lines)
    children = create_children_nodes(headings)
    heading = ParentNode(f"h{heading_number}", children)
    return heading
    


def create_code_block(block):
    lines = block.split("\n")
    # remove back ticks from lines
    lines = lines[1:-1]
    code_text = " ".join(lines)
    children = create_children_nodes(code_text)
    code = ParentNode("code", children) 
    pre = ParentNode("pre", [code])
    return pre

def create_paragraph_block(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = create_children_nodes(paragraph)
    return ParentNode("p", children)

def create_unordered_list(block):
    children = []
    lines = block.split("\n")
    for line in lines:
        # remove list marker
        line = line[2:]
        # create list item with children
        list_item = ParentNode("li", create_children_nodes(line))
        # append list item to ul children
        children.append(list_item)
    unordered_list = ParentNode("ul", children)
    return unordered_list

def create_ordered_list(block):
    children = []
    lines = block.split("\n")
    for line in lines:
        line = line[3:]
        list_item = ParentNode("li", create_children_nodes(line))
        children.append(list_item)
    ordered_list = ParentNode("ol", children)
    return ordered_list


def markdown_to_html_node(markdown):
    children = []
    # split markdown into blocks
    blocks = markdown_to_blocks(markdown)
    # create children on each block type
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_quote:
            children.append(create_quote_block(block))
            continue

        if block_type == block_type_heading:
            children.append(create_heading(block))
            continue

        if block_type == block_type_code: 
            children.append(create_code_block(block))
            continue

        if block_type == block_type_unordered_list:
            children.append(create_unordered_list(block))
            continue

        if block_type == block_type_ordered_list:
            children.append(create_ordered_list(block))
            continue

        if block_type == block_type_paragraph:
            children.append(create_paragraph_block(block))
            continue
    div = ParentNode("div", children)
    return div
