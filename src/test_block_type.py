import unittest

from blocktype import *

class TestBlockType(unittest.TestCase):
    def test_block_to_block_type(self):
        # Case 1: Headings
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)