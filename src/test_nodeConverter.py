import unittest
from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from nodeConverter import TextToNodeConverter

class TestNodeConverter(unittest.TestCase):

    def test_basicToLeaf(self):
        textNode = TextNode("This is some text","bold")
        converter = TextToNodeConverter()
        leafNode = converter.text_node_to_html_node(textNode)
        assert leafNode.to_html() == "<b>This is some text</b>"

    def test_imgToLeaf(self):
        textNode = TextNode("This should not matter","image","image.jpg","alt text")
        converter = TextToNodeConverter()
        leafNode = converter.text_node_to_html_node(textNode)
        assert leafNode.to_html() == '<img> src="image.jpg" alt="alt text"></img>'
    
    def test_linkToLeaf(self):
        textNode = TextNode("Some text","link","www.google.com",)
        converter = TextToNodeConverter()
        leafNode = converter.text_node_to_html_node(textNode)
        assert leafNode.to_html() == '<a> href="www.google.com">Some text</a>'

    def test_italicWithAlt(self):
        textNode = TextNode("This has alt text","italic", None,"alt text")
        converter = TextToNodeConverter()
        leafNode = converter.text_node_to_html_node(textNode)
        assert leafNode.to_html() == "<i>This has alt text</i>"

if __name__ == "__main__":
    unittest.main()