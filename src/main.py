from textnode import *

def main():
    node1 = TextNode("This is test text.", TextType.BOLD)
    node2 = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")

    print(node1)
    print(node2)

main()