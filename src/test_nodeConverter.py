import unittest
from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from nodeConverter import NodeConverter

class TestNodeConverter(unittest.TestCase):

    def test_basicToLeaf(self):
        textNode = TextNode("This is some text","bold")
        converter = NodeConverter()
        leafNode = converter.text_node_to_html_node(textNode)
        assert leafNode.to_html() == "<b>This is some text</b>"

    def test_imgToLeaf(self):
        textNode = TextNode("This should not matter","image","image.jpg","alt text")
        converter = NodeConverter()
        leafNode = converter.text_node_to_html_node(textNode)
        assert leafNode.to_html() == '<img> src="image.jpg" alt="alt text"></img>'
    
    def test_linkToLeaf(self):
        textNode = TextNode("Some text","link","www.google.com",)
        converter = NodeConverter()
        leafNode = converter.text_node_to_html_node(textNode)
        assert leafNode.to_html() == '<a href="www.google.com">Some text</a>'

    def test_italicWithAlt(self):
        textNode = TextNode("This has alt text","italic", None,"alt text")
        converter = NodeConverter()
        leafNode = converter.text_node_to_html_node(textNode)
        assert leafNode.to_html() == "<i>This has alt text</i>"

    def test_splitDelimSingle(self):
        textNode1 = TextNode("Words words *italic words* words words")
        oldNodes = [textNode1]
        converter = NodeConverter() 
        newNodes = converter.split_nodes_delimiter(oldNodes, "*","italic")
        expectedNodes = [
            TextNode("Words words ", "text"),
            TextNode("italic words", "italic"),
            TextNode(" words words", "text")]
        assert newNodes == expectedNodes

    def test_splitDelimTwoSameDelim(self):
        textNode1 = TextNode("Words words *italic words* words words")
        textNode2 = TextNode("Another node with *some italic words* inside of it")
        oldNodes = [textNode1,textNode2]
        converter = NodeConverter() 
        newNodes = converter.split_nodes_delimiter(oldNodes, "*", "italic")
        expectedNodes = [
            TextNode("Words words ", "text"),
            TextNode("italic words", "italic"),
            TextNode(" words words", "text"),            
            TextNode("Another node with ", "text"),
            TextNode("some italic words", "italic"),
            TextNode(" inside of it", "text")]
        assert newNodes == expectedNodes

    def test_splitDelimTwoDiffDelim(self):
        textNode1 = TextNode("Words words **bold words** words words")
        textNode2 = TextNode("Another node with *some italic words* inside of it")
        oldNodes = [textNode1,textNode2]
        converter = NodeConverter() 
        newNodes = converter.split_nodes_delimiter(oldNodes,"**", "bold")
        expectedNodes = [
            TextNode("Words words ", "text"),
            TextNode("bold words", "bold"),
            TextNode(" words words", "text"),            
            TextNode("Another node with *some italic words* inside of it", "text"),]
        assert newNodes == expectedNodes

    def test_splitDelimTwoDiffDelimDoubleParse(self):
        textNode1 = TextNode("Words words **bold words** words words")
        textNode2 = TextNode("Another node with *some italic words* inside of it")
        oldNodes = [textNode1,textNode2]
        converter = NodeConverter() 
        firstNewNodes = converter.split_nodes_delimiter(oldNodes,"**", "bold")
        secondNewNodes = converter.split_nodes_delimiter(firstNewNodes, "*", "italic")
        expectedNodes = [
            TextNode("Words words ", "text"),
            TextNode("bold words", "bold"),
            TextNode(" words words", "text"),            
            TextNode("Another node with ", "text"),
            TextNode("some italic words", "italic"),
            TextNode(" inside of it", "text"),]
        assert secondNewNodes == expectedNodes
        
    def test_splitDelimDoubleParseSingle(self):
        textNode1 = TextNode("Words words **bold words** words words but also some *italic words* yay!")
        oldNodes = [textNode1]
        converter = NodeConverter() 
        firstNewNodes = converter.split_nodes_delimiter(oldNodes,"**", "bold")
        secondNewNodes = converter.split_nodes_delimiter(firstNewNodes, "*", "italic")
        expectedNodes = [
            TextNode("Words words ", "text"),
            TextNode("bold words", "bold"),
            TextNode(" words words but also some ", "text"),            
            TextNode("italic words", "italic"),
            TextNode(" yay!", "text")]
        assert secondNewNodes == expectedNodes  

    def test_splitLink(self):
        nodeList = [TextNode("This is text with a [link](https://www.example.com) and [another](https://www.example.com/another) and [oneMore](https://site.com)", "text")]
        converter = NodeConverter()
        newNodes = converter.split_nodes_links(nodeList)
        expectedNodes = [
            TextNode("This is text with a " , "text"), 
            TextNode("link", "link", "https://www.example.com"), 
            TextNode(" and " , "text"),
            TextNode("another", "link", "https://www.example.com/another"),
            TextNode(" and ", "text"), 
            TextNode("oneMore", "link", "https://site.com")]
        assert newNodes == expectedNodes

    def test_splitLinkStart(self):
        nodeList = [TextNode("[link](https://www.example.com) and [another](https://www.example.com/another) and [oneMore](https://site.com)", "text")]
        converter = NodeConverter()
        newNodes = converter.split_nodes_links(nodeList)
        expectedNodes = [ 
            TextNode("link", "link", "https://www.example.com"), 
            TextNode(" and " , "text"),
            TextNode("another", "link", "https://www.example.com/another"),
            TextNode(" and ", "text"), 
            TextNode("oneMore", "link", "https://site.com")]
        assert newNodes == expectedNodes

    def test_splitLinkEndText(self):
        nodeList = [TextNode("[link](https://www.example.com) and [another](https://www.example.com/another) and [oneMore](https://site.com) and then more text", "text")]
        converter = NodeConverter()
        newNodes = converter.split_nodes_links(nodeList)
        expectedNodes = [ 
            TextNode("link", "link", "https://www.example.com"), 
            TextNode(" and " , "text"),
            TextNode("another", "link", "https://www.example.com/another"),
            TextNode(" and ", "text"), 
            TextNode("oneMore", "link", "https://site.com"),
            TextNode(" and then more text", "text")]
        assert newNodes == expectedNodes

    def test_splitImage(self):
        nodeList = [TextNode("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)", "text")]
        converter = NodeConverter()
        newNodes = converter.split_nodes_images(nodeList)
        expectedNodes = [TextNode("This is text with an ","text"),
                        TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png", "image"),
                        TextNode(" and another ", "text"),
                        TextNode("second image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png", "second image")]
        assert newNodes == expectedNodes


#test images in links and vice versa 
   
    def test_textToNode(self):
        converter = NodeConverter()
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        newNodes = converter.text_to_textnodes(text)
        expectedNodes = [TextNode('This is ', 'text'),
                        TextNode('text', 'bold'),
                        TextNode(' with an ', 'text'),
                        TextNode('italic', 'italic'),
                        TextNode(' word and a ', 'text'),
                        TextNode('code block', 'code'),
                        TextNode(' and an ', 'text'),
                        TextNode('image', 'image', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png', 'image'),
                        TextNode(' and a ', 'text'),
                        TextNode('link', 'link', 'https://boot.dev')]
        assert newNodes == expectedNodes


if __name__ == "__main__":
    unittest.main()