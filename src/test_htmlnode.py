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
        
    #TODO: test if to_html raises ValueError
    #def test_to_html_value_error(self):
        #node = LeafNode()
    def test_to_html_tag_value(self):
        node = LeafNode(None, "This is a paragraph of text.", None)
        #this only checks if the defined node value equals the asserted test
        #TODO: check if value returns when tag is none with to_html method
        self.assertIs(node.value, "This is a paragraph of text.")
        
    #TODO: test if self.props outputs correctly when not None
    
if __name__ == "__main__":
    unittest.main() 