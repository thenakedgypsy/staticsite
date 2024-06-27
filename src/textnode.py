class TextNode():

    def __init__(self, content, type, url):
        self.text = content
        self.textType = type
        self.url = url
    
    def __eq__(self, other):
        if self.text == other.text and self.textType == other.textType and self.url == other.url:
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text},{self.textType},{self.url})"