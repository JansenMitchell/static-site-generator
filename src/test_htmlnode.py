import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_leaf(self):
        node = LeafNode("a", None, {"href": "https://www.google.com"})
        self.assertRaises(ValueError, node.to_html)
    
        node = LeafNode(None, "This is a paragraph of text.", None)
        self.assertEqual(node.to_html(), "This is a paragraph of text.")
        
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
        
    def test_parent(self):
        node = ParentNode(
            "p",
            [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')
        
        node = ParentNode(
            None,
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertRaises(ValueError, node.to_html)
        
        node = ParentNode("p", None)
        self.assertRaises(ValueError, node.to_html)
        
        with self.assertRaises(TypeError):
            ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )

        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                    ]
                ),
                LeafNode("i", "italic text"),
            ]
        )
        self.assertEqual(node.to_html(), '<div><p><b>Bold text</b>Normal text</p><i>italic text</i></div>')
    
if __name__ == "__main__":
    unittest.main() 