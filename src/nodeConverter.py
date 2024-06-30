from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode
from linkExtractor import LinkExtractor

class NodeConverter: # converter class - converts nodes
    
    def text_node_to_html_node(self, textNode):  #returns a single htmlnode -> converts textNodes to htmlnodes
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

    def split_nodes_delimiter(self, oldNodes, delimiter, textType):# returns a list of textnodes -> splits textnodes into other textnodes based on delimiter 
        newNodes = []
        for node in oldNodes:                             #for each node check for the delim and split
            if delimiter == "" or delimiter == None:
                newNodes.append(TextNode(node.text),"text")
            elif node.textType == "bold" or node.textType == "italic" or node.textType == "code": #if its not just text then check if this node has already been passed over
                newNodes.append(node)            
            else:                                          #otherwise split at delim and add type
                splitNode = node.text.split(delimiter)
                i = 1
                for part in splitNode:
                    if i % 2 == 0:
                        newNodes.append(TextNode(part, textType))
                    else:
                        newNodes.append(TextNode(part, "text"))
                    i += 1
        return newNodes
        
    def split_nodes_links(old_nodes):
        linkExtractor = LinkExtractor
        newNodes = []
        for node in old_nodes:
            splitNode = linkExtractor.extract_markdown_links_split(node.text)
            i = 0
            partCount = len(splitNode)                            
            while i < partCount:                
                if splitNode[i]:
                    if splitNode[i] != "":
                        newNodes.append(TextNode(splitNode[i],"text"))
                if i + 2 < partCount:
                    newNodes.append(TextNode(splitNode[i+1],"link", splitNode[i+2]))
                    i +=3
                else:
                    i +=1                
            return newNodes
                    
    def split_nodes_images(old_nodes):
        pass