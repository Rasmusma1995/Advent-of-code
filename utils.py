import os

def read(name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, name)
    with open(file_path, 'r') as f:
        content = f.read()
    return content