import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node.url)
        
    def test_not_none(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertIsNotNone(node.url)
        
if __name__ == "__main__":
    unittest.main() 