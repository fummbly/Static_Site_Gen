import re

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
    if re.match(r"^#{1, 6}", block):
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
