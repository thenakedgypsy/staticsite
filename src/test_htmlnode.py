import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_propsToHTML(self):
        testList = ["one","two","three"]
        testDict = {"href": "https://www.google.com", "target" : "_blank"}
        node = HTMLNode("tagname", "contents here", testList, testDict)
        if node.props_to_html() == 'href="https://www.google.com" target="_blank"':
            return True

    
        




if __name__ == "__main__":
    unittest.main()