import unittest
from markdownConverter import MarkdownConverter


class TestMarkdownConverter(unittest.TestCase):

    def test_markdownToBlocks(self):
        converter = MarkdownConverter()
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is a list item
* This is another list item"""

        expectedBlocks = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is a list item\n* This is another list item']
        assert converter.markdownToBlock(markdown) == expectedBlocks

    def test_getBlockTypePara(self):
        converter = MarkdownConverter()
        block = "This is just some text"
        assert converter.getBlockType(block) == "paragraph"

    def test_getBlockTypeHeading(self):
        converter = MarkdownConverter()
        block = "###### This is a heading"
        assert converter.getBlockType(block) == "heading"

    def test_getBlockTypeHeadingManyHash(self):
        converter = MarkdownConverter()
        block = "######## This is a heading"
        assert converter.getBlockType(block) == "paragraph"

    def test_getBlockTypeHeadingNoSpace(self):
        converter = MarkdownConverter()
        block = "##This is a heading"
        assert converter.getBlockType(block) == "paragraph"

    def test_getBlockTypeList(self):
        converter = MarkdownConverter()
        block = "* List Item One\n* List item 2 \n* List item four"
        assert converter.getBlockType(block) == "unordered_list"

    def test_getBlockTypeNumbered(self):
        converter = MarkdownConverter()
        block = "1. List Item One\n2. List item 2 \n3. List item four"
        assert converter.getBlockType(block) == "ordered_list"

    def test_getBlockTypeNumberedBad(self):
        converter = MarkdownConverter()
        block = "1. List Item One\n3. List item 2 \n2. List item four"
        assert converter.getBlockType(block) == "paragraph"

    def test_getBlockTypeCode(self):
        converter = MarkdownConverter()
        block = "```This is some code```"
        assert converter.getBlockType(block) == "code"

    def test_getBlockTypeCodeNoClosing(self):
        converter = MarkdownConverter()
        block = "```This is some code"
        assert converter.getBlockType(block) == "paragraph"

    def test_getBlockTypeQuote(self):
        converter = MarkdownConverter()
        block = ">This is a quote \n>That goes on for some lines\n>who even talks that long"
        assert converter.getBlockType(block) == "quote"

    def test_getBlockTypeQuoteBade(self):
        converter = MarkdownConverter()
        block = ">This is a quote \nOoops! That goes on for some lines\n>who even talks that long"
        assert converter.getBlockType(block) == "paragraph"        




if __name__ == "__main__":
    unittest.main()