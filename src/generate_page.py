from markdowntohtml import markdown_to_html_node
from htmlnode import *
import os
from pathlib import Path

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
    
    final_html = template_file.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    
    dir_path = os.path.dirname(dest_path)
    os.makedirs(dir_path, exist_ok=True)
    
    with open(dest_path, "w") as file:
        file.write(final_html)
        
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print(f"Generating page from {dir_path_content}, to {dest_dir_path} using {template_path}")
    
    for entry in os.listdir(dir_path_content):
        full_path = os.path.join(dir_path_content, entry)
        if os.path.isfile(full_path):
            if entry.endswith(".md"):
                #TODO: Debug path creation code
                
                # Convert the full path to a Path object
                path_obj = Path(full_path)
                # Get the relative path from the content directory
                rel_path = path_obj.relative_to(dir_path_content)
                # Create new path in public directory
                output_path = Path(dest_dir_path) / rel_path
                # Change extension from .md to .html
                output_path = output_path.with_suffix('.html')
                html_content = generate_page(full_path, template_path, output_path)       
                output_path.parent.mkdir(parents=True, exist_ok=True)

        elif os.path.isdir(full_path):
            generate_pages_recursive(full_path, template_path, dest_dir_path)