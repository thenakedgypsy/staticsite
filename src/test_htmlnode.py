import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_simplePropsToHTML(self):
        testList = ["one","two","three"]
        testDict = {"href": "https://www.google.com", "target" : "_blank"}
        node = HTMLNode("tagname", "contents here", testList, testDict)
        if node.props_to_html() == 'href="https://www.google.com" target="_blank"':
            return True

    def test_PropsToHTML(self):
        testList = ["one","two","three"]
        testDict = {"href": "https://www.google.com", "target" : "_blank", "someThirdThing": "sadness"}
        node = HTMLNode("tagname", "contents here", testList, testDict)
        if node.props_to_html() == 'href="https://www.google.com" target="_blank" someThirdThing="sadness"':
            return True

    def test_prints(self):
        testList = ["one","two","three"]
        testDict = {"href": "https://www.google.com", "target" : "_blank"}
        node = HTMLNode("tagname", "contents here", testList, testDict)
        if node.__repr__ == "HTMLNode(tagname, contents here, ['one', 'two', 'three'], {'href': 'https://www.google.com', 'target': '_blank'})":
            return True
            
        




if __name__ == "__main__":
    unittest.main()