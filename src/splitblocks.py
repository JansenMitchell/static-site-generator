import re

def markdown_to_blocks(markdown):
    # TODO: Strip leading and trailing whitespace.
    blocks = markdown.split("\n\n")
    return blocks