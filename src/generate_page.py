def extract_title(markdown):
    if markdown.startswith("# "):
        return markdown.strip("# ")
    raise Exception("not a title")