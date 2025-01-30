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