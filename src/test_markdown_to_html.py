import unittest

from markdowntohtml import *
from htmlnode import *

class TestMardownToHtml(unittest.TestCase):
    def test_block_to_html(self):
        #Case 1: Headings
        markdown = "# Hello World"
        expected_node = HTMLNode(tag="div", children=[
            HTMLNode(tag="h1", children=["Hello World"])
        ])
        result_node = markdown_to_hmtl_node(markdown)
        self.assertEqual(result_node, expected_node)
        
        #Case 2: Paragraphs
        markdown = "This is a paragraph"
        expected_node = HTMLNode(tag="div", children=[
            HTMLNode(tag="p", children=["This is a paragraph"])
        ])
        result_node = markdown_to_hmtl_node(markdown)
        self.assertEqual(result_node, expected_node)