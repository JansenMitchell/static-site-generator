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
        if node.text_type == TextType.NORMAL:
            segments = extract_markdown_links(node.text)
            for link in segments:
                sections = node.text.split(f"[{link[0]}]({link[1]})", 1)
                if sections[0]:
                    segment_list.append(TextNode(sections[0], TextType.NORMAL))
                segment_list.append(TextNode(link[0], TextType.LINKS, link[1]))
                if sections[1]:
                    segment_list.append(TextNode(sections[1], TextType.NORMAL))
        else:
            segment_list.append(node)
    return segment_list
                