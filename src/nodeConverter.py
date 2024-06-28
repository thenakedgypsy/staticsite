from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode

class TextToNodeConverter:
    def text_node_to_html_node(self, textNode):
        if isinstance(textNode, TextNode):
            nodeType = textNode.textType
            value = textNode.text
            if nodeType == "text":
                return LeafNode(None,value)
            if nodeType == "bold":
                return LeafNode("b",value)
            if nodeType == "italic":
                return LeafNode("i",value)
            if nodeType == "code":
                return LeafNode("code",value)
            if nodeType == "link":
                return LeafNode("a",value,{"href": f"{textNode.url}"})
            if nodeType == "image":
                return LeafNode("img","",{"src" : f"{textNode.url}", "alt": f"{textNode.alt}"})
            else:
                raise Exception("Type not recognised")
        else:
            raise AttributeError("Must be a TextNode object")

