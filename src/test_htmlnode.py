import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):

    def test_simplePropsToHTML(self):
        testList = ["one","two","three"]
        testDict = {"href": "https://www.google.com", "target" : "_blank"}
        node = HTMLNode("p", "contents here", testList, testDict)
        assert node.props_to_html() == f' href="https://www.google.com" target="_blank"'

    def test_PropsToHTML(self):
        testList = ["one","two","three"]
        testDict = {"href": "https://www.google.com", "target" : "_blank", "someThirdThing": "sadness"}
        node = HTMLNode("p", "contents here", testList, testDict)
        assert node.props_to_html() == ' href="https://www.google.com" target="_blank" someThirdThing="sadness"'     

    def test_prints(self):
        testList = ["one","two","three"]
        testDict = {"class": "text", "target" : "_blank"}
        node = HTMLNode("p", "contents here", testList, testDict)
        assert repr(node) == "HTMLNode(p, contents here, ['one', 'two', 'three'], {'class': 'text', 'target': '_blank'})"
       

class TestLeafNode(unittest.TestCase):

    def test_simpleToHTML(self):
        testDict = {"class": "text", "target" : "_blank"}
        node = LeafNode("p", "Text and props here", testDict)
        assert node.to_html() == f'<p> class="text" target="_blank">Text and props here</p>'

    def test_ToHTMLNoProps(self):
        node = LeafNode("a", "Just Text Here", None)
        assert node.to_html() == f"<a>Just Text Here</a>"
        
    def test_noTag(self):
        node = LeafNode(None,"Value",None)
        assert node.to_html() == f"Value"

class TestParentNode(unittest.TestCase):

    def test_ToHTML(self):
        testDict = {"class": "text", "target" : "_blank"}
        node = ParentNode("p",[
        LeafNode("b", "Bold text"),
        LeafNode("a", "Normal text", testDict),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text",),],)
        assert node.to_html() == f'<p><b>Bold text</b><a> class="text" target="_blank">Normal text</a><i>italic text</i>Normal text</p>'

    def test_nestedParent(self):
        node = ParentNode("p",[
        LeafNode("b", "Bold text"),
        ParentNode("a",[
            LeafNode("b", "Nested Bold"),
            LeafNode("i", "Nested Italic"),
        ],),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text",),],)
        assert node.to_html() == f'<p><b>Bold text</b><a><b>Nested Bold</b><i>Nested Italic</i></a><i>italic text</i>Normal text</p>'

    def test_nestedParentWithProps(self):
        testDict = {"class": "text", "target" : "_blank"}
        node = ParentNode("p",[
        LeafNode("b", "Bold text"),
        ParentNode("a",[
            LeafNode("b", "Nested Bold"),
            LeafNode("i", "Nested Italic"),
        ], testDict),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text",),],testDict)
        assert node.to_html() == f'<p> class="text" target="_blank"<b>Bold text</b><a> class="text" target="_blank"<b>Nested Bold</b><i>Nested Italic</i></a><i>italic text</i>Normal text</p>'

    def test_noChildrenRaisesValueError(self):
        with self.assertRaises(ValueError):
            node = ParentNode("p",None,)

    def test_noTagRaisesValueError(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None,None,)


if __name__ == "__main__":
    unittest.main()