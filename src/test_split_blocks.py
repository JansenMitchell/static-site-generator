import unittest

from splitblocks import *

class TestSplitBlocks(unittest.TestCase):
    def test_split_blocks(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        self.assertEqual(markdown_to_blocks(markdown), ["# This is a heading", 
                                                        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", 
                                                        """* This is the first list item in a list block
* This is a list item
* This is another list item"""])
    
    def test_split_block_stripped(self):
        markdown = """ # This is a heading 

 This is a paragraph of text. It has some **bold** and *italic* words inside of it. 

 * This is the first list item in a list block
* This is a list item
* This is another list item """
        self.assertEqual(markdown_to_blocks(markdown), ["# This is a heading", 
                                                        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", 
                                                        """* This is the first list item in a list block
* This is a list item
* This is another list item"""])