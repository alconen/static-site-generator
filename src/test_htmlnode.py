import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_HTMLNode_props_to_html(self):
        node = HTMLNode("a", "site", [], {"href": "https://www.google.com", "blah": "blah"})
        self.assertEqual(node.props_to_html(), 
                         ' href="https://www.google.com" blah="blah"')
    
    def test_HTMLNode_repr(self):
        node = HTMLNode("a", "site", [], {"href": "https://www.google.com", "blah": "blah"})
        self.assertEqual(repr(node), 
                         "HTMLNode(a, site, [], {'href': 'https://www.google.com', 'blah': 'blah'}")
class TestLeafNode(unittest.TestCase):
    def test_LeafNode_repr(self):
        node = LeafNode("a", "site", {"href": "https://www.google.com", "blah": "blah"})
        self.assertEqual(repr(node), 
                         "LeafNode(a, site, {'href': 'https://www.google.com', 'blah': 'blah'}")
        
    def test_LeafNode_to_html(self):
        node = LeafNode("a", "site", {"href": "https://www.google.com", "blah": "blah"})
        self.assertEqual(node.to_html(),
                        "<a href=\"https://www.google.com\" blah=\"blah\">site</a>")

    def test_LeafNode_null_props(self):
        node = LeafNode("a", "site")
        self.assertEqual(node.to_html(),
                         "<a>site</a>")
    
    def test_LeafNode_null_value(self):
        self.assertRaises(ValueError, LeafNode().to_html)

    def test_LeafNode_null_tag(self):
        node = LeafNode(None, "site")
        self.assertEqual(node.to_html(),
                         "site")
            
class TestParentNode(unittest.TestCase):
    def test_ParentNode_repr(self):
        node = ParentNode(
            [
                LeafNode("a", "site", {"href": "https://www.google.com", "blah": "blah"})
            ], 
            "p", 
            {'href': 'https://www.google.com', 'blah': 'blah'})
        self.assertEqual(repr(node), 
                         "ParentNode(p, [LeafNode(a, site, {'href': 'https://www.google.com', 'blah': 'blah'}], {'href': 'https://www.google.com', 'blah': 'blah'})")

    def test_ParentNode_to_html_non_nested(self):
        node = ParentNode(
            [
                LeafNode("a", "site", {"href": "https://www.google.com", "blah": "blah"}),
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
            ], 
            "p", 
            {'href': 'https://www.google.com', 'blah': 'blah'})
        self.assertEqual(node.to_html(),
                         "<p href=\"https://www.google.com\" blah=\"blah\"><a href=\"https://www.google.com\" blah=\"blah\">site</a><b>Bold text</b>Normal text</p>")

    def test_ParentNode_to_html_one_nest(self):
        node = ParentNode(
            [
                LeafNode("a", "site", {"href": "https://www.google.com", "blah": "blah"}),
                LeafNode("b", "Bold text"),
                ParentNode(
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                    ], "h1")
            ], 
            "p", 
            {'href': 'https://www.google.com', 'blah': 'blah'})
        self.assertEqual(node.to_html(),
                         "<p href=\"https://www.google.com\" blah=\"blah\"><a href=\"https://www.google.com\" blah=\"blah\">site</a><b>Bold text</b><h1><b>Bold text</b>Normal text</h1></p>")

    def test_ParentNode_to_html_multi_nest(self):
        node = ParentNode(
            [
                LeafNode("a", "site", {"href": "https://www.google.com", "blah": "blah"}),
                LeafNode("b", "Bold text"),
                ParentNode(
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                    ], "h1"),
                ParentNode(
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        ParentNode(
                            [
                                LeafNode("b", "Bold text"),
                                LeafNode(None, "Normal text"),
                            ], "h1")
                    ], "h1"),
            ], 
            "p", 
            {'href': 'https://www.google.com', 'blah': 'blah'})
        self.assertEqual(node.to_html(),
                         "<p href=\"https://www.google.com\" blah=\"blah\"><a href=\"https://www.google.com\" blah=\"blah\">site</a><b>Bold text</b><h1><b>Bold text</b>Normal text</h1><h1><b>Bold text</b>Normal text<h1><b>Bold text</b>Normal text</h1></h1></p>")
        
if __name__ == "__main__":
    unittest.main()