from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode

            


def main():
    node = TextNode("blah", "bold", "https://example.com")
    print(node)
    node = HTMLNode("a", "site", [], {"href": "https://www.google.com", "blah": "blah"})
    print(node)
    node = LeafNode("a", "site", {"href": "https://www.google.com", "blah": "blah"})
    print(node.to_html())


main()