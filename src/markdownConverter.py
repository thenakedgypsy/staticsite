from htmlnode import LeafNode, ParentNode
from nodeConverter import NodeConverter

class MarkdownConverter():
     
    def markdownToBlock(self,markdown):
        blocks = markdown.split("\n\n")
        cleanBlocks = []
        for block in blocks:
            block = block.strip()
            if block:
                cleanBlocks.append(block)
        return cleanBlocks
     
    def getBlockType(self,block):
        if block.startswith("#"): #if heading
            count = 0
            for char in block:
                if char == "#":
                    count += 1
                else:
                    break
            if count <= 6:
                if block[count] != " ":
                    return "paragraph"
                else: 
                    return ("heading", count)
            return "paragraph"
        if block.startswith("```") and block.endswith("```"): #if its code
            return "code"
        if block.startswith(">"): #if its a quote
            splitBlock = block.split("\n")
            for line in splitBlock:
                if not line.startswith(">"):
                    return "paragraph"
            return "quote"
        if block.startswith("* "): #if its an unorderedlist*
            splitBlock = block.split("\n")
            for line in splitBlock:
                if not line.startswith("* "):
                    return "paragraph"
            return "unordered_list"        
        if block.startswith("- "):#if its an unorderedlist-
            splitBlock = block.split("\n")
            for line in splitBlock:
                if not line.startswith("- "):
                    return "paragraph"
            return "unordered_list"
        if block.startswith("1. "):#if its anumberedlist
            splitBlock = block.split("\n")
            i = 1
            for line in splitBlock:
                if not line.startswith(f"{i}. "):
                    return "paragraph"
                i+=1
            return "ordered_list"
        else:
            return "paragraph"   #otherwise its a paragraph  
    
    def headingToNode(self,block):
        headingLevel = self.getBlockType(block)[1]
        content = block[headingLevel+1:].strip()
        node = LeafNode(f"h{headingLevel}", content)         
        return node

    def codeToNode(self,block):
        content = block[3:-3].strip()
        innerNode = LeafNode("code",content)
        outerNode = ParentNode("pre",children=[innerNode])
        return outerNode

    def uListToNode(self,block):
        splitBlock = block.split("\n")
        cleanLines = []
        for line in splitBlock:
            cleanLines.append(LeafNode("li",line[1:].strip()))    
        node = ParentNode("ul",cleanLines)
        return node
    
    def oListToNode(self,block):
        splitBlock = block.split("\n")
        cleanLines = []
        for line in splitBlock:
            i = 0
            for char in line:
                if char != " ":
                    i+=1
                else:
                    break
            cleanLines.append(LeafNode("li",line[i:].strip()))    
        node = ParentNode("ol",cleanLines)
        return node
    
    def quoteToNode(self,block):
        splitBlock = block.split("\n")
        cleanLines = []
        for line in splitBlock:
            cleanLines.append(LeafNode("p",line[1:].strip()))
        node = ParentNode("blockquote",cleanLines)
        return node

    def paraToNode(self,block):
        if block != "":
            node = LeafNode("p", block)
        return node

    def markdownToHTML(self, markdown):
        converter = NodeConverter()
        blocks = self.markdownToBlock(markdown)
        newNodes = []
        for block in blocks:
            if type(self.getBlockType(block)) is tuple:
                newNodes.append(self.headingToNode(block))
            else:
                if self.getBlockType(block) == "paragraph":
                    newNodes.append(self.paraToNode(block))
                elif self.getBlockType(block) == "code":
                    newNodes.append(self.codeToNode(block))
                elif self.getBlockType(block) == "unordered_list":
                    newNodes.append(self.uListToNode(block))              
                elif self.getBlockType(block) == "ordered_list":
                    newNodes.append(self.oListToNode(block))
                elif self.getBlockType(block) == "quote":
                    newNodes.append(self.quoteToNode(block))
        node = ParentNode("div",newNodes)
        preHTML = node.to_html()
        textNodes = converter.text_to_textnodes(preHTML)
        htmlNodes = []
        for node in textNodes:
            htmlNodes.append(converter.text_node_to_html_node(node))
        htmlString = ""
        for node in htmlNodes:
            htmlString += node.to_html()
        return htmlString

        

        