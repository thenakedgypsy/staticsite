class HTMLNode():
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
        
    this = {"href": "https://www.google.com", "target": "_blank"}

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        propString = ""
        for key in self.props:
            propString += f' {key}="{self.props[key]}"'
        return propString

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self,tag,value,props):
        super().__init__(tag,value,None,props)
        if self.value == None:
            raise ValueError("A leaf node requires a value")


    def to_html(self):
        htmlProps = self.props_to_html()

        if self.tag == None:
            return self.value
        if htmlProps == "":
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{htmlProps}>{self.value}</{self.tag}>"
        
