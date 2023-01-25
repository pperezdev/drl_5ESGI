import os

class FileManager:
    def __init__(self) -> None:
        self.main_path  = os.path.dirname(os.path.abspath(__file__))[:-13]

    def __open_file(self, path:str) -> str:
        data = ""
        with open(path, 'r') as f:
            data += f.read()
        return data
    
    def open_file(self, path:str) -> str:
        return self.__open_file(f"{self.main_path}{path}")
         
    
    def open_custom_file(self, path:str) -> str:
        return self.__open_file(path)