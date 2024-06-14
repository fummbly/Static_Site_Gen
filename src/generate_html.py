from shutil import rmtree
from os import path
from block_markdown import markdown_to_blocks, markdown_to_html_node
from copystatic import copy_dir


# extract page title from markdown
def extract_title(markdown):
    # split the markdown into blocks
    blocks = markdown_to_blocks(markdown)
    lines = []
    # get the lines
    for block in blocks:
        lines.extend(block.split("\n"))
    # loop through the lines for an h1 tag 
    for line in lines:
        if line.startswith("# "):
            return line.lstrip("#").strip()
    
    # if it is not found raise exception
    raise Exception("No title found")

# Generate HTML page from markdown
def generate_page(from_path, template_path, to_path):
    print(f"Generating page from {from_path} to {to_path} with {template_path}")
    # remove the public dir if exists
    if path.exists("./public"):
        rmtree("./public")

    copy_dir("./static", "./public")

    # open markdown page and put it into markdown variable
    markdown = ""
    with open(from_path, 'r') as f:
        markdown = f.read()
        f.close()

    # open template page and put it into template variable
    template = ""
    with open(template_path, 'r') as f:
        template = f.read()
        f.close()
        
    # extract title
    title = extract_title(markdown)
    # create html content
    content = markdown_to_html_node(markdown).to_html()

    # create the new paage
    new_page = template
    # replace the title placeholder with the title
    new_page = new_page.replace("{{ Title }}", title)
    # replace the content placeholder with the content
    new_page = new_page.replace("{{ Content }}", content)

    # write the file 
    with open(to_path, 'w') as f:
        f.write(new_page)
        f.close()


    


