from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "qoute"
    UNORDERED_LIST = "unordred_list"
    ORDERED_LIST = "ordered_list"
    
def block_to_block_type(block):
    if block[0] == "#":
        return BlockType.HEADING
    if block[0:3] == "```":
        return BlockType.CODE