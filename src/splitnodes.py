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
    result = []
    
    def _split_images(text):
        images = extract_markdown_images(text)
        if not images:
            if text:
                return [TextNode(text, TextType.NORMAL)]
            return []
        
        first_image = images[0]
        
        sections = text.split(f"![{first_image[0]}]({first_image[1]})", 1)
        
        current_results = []
        if sections[0]:
            current_results.append(TextNode(sections[0], TextType.NORMAL))
        current_results.append(TextNode(first_image[0], TextType.IMAGES, first_image[1]))
        if sections[1]:
            current_results.extend(_split_images(sections[1]))
            
        return current_results
    
    for node in old_nodes:
        if node.text_type == TextType.NORMAL:
            result.extend(_split_images(node.text))
        else:
            result.append(node)
            
    return result

def split_nodes_link(old_nodes):
    result = []
    
    def _split_links(text):
        links = extract_markdown_links(text)
        if not links:
            if text:
                return [TextNode(text, TextType.NORMAL)]
            return []
        
        first_link = links[0]
        
        sections = text.split(f"[{first_link[0]}]({first_link[1]})", 1)
                
        current_results = []
        if sections[0]:
            current_results.append(TextNode(sections[0], TextType.NORMAL))
        current_results.append(TextNode(first_link[0], TextType.LINKS, first_link[1]))
        if sections[1]:
            current_results.extend(_split_links(sections[1]))
        
        return current_results
            
    for node in old_nodes:
        if node.text_type == TextType.NORMAL:
            result.extend(_split_links(node.text))
        else:
            result.append(node)
            
    return result