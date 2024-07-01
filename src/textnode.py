class TextNode():

    def __init__(self, content, type=None, url=None, alt=None):
        self.text = content
        self.textType = type
        self.url = url
        self.alt = alt
    
    def __eq__(self, other):
        if self.text == other.text and self.textType == other.textType and self.url == other.url and self.alt == other.alt:
            return True
        else:
            return False

    def __repr__(self):
        returnString = f"TextNode('{self.text}'"
        if self.textType != None or self.textType != "":
            returnString += f", '{self.textType}'"
        if self.url != None:
            returnString += f", '{self.url}'"
        if self.alt != None:
            returnString += f", '{self.alt}'"
        returnString += f")"
        return returnString
        #return f"TextNode({self.text},{self.textType},{self.url},{self.alt})"