import unittest

from main import text_node_to_html_node
from textnode import *
from htmlnode import *

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_type_normal(self):
        text_node = TextNode("Normal text", TextType.NORMAL)
        self.assertEqual(text_node_to_html_node(text_node), LeafNode(None, text_node.text, {}))
        
    def test_text_type_bold(self):
        text_node = TextNode("Bold text", TextType.BOLD)
        self.assertEqual(text_node_to_html_node(text_node), LeafNode("b", text_node.text, {}))
        
    def test_text_type_italic(self):
        text_node = TextNode("Italic text", TextType.ITALIC)
        self.assertEqual(text_node_to_html_node(text_node), LeafNode("i", text_node.text, {}))
        
    #TODO: Figure out why tests past 20 are not being picked up.