import unittest
from markdownConverter import MarkdownConverter
from htmlnode import LeafNode, ParentNode


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
        assert converter.getBlockType(block) == ('heading', 6)

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
        block = "1. List Item One\n2. list item two \n3. list item three"
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
        block = "```This is not some code"
        assert converter.getBlockType(block) == "paragraph"

    def test_getBlockTypeQuote(self):
        converter = MarkdownConverter()
        block = ">This is a quote \n>That goes on for some lines\n>who even talks that long"
        assert converter.getBlockType(block) == "quote"

    def test_getBlockTypeQuoteBade(self):
        converter = MarkdownConverter()
        block = ">This is a quote \nOoops! That goes on for some lines\n>who even talks that long"
        assert converter.getBlockType(block) == "paragraph"     

    def test_headingToNode(self):   
        converter = MarkdownConverter()
        block = "# This should have a heading value of 1"
        node = converter.headingToNode(block)
        expectedNode = LeafNode("h1","This should have a heading value of 1")
        assert node == expectedNode

    def test_headingToNodeTwo(self):   
        converter = MarkdownConverter()
        block = "## This should have a heading value of 2"
        node = converter.headingToNode(block)
        expectedNode = LeafNode("h2","This should have a heading value of 2")
        assert node == expectedNode

    def test_codeToNode(self):
        converter = MarkdownConverter()
        block = "```This is some code```"
        node = converter.codeToNode(block)       
        expectedNode = ParentNode("pre", [LeafNode("code", "This is some code")])
        assert node == expectedNode

    def test_uListToNode(self):
        converter = MarkdownConverter()
        block = "* List Item One\n* List item two \n* List item three"
        expectedNode = ParentNode("ul",[LeafNode("li","List Item One"),LeafNode("li","List item two"), LeafNode("li","List item three")])
        node = converter.uListToNode(block)
        assert node ==  expectedNode

    def test_oListToNode(self):
        converter = MarkdownConverter()
        block = "1. one\n2. two \n3. three\n4. four\n5. five\n6. six\n7. seven\n8. eight\n9. nine\n10. ten!"
        expectedNode = ParentNode("ol", [LeafNode("li", "one"), 
                                         LeafNode("li", "two"), 
                                         LeafNode("li", "three"), 
                                         LeafNode("li", "four"), 
                                         LeafNode("li", "five"), 
                                         LeafNode("li", "six"), 
                                         LeafNode("li", "seven"), 
                                         LeafNode("li", "eight"), 
                                         LeafNode("li", "nine"), 
                                         LeafNode("li", "ten!")])
        node = converter.oListToNode(block)
        assert node == expectedNode
    
    def test_quoteToNode(self):
        converter = MarkdownConverter()
        block = ">This is a quote \n>That goes on for some lines\n>who even talks that long"
        expectedNode = ParentNode("blockquote",[LeafNode("p","This is a quote"),
                                                LeafNode("p","That goes on for some lines"),
                                                LeafNode("p","who even talks that long")])
        node = converter.quoteToNode(block)
        assert node == expectedNode  


if __name__ == "__main__":
    unittest.main()