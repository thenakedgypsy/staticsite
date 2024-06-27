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