class HTMLNode(): #represents a node that will convert to html
    def __init__(self,tag,value,children,props):
        self.tag = tag
        self.value = value
        if children == None:
            self.children = list()
        else:
            self.children = children
        if props == None:
            self.props = dict()
        else:
            self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self): #converts properties dict to html
        propString = ""
        for key in self.props:
            propString += f' {key}="{self.props[key]}"'
        return propString

    def __repr__(self):
        toPrint =  f"HTMLNode({self.tag}, {self.value}" 
        if self.children != None:
            toPrint += f", {self.children}"
        if self.props !=None:
            toPrint += f", {self.props}"
        toPrint += ")"
        return toPrint
    
    def __eq__(self,other):
        if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
            return True
        else:
            return False
    
class LeafNode(HTMLNode): #node without any children
    def __init__(self,tag,value,props=None):
        super().__init__(tag,value,None,props)
        if self.value == None:
            raise ValueError("A LeafNode requires a value")


    def to_html(self): #converts itself to html
        htmlProps = self.props_to_html()
        if self.tag == None:
            return self.value
        if htmlProps == "":
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            if self.tag == "a":
                return f"<{self.tag}{htmlProps}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}{htmlProps}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode): #node that will have either more parentnodes or leafnodes as children
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)
        if self.tag == None:
            raise ValueError("A ParentNode requires a tag")
        if len(self.children) == 0:
            raise ValueError("A ParentNode requires children")

    def to_html(self):
        if self.props == None:
            htmlString = f"<{self.tag}>"
        else:
            htmlString = f"<{self.tag}>{self.props_to_html()}"
        for child in self.children:
            htmlString += child.to_html()
        htmlString += f"</{self.tag}>"  
        return htmlString             
