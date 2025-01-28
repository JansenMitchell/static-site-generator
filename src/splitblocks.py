def markdown_to_blocks(markdown):
    blocks = []
    blocks_split = markdown.split("\n\n")
    for block in blocks_split:
        block_stripped = block.strip()
        if block_stripped:
            blocks.append(block_stripped)
    return blocks