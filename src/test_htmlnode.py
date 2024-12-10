import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_none(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)
        
    def test_not_none(self):
        node = HTMLNode("tag", "value", "children", "props")
        self.assertIsNotNone(node.tag)
        self.assertIsNotNone(node.value)
        self.assertIsNotNone(node.children)
        self.assertIsNotNone(node.props)
        
    def test_props_equal(self):
        node = HTMLNode(None, None, None, 
                        {
                            "href": "https://www.google.com", 
                            "target": "_blank",
                        })
        node2 = HTMLNode(None, None, None, 
                        {
                            "href": "https://www.google.com", 
                            "target": "_blank",
                        })
        self.assertDictEqual(node.props, node2.props)
    
if __name__ == "__main__":
    unittest.main() 