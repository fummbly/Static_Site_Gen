from block_markdown import markdown_to_html_node
import unittest

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_html(self):
         
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

        self.assertEqual("<div><h1>My main heading</h1><h3>A smaller heading</h3><ul><li>Item </li><li>Another </li><li>and this one is <b>special</b></li></ul><blockquote>This is a quote And Another</blockquote><pre><code>Some code</code></pre><p>And this is just a paragraph</p><p></p></div>", markdown_to_html_node(text).to_html())


if __name__ == "__main__":
    unittest.main()
