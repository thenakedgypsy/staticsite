import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_simplePropsToHTML(self):
        testList = ["one","two","three"]
        testDict = {"href": "https://www.google.com", "target" : "_blank"}
        node = HTMLNode("tagname", "contents here", testList, testDict)
        assert node.props_to_html() == f' href="https://www.google.com" target="_blank"'
        

    def test_PropsToHTML(self):
        testList = ["one","two","three"]
        testDict = {"href": "https://www.google.com", "target" : "_blank", "someThirdThing": "sadness"}
        node = HTMLNode("tagname", "contents here", testList, testDict)
        assert node.props_to_html() == ' href="https://www.google.com" target="_blank" someThirdThing="sadness"'
        

    def test_prints(self):
        testList = ["one","two","three"]
        testDict = {"href": "https://www.google.com", "target" : "_blank"}
        node = HTMLNode("tagname", "contents here", testList, testDict)
        actualRepr = repr(node)
        assert actualRepr == "HTMLNode(tagname, contents here, ['one', 'two', 'three'], {'href': 'https://www.google.com', 'target': '_blank'})"
       
  

if __name__ == "__main__":
    unittest.main()