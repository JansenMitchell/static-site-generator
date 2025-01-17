import unittest

from textnode import *
from splitnodes import *

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
    def test_split_nodes_link_basic(self):
        node = TextNode("Hello [world](https://example.com)", TextType.NORMAL)
        nodes = split_nodes_link([node])
        assert len(nodes) == 2
        assert nodes[0].text == "Hello "
        assert nodes[0].text_type == TextType.NORMAL
        assert nodes[1].text == "world"
        assert nodes[1].text_type == TextType.LINKS
        assert nodes[1].url == "https://example.com"
        
    def test_split_nodes_link_multiple(self):
        node = TextNode(
            "This is [link1](url1) and [link2](url2)", 
            TextType.NORMAL
        )
        nodes = split_nodes_link([node])
        assert len(nodes) == 4
        assert nodes[0].text == "This is "
        assert nodes[1].text == "link1"
        assert nodes[1].url == "url1"
        assert nodes[2].text == " and "
        assert nodes[3].text == "link2"
        assert nodes[3].url == "url2"