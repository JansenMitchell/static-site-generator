import unittest

from markdowntohtml import *
from htmlnode import *

class TestMardownToHtml(unittest.TestCase):
    def test_block_to_html(self):
        #Case 1: Headings
        for i in range(1, 7):  # Loop from 1 to 6 for `h1` through `h6`
            with self.subTest(level=i):  
                markdown = f"{'#' * i} Heading Level {i}"  # Build markdown for the heading
                expected_node = HTMLNode(tag="div", children=[
                    HTMLNode(tag=f"h{i}", children=[f"Heading Level {i}"])
                ])
                result_node = markdown_to_html_node(markdown)  # Call your function
                self.assertEqual(result_node, expected_node)  # Compare the output
        
        #Case 2: Paragraphs
        markdown = "This is a paragraph"
        expected_node = HTMLNode(tag="div", children=[
            HTMLNode(tag="p", children=["This is a paragraph"])
        ])
        result_node = markdown_to_html_node(markdown)
        self.assertEqual(result_node, expected_node)
        
        #Case 3: Blockquotes
        markdown = "> This is a quote"
        expected_node = HTMLNode(tag="div", children=[
            HTMLNode(tag="blockquote", children=["This is a quote"])
            ])
        result_node = markdown_to_html_node(markdown)
        self.assertEqual(result_node, expected_node)
        
        #Case 4: Unordered lists
        markdown = "- This is a list item"
        expected_node = HTMLNode(tag="div", children=[
            HTMLNode(tag="ul", children=[
                HTMLNode(tag="li", children=["This is a list item"])
            ])
        ])
        result_node = markdown_to_html_node(markdown)
        self.assertEqual(result_node, expected_node)
        
        #Case 5: Ordered lists
        markdown = "1. This is a list item"
        expected_node = HTMLNode(tag="div", children=[
            HTMLNode(tag="ol", children=[
                HTMLNode(tag="li", children=["This is a list item"])
            ])
        ])
        result_node = markdown_to_html_node(markdown)
        self.assertEqual(result_node, expected_node)
        
        #Case 6: Code
        markdown = """```
        print("Hello World")
        ```
        """
        expected_node = HTMLNode(tag="div", children=[
            HTMLNode(tag="code", children=[
                HTMLNode(tag="pre", children=['print("Hello World")'])
            ])
        ])