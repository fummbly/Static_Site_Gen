from block_markdown import markdown_to_html_node
from htmlnode import ParentNode

def main():
    text = """
# My main heading

### A smaller heading

* Item 
* Another 
* and this one is **special**

>This is a quote
>And Another

```
Some code
```

And this is
just a paragraph


"""
    print(markdown_to_html_node(text).to_html())

    
main()

