from htmlnode import *
from splitblocks import markdown_to_blocks
from blocktype import *
from splitnodes import *
from textnodetohtmlnode import *

def markdown_to_hmtl_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent_node = HTMLNode(tag="div", children=[])
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
    # Convert all text nodes to HTML nodes
    return [text_node_to_html_node(node) for node in nodes]

def create_html_node_for_block(block):
    block_type = block_to_block_type(block)  # Determine the block type

    if block_type == BlockType.HEADING:
        # Extract heading level and text
        level = block.count("#", 0, block.find(" "))  # Number of '#' characters before the first space
        text = block[level + 1:].strip()  # Remove the '#' characters and extract the text
        return HTMLNode(tag=f"h{level}", children=text_to_children(text))

    elif block_type == BlockType.PARAGRAPH:
        return HTMLNode(tag="p", children=[block.strip()])

    elif block_type == BlockType.CODE:
        code_content = block[3:-3].strip()  # Remove the triple backticks
        return HTMLNode(tag="pre", children=[HTMLNode(tag="code", children=[code_content])])

    elif block_type == BlockType.QUOTE:
        quote_content = block[1:].strip()  # Remove the `>` marker
        return HTMLNode(tag="blockquote", children=[quote_content])

    elif block_type == BlockType.UNORDERED_LIST:
        list_items = [HTMLNode(tag="li", children=[item[2:].strip()]) for item in block.split("\n") if item]
        return HTMLNode(tag="ul", children=list_items)

    elif block_type == BlockType.ORDERED_LIST:
        list_items = [HTMLNode(tag="li", children=[item.split(maxsplit=1)[1].strip()]) for item in block.split("\n") if item]
        return HTMLNode(tag="ol", children=list_items)

    return None  # In case a new block type crops up unexpectedly