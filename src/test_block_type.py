import unittest

from blocktype import *

class TestBlockType(unittest.TestCase):
    def test_block_to_block_type(self):
        # Case 1: Headings
        block = "##### This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        
        # Case 2: Code blocks
        block = """```
        print("Hello World!")
        ```"""
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        
        # Case 3: Quote blocks
        block = ">This is a quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        
        # Case 4: Unordered list
        block = "- This is an item"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        
        # Case 5: Ordered list
        block = "1. This is the first item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        
        # Case 6: Paragraph
        block = "This is a paragraph."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)