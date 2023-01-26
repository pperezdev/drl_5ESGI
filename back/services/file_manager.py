import os
import pickle 

class FileManager:
    def __init__(self) -> None:
        self.main_path  = os.path.dirname(os.path.abspath(__file__))[:-13]

    def __open_file(self, path:str) -> str:
        data = ""
        with open(path, 'r') as f:
            data += f.read()
        return data
    
    def __open_pickle_file(self, path:str) -> str:
        with open(path, 'rb') as f:
            data = pickle.load(f)
        return data
    
    def __write_file__(self, path:str, data) -> str:
        print(data)
        print(type(data))
        with open(path, 'wb') as f:
            pickle.dump(data, f)
    
    def open_file(self, path:str) -> str:
        return self.__open_file(f"{self.main_path}{path}")
    
    def open_custom_file(self, path:str) -> str:
        return self.__open_file(path)
    
    def save_model(self, path:str, data):
        self.__write_file__(f"{self.main_path}models/{path}.pickle", data)
        
    def load_model(self, path:str):
        return self.__open_pickle_file(f"{self.main_path}models/{path}.pickle")