import unittest

from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes
)

from textnode import TextNode

class TestNodeSplit(unittest.TestCase):
    def test_node_split_1(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertEqual(repr(new_nodes),
                         "[TextNode(This is text with a , text, None), TextNode(code block, code, None), TextNode( word, text, None)]")
    
    def test_node_split_2(self):
        nodes = [
            TextNode("This is text with **two** bold **words**", "text"),
            TextNode("**This** is also text with two **bold** words", "text"),
            TextNode("This is bold text", "bold")
        ]
        new_nodes = split_nodes_delimiter(nodes, "**", "bold")
        self.assertEqual(repr(new_nodes),
                         "[TextNode(This is text with , text, None), TextNode(two, bold, None), TextNode( bold , text, None), TextNode(words, bold, None), TextNode(This, bold, None), TextNode( is also text with two , text, None), TextNode(bold, bold, None), TextNode( words, text, None), TextNode(This is bold text, bold, None)]")

    def test_node_split_3(self):
        nodes = [
            TextNode("This is *text* with *two* italic words", "text"),
            TextNode("*This* is *text*  with *many italic words*", "text"),
            TextNode("This is bold text", "bold")
        ]
        new_nodes = split_nodes_delimiter(nodes, "*", "italic")
        self.assertEqual(repr(new_nodes),
                         "[TextNode(This is , text, None), TextNode(text, italic, None), TextNode( with , text, None), TextNode(two, italic, None), TextNode( italic words, text, None), TextNode(This, italic, None), TextNode( is , text, None), TextNode(text, italic, None), TextNode(  with , text, None), TextNode(many italic words, italic, None), TextNode(This is bold text, bold, None)]")

class TestImageExtract(unittest.TestCase):
    def test_extract_image(self):
        text = "This is text with ![image](example-link.com) and ![image2](example-link2.com)"
        self.assertEqual(extract_markdown_images(text),
                         [
                             ("image","example-link.com"),
                             ("image2","example-link2.com")
                         ])

class TestLinkExtract(unittest.TestCase):
    def test_extract_link(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        self.assertEqual(extract_markdown_links(text),
                          [
                              ("link", "https://www.example.com"),
                              ("another", "https://www.example.com/another")
                          ])
        
class TestImageSplit(unittest.TestCase):
    def test_node_split_1(self):
        node = TextNode("This is text with one ![image](example.com)", "text")
        new_nodes = split_nodes_image([node])
        self.assertEqual(repr(new_nodes),
                         "[TextNode(This is text with one , text, None), TextNode(image, img, example.com)]")
    
    def test_node_split_2(self):
        node = TextNode("This is text with two ![image](example.com) , ![another](example.com) blah", "text")
        new_nodes = split_nodes_image([node])
        self.assertEqual(repr(new_nodes),
                         "[TextNode(This is text with two , text, None), TextNode(image, img, example.com), TextNode( , , text, None), TextNode(another, img, example.com), TextNode( blah, text, None)]")
        
class TestSplit(unittest.TestCase):
    def test_node_split_1(self):
        node = TextNode("This is text with one [link](example.com)", "text")
        new_nodes = split_nodes_link([node])
        self.assertEqual(repr(new_nodes),
                         "[TextNode(This is text with one , text, None), TextNode(link, link, example.com)]")
    
    def test_node_split_2(self):
        node = TextNode("This is text with two [link](example.com) , [link2](example2.com) blah", "text")
        new_nodes = split_nodes_link([node])
        self.assertEqual(repr(new_nodes),
                         "[TextNode(This is text with two , text, None), TextNode(link, link, example.com), TextNode( , , text, None), TextNode(link2, link, example2.com), TextNode( blah, text, None)]")

class TestTextNodeSplit(unittest.TestCase):
    def test_node_split_1(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        self.assertEqual(repr(text_to_textnodes(text)),
                        "[TextNode(This is , text, None), TextNode(text, bold, None), TextNode( with an , text, None), TextNode(italic, italic, None), TextNode( word and a , text, None), TextNode(code block, code, None), TextNode( and an , text, None), TextNode(image, img, https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png), TextNode( and a , text, None), TextNode(link, link, https://boot.dev)]"
        )