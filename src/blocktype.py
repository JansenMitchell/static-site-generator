from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "qoute"
    UNORDERED_LIST = "unordred_list"
    ORDERED_LIST = "ordered_list"
    IMAGE = "image"
    
def block_to_block_type(block):
    if block[0] == "#":
        return BlockType.HEADING
    if block[0:3] == "```" and block[-3:] == "```":
        return BlockType.CODE
    if block[0] == ">":
        return BlockType.QUOTE
    if ((block[0] == "*" or block[0] == "-")
    and block[1] == " "):
        return BlockType.UNORDERED_LIST
    if "." in block:
        parts = block.split(".")
        number_part = parts[0]
        content_part = parts[1]
        if number_part.isdigit() and int(number_part) == 1:
            if content_part.startswith(" "):
                return BlockType.ORDERED_LIST
    if block[0] == "!":
        return BlockType.IMAGE
    return BlockType.PARAGRAPH