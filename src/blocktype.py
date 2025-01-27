from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "qoute"
    UNORDERED_LIST = "unordred_list"
    ORDERED_LIST = "ordered_list"