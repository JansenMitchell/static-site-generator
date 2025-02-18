import os
import shutil
from generate_page import generate_page

def copy_source_to_destination(source, destination):
    if os.path.exists(destination):
        try:
            shutil.rmtree(destination)
            print(f"Directory '{destination}' and its contents have been removed.")
        except Exception as e:
            print(f"Error removing '{destination}': {e}")
    os.mkdir(destination)
    
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)
        if os.path.isfile(source_path):
            print(f"Copying file: {source_path} -> {dest_path}")
            shutil.copy(source_path, dest_path)
        elif os.path.isdir(source_path):
            print(f"Processing directory: {source_path}")
            copy_source_to_destination(source_path, dest_path)
            
def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.makedirs("public")
    copy_source_to_destination("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()