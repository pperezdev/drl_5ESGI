from .file_manager import FileManager

def get_structure(path) -> list:
    fm = FileManager()
    data = fm.open_file(path)
    structure = []
    for line in data.split('\n'):
        structure.append(line)
    return structure

def draw_map(path):
    structure = get_structure(path)

def color_to_number():
    pass