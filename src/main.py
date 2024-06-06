from textnode import TextNode


def main():
    # Initializing TextNodes 
    firstNode = TextNode("Test text body", "Bold")
    secondNode = TextNode("Another text node", "Italic", "http://google.com")
    thirdNode = TextNode("Test text body", "Bold")
    
    # Testing printing of TextNodes
    print(firstNode)
    print(secondNode)
    print(thirdNode)

    # Testing equal function of TextNodes
    # Should return false
    if firstNode == secondNode:
        print("First node equals second node")
    else:
        print("First node doesn't equal second node")

    # Should return true
    if firstNode == thirdNode:
        print("First node equals third node")
    else:
        print("First node doesn't equal third node")


main()
