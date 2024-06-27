import unittest
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "some_url")
        node2 = TextNode("This is a text node", "bold", "some_url")
        self.assertEqual(node, node2)

    def test_eqNoneURL(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)

    def test_eqAllNone(self):
        node = TextNode(None, None, None)
        node2 = TextNode(None, None, None)
        self.assertEqual(node, node2)  

    def test_difType(self):
        node = TextNode("This is a text node", "italic", "some_url")
        node2 = TextNode("This is a text node", "bold", "some_url")
        self.assertNotEqual(node, node2)  

    def test_difText(self):
        node = TextNode("This is a text node", "italic", "some_url")
        node2 = TextNode("This is a different text node", "italic", "some_url")
        self.assertNotEqual(node, node2)          

    def test_difURL(self):
        node = TextNode("This is a text node", "italic", "some_url")
        node2 = TextNode("This is a different text node", "bold", "another_url")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()