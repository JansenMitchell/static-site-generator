from htmlnode import *
from splitblocks import markdown_to_blocks
from blocktype import *
from splitnodes import *
from textnodetohtmlnode import *

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent_node = ParentNode(tag="div", children=[])
    for block in blocks:
        node = create_html_node_for_block(block)
        parent_node.children.append(node)
    return parent_node

def text_to_children(text):
    # Start with a single text node
    nodes = [TextNode(text, TextType.NORMAL)]
    # Split on each delimiter in sequence
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_link(nodes)
    # Convert all text nodes to HTML nodes
    return [text_node_to_html_node(node) for node in nodes]

def create_html_node_for_block(block):
    block_type = block_to_block_type(block)  # Determine the block type
    
    if block_type == BlockType.HEADING:
        # Extract heading level and text
        level = block.count("#", 0, block.find(" "))  # Number of '#' characters before the first space
        text = block[level + 1:].strip()  # Remove the '#' characters and extract the text
        return ParentNode(tag=f"h{level}", children=text_to_children(text))

    elif block_type == BlockType.PARAGRAPH:
        return ParentNode(tag="p", children=text_to_children(block.strip()))

    elif block_type == BlockType.CODE:
        code_content = block[3:-3].strip()  # Remove the triple backticks
        code_node = LeafNode(tag="code", value=code_content)
        return ParentNode(tag="pre", children=[code_node])

    elif block_type == BlockType.QUOTE:
        quote_content = block[1:].strip()  # Remove the `>` marker
        return ParentNode(tag="blockquote", children=text_to_children(quote_content))

    elif block_type == BlockType.UNORDERED_LIST:
    # Convert each list item's text to proper text nodes first
        list_items = []
        for item in block.split("\n"):
            if item:
                text = item[2:].strip()  # Remove "* " from start
                text_children = text_to_children(text)  # Convert text to proper nodes
                list_items.append(ParentNode(tag="li", children=text_children))
        return ParentNode(tag="ul", children=list_items)

    elif block_type == BlockType.ORDERED_LIST:
        # Convert each list item's text to proper text nodes
        list_items = []
        for item in block.split("\n"):
            if item:
                text = item.split(maxsplit=1)[1].strip()  # Remove "1. " from start
                text_children = text_to_children(text)  # Convert text to proper nodes
                list_items.append(ParentNode(tag="li", children=text_children))
        return ParentNode(tag="ol", children=list_items)

    return None  # In case a new block type crops up unexpectedly