import unittest

from textnode import TextNode


class TestTextNodeClass(unittest.TestCase):
    def test_eq_1(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("hello", "bold", None)
        node2 = TextNode("hello", "bold")
        self.assertEqual(node, node2)

    def test_eq_3(self):
        node = TextNode("blah", "bold", "example.com")
        node2 = TextNode("blah2", "bold", "example.com")
        self.assertNotEqual(node, node2)

    def test_eq_4(self):
        node = TextNode("blah", "bold", "example.com")
        node2 = TextNode("blah", "bold2", "example.com")
        self.assertNotEqual(node, node2)

    def test_eq_5(self):
        node = TextNode("blah", "bold", "example.com")
        node2 = TextNode("blah", "bold", "ex2ample.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()