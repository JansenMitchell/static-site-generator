import unittest

from textnode import *
from splitnodesdelimiter import split_nodes_delimiter

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is a text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes,
                        [
                            TextNode("This is a text with a ", TextType.NORMAL),
                            TextNode("code block", TextType.CODE),
                            TextNode(" word", TextType.NORMAL),
                        ])
    def test_bold(self):
        node = TextNode("This is a text with a **bold** word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes,
                        [
                            TextNode("This is a text with a ", TextType.NORMAL),
                            TextNode("bold", TextType.BOLD),
                            TextNode(" word", TextType.NORMAL),
                        ])
        
    def test_italics(self):
        node = TextNode("This is a text with a *italic* word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(new_nodes,
                        [
                            TextNode("This is a text with a ", TextType.NORMAL),
                            TextNode("italic", TextType.ITALIC),
                            TextNode(" word", TextType.NORMAL),
                        ])