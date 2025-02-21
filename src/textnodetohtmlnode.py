from textnode import *
from htmlnode import *
    
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.NORMAL:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text, {})
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text, {})
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text, {})
    if text_node.text_type == TextType.LINKS:
        return LeafNode(
            "a",
            text_node.text,
            {"href": text_node.url}  # Make sure props are being set!
        )
    if text_node.text_type == TextType.IMAGES:
        props = {
            "src": text_node.url,
            "alt": text_node.text
        }
        return LeafNode("img", "", props)
    else:
        raise Exception("Not a valid type.")