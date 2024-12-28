from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    for node in old_nodes:
        if node.text_type == TextType.NORMAL:
            segements = node.text.split(delimiter)
            for segment in segements:
                segment = TextNode(text, text_type)
                