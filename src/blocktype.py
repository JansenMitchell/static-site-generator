from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "qoute"
    UNORDERED_LIST = "unordred_list"
    ORDERED_LIST = "ordered_list"
    
def block_to_block_type(block):
    #TODO: Cover edge cases
    # Heading depth to 6
    # Multiple spaces before and after
    if block[0] == "#":
        return BlockType.HEADING