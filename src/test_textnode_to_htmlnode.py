import unittest

from main import text_node_to_html_node
from textnode import *
from htmlnode import *

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_type_normal(self):
        text_node = TextNode("Normal text", TextType.NORMAL)
        self.assertEqual(text_node_to_html_node(text_node), LeafNode(None, text_node.text, {}))