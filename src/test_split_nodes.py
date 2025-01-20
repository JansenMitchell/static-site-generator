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
        
        # Case 2: Images adjacent to each other
        node2 = TextNode("![image1](url1)![image2](url2)", TextType.NORMAL)
        nodes2 = split_nodes_image([node2])
        assert len(nodes2) == 2
        assert nodes2[0].text == "image1"
        assert nodes2[0].url == "url1"
        assert nodes2[1].text == "image2"
        assert nodes2[1].url == "url2"

        # Case 3: Text starts and ends with images
        node3 = TextNode("![image1](url1) middle text ![image2](url2)", TextType.NORMAL)
        nodes3 = split_nodes_image([node3])
        assert len(nodes3) == 3
        assert nodes3[0].text == "image1"
        assert nodes3[0].url == "url1"
        assert nodes3[1].text == " middle text "
        assert nodes3[2].text == "image2"
        assert nodes3[2].url == "url2"
        
    def test_split_nodes_images_edge_cases(self):
        # Case 1: Text before and after a single link
        node1 = TextNode("Some text ![image1](url1) more text.", TextType.NORMAL)
        nodes1 = split_nodes_image([node1])
        assert len(nodes1) == 3
        assert nodes1[0].text == "Some text "
        assert nodes1[1].text == "image1"
        assert nodes1[1].url == "url1"
        assert nodes1[2].text == " more text."
        
    def test_split_nodes_link_edge_cases(self):
        # Case 1: Text before and after a single link
        node1 = TextNode("Some text [link1](url1) more text.", TextType.NORMAL)
        nodes1 = split_nodes_link([node1])
        assert len(nodes1) == 3
        assert nodes1[0].text == "Some text "
        assert nodes1[1].text == "link1"
        assert nodes1[1].url == "url1"
        assert nodes1[2].text == " more text."

        # Case 2: Links adjacent to each other
        node2 = TextNode("[link1](url1)[link2](url2)", TextType.NORMAL)
        nodes2 = split_nodes_link([node2])
        assert len(nodes2) == 2
        assert nodes2[0].text == "link1"
        assert nodes2[0].url == "url1"
        assert nodes2[1].text == "link2"
        assert nodes2[1].url == "url2"

        # Case 3: Text starts and ends with links
        node3 = TextNode("[link1](url1) middle text [link2](url2)", TextType.NORMAL)
        nodes3 = split_nodes_link([node3])
        assert len(nodes3) == 3
        assert nodes3[0].text == "link1"
        assert nodes3[0].url == "url1"
        assert nodes3[1].text == " middle text "
        assert nodes3[2].text == "link2"
        assert nodes3[2].url == "url2"