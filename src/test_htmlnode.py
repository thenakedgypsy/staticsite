import unittest
from htmlnode import HTMLNode, LeafNode

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
        testDict = {"href": "https://www.google.com", "target" : "_blank"}
        node = HTMLNode("p", "contents here", testList, testDict)
        #actualRepr = repr(node)
        assert repr(node) == "HTMLNode(p, contents here, ['one', 'two', 'three'], {'href': 'https://www.google.com', 'target': '_blank'})"
       

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
        print(node.to_html())
        assert node.to_html() == f"Value"


    

if __name__ == "__main__":
    unittest.main()