from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode

class NodeConverter: # converter class - converts textnodes to htmlnodes
    
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

    def split_nodes_delimiter(self, oldNodes, delimiter,textType):
        newNodes = []
        for node in oldNodes: #for each node check for the delim and split
            if delimiter == "" or delimiter == None:
                newNodes.append(TextNode(node.text),"text")
            else:
                splitNode = node.text.split(delimiter)
                i = 1
                for part in splitNode:
                    if i % 2 == 0:
                        newNodes.append(TextNode(part, textType))
                    else:
                        newNodes.append(TextNode(part, "text"))
                    i += 1
        return newNodes
