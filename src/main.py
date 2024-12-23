from textnode import *
from htmlnode import *

def main():
    test_object = TextNode("This is a text node", TextType.NORMAL, "https://www.boot.dev")
    print(test_object)
    
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.NORMAL:
        return LeafNode(None, text_node.text, {})
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text, {})
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text, {})
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text, {})
    if text_node.text_type == TextType.LINKS:
        props = {"href": text_node.url}
        return LeafNode("a", text_node.text, props)
    if text_node.text_type == TextType.IMAGES:
        props = {
            "src": text_node.url,
            "alt": text_node.text
        }
        return LeafNode("img", "", props)
    else:
        raise Exception("Not a valid type.")
    
main()