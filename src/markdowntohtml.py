from htmlnode import *
from splitblocks import markdown_to_blocks

def markdown_to_hmtl_node(markdown):
    blocks = markdown_to_blocks(markdown)