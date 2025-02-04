import unittest

from markdowntohtml import *
from htmlnode import *

class TestMardownToHtml(unittest.TestCase):
    def test_block_to_html(self):
        markdown = "# Hello World"
        expected_node = HTMLNode(tag="div", children=[
            HTMLNode(tag="h1", children=["Hello World"])
        ])
        result_node = markdown_to_hmtl_node(markdown)
        self.assertEqual(result_node, expected_node)