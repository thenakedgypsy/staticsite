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
                    return "heading"
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
            return "paragraph"     