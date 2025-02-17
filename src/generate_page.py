from markdowntohtml import markdown_to_html_node
from htmlnode import *

def extract_title(markdown):
    markdown_split = markdown.split('\n')
    for line in markdown_split:
        line = line.strip()
        if line.startswith("# "):
            return line.strip("# ")
    raise Exception("not a title")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, "r") as file:
        from_file = file.read()
    
    with open(template_path, "r") as file:
        template_file = file.read()
    
    title = extract_title(from_file)
    html_node = markdown_to_html_node(from_file)  # First convert markdown to node
    html_string = html_node.to_html()  # Then convert node to HTML string