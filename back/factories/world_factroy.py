from ..services import *
from ..constant import *
from ..worlds import *

def open_number_world(map_name:str, custom_path:str="", tp:World=World, *agrs, **kwargs) -> World:
    fm  = FileManager()
    if custom_path == "":
        return tp(fm.open_file(f"{map_number_path}{map_name}"), *agrs, **kwargs)
    else:
        return tp(fm.open_custom_file(custom_path), *agrs, **kwargs)

def open_color_world(map_name:str, custom_path:str="", tp:World=World, *agrs, **kwargs) -> World:
    fm  = FileManager()
    if custom_path == "":
        return tp(fm.open_file(f"{map_color_path}{map_name}"), *agrs, **kwargs)
    else:
        return tp(fm.open_custom_file(custom_path), *agrs, **kwargs)

def open_world(is_color:bool,map_name:str, custom_path:str="", tp:World=World, *agrs, **kwargs) -> World:
    if is_color:
        return open_color_world(map_name, custom_path, tp, *agrs, **kwargs)
    else:
        return open_number_world(map_name, custom_path, tp, *agrs, **kwargs)