import re

def markdown_to_blocks(markdown):
    # When the function detects a new line after a string, it splits.
    # Leading and trailing whitespace is stripped from each block.
    # "Empty" blocks are removed. 
    # Empty blocks are blocks that are empty with an empty block preceding and succeding it.
    pass