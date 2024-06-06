from htmlnode import ParentNode, LeafNode


def main():
    parent = ParentNode(
        "p", 
        [
            ParentNode("div", [
                LeafNode("p", "another paragraph", {"class": "center"})
            ]),
            LeafNode(None, "Normal text"),
            LeafNode("i", "Italic text")
        ],
    )

    parent.to_html()


main()
