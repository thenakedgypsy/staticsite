import unittest
from linkExtractor import LinkExtractor

class TestLinkExtractor(unittest.TestCase):
    def test_extractImages(self):
        imageExtractor = LinkExtractor
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        expectedList = [('image', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png'), ('another', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png')]
        assert imageExtractor.extract_markdown_images(text) == expectedList

    def test_extractLinks(self):
        linkExtractor = LinkExtractor
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        expectedList = [('link', 'https://www.example.com'), ('another', 'https://www.example.com/another')]
        assert linkExtractor.extract_markdown_links(text) == expectedList

    def test_extractLinksThree(self):
        linkExtractor = LinkExtractor
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another) and [oneMore](https://site.com)"
        expectedList = [('link', 'https://www.example.com'), ('another', 'https://www.example.com/another'),('oneMore','https://site.com')]
        assert linkExtractor.extract_markdown_links(text) == expectedList



if __name__ == "__main__":
    unittest.main()