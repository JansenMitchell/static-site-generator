import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node.url)
        
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertIsNotNone(node.url)
        
if __name__ == "__main__":
    unittest.main() 