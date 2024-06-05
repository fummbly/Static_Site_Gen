from textnode import TextNode


def main():
    firstNode = TextNode("Test text body", "Bold")

    secondNode = TextNode("Another text node", "Italic", "http://google.com")

    thirdNode = TextNode("Test text body", "Bold")

    print(firstNode)
    print(secondNode)
    print(thirdNode)

    if firstNode == secondNode:
        print("First node equals second node")
    else:
        print("First node doesn't equal second node")

    if firstNode == thirdNode:
        print("First node equals third node")
    else:
        print("First node doesn't equal third node")


main()
