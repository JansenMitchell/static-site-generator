from markdowntohtml import markdown_to_html_node
from htmlnode import *

def extract_title(markdown):
    if markdown.startswith("# "):
        return markdown.strip("# ")
    raise Exception("not a title")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = from_path.read()
    template_file = template_path.read()
    
    markdown_to_html_node(HTMLNode.to_html(from_file))