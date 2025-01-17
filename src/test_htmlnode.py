import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_leaf_value_error(self):
        node = LeafNode("a", None, {"href": "https://www.google.com"})
        self.assertRaises(ValueError, node.to_html)
    
    def test_leaf_tag_none(self):
        node = LeafNode(None, "This is a paragraph of text.", None)
        self.assertEqual(node.to_html(), "This is a paragraph of text.")
        
    def test_leaf_props_not_none(self):
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
        
    def test_parent_tag_value_error(self):
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
        
    def test_parent_children_value_error(self):
        node = ParentNode("p", None)
        self.assertRaises(ValueError, node.to_html)
        
    def test_parent_multiple_children(self):
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

    def test_parent_nesting_children(self):
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