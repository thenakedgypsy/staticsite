import re

class LinkExtractor():
    def extract_markdown_images(text): #Takes raw text and returns a list of tuples. Each tuple should contain the alt text and the URL of any markdown images. 
        matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
        return matches

    def extract_markdown_links(text): #extracts markdown links instead of images. It should return tuples of anchor text and URLs.
        matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
        return matches
    
    def extract_markdown_images_split(text):
        matches = re.split(r"!\[(.*?)\]\((.*?)\)", text)
        return matches 

    def extract_markdown_links_split(text): #extracts markdown links instead of images. It should return tuples of anchor text and URLs.
        matches = re.split(r"\[(.*?)\]\((.*?)\)", text)
        return matches
           