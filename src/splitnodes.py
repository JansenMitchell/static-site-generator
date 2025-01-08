from textnode import *
from extractmarkdown import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    segment_list = []
    for node in old_nodes:
        if node.text_type == TextType.NORMAL:
            segments = node.text.split(delimiter)
            if len(segments) % 2 == 0:
                raise ValueError("Unmatched delimiter found in the text.")
            for i, segment in enumerate(segments):
                if i % 2 == 0:
                    node_type = TextType.NORMAL
                else:
                    node_type = text_type
                new_node = TextNode(segment, node_type)
                segment_list.append(new_node)
        else:
            segment_list.append(old_nodes)
    return segment_list

def split_nodes_image(old_nodes):
    pass

def split_nodes_link(old_nodes):
    segment_list = []
    for node in old_nodes:
        if node.text_type == TextType.LINKS:
            segments = extract_markdown_links(node)
            #TODO: Split the text around the link
            #TODO: Create a text node for the content before the link (if any)
            #TODO: Create a link node for the link itself
            #TODO: Continue with the remaining text
            for link in segments:
                sections = node.text.split(f"[{link.text}]({link.url})", 1)
                text = sections.text
                url = sections.url
                new_node = TextNode(text, TextType.LINKS, url)
                segment_list.append(new_node)
        else:
            segment_list.append(new_node)
                