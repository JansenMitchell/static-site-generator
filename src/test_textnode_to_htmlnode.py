import unittest

from textnodetohtmlnode import *
from textnode import *
from htmlnode import *

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_type_links(self):
        text_node = TextNode("Links", TextType.LINKS)
        props = {"href": text_node.url}
        self.assertEqual(text_node_to_html_node(text_node), LeafNode("a", text_node.text, props))
        
    def test_text_type_images(self):
        text_node = TextNode("Images", TextType.IMAGES)
        props = {
            "src": text_node.url,
            "alt": text_node.text
        }
        self.assertEqual(text_node_to_html_node(text_node), LeafNode("img", "", props))
        
    def test_text_type_error(self):
        with self.assertRaises(Exception):
            TextNode("Random text", TextType.RANDOM)