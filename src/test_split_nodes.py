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
    def test_image(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes,
                        [
                            TextNode("This is text with a link ", TextType.NORMAL),
                            TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"),
                            TextNode(" and ", TextType.NORMAL),
                            TextNode(
                                "to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev"
                            ),
                        ])