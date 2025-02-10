import os
import shutil

def copy_source_to_destination(source, destination):
    if os.path.exists(destination):
        try:
            shutil.rmtree(destination)
            print(f"Directory '{destination}' and its contents have been removed.")
        except Exception as e:
            print(f"Error removing '{destination}': {e}")