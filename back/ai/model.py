from ..services import FileManager
import numpy as np
import uuid

class Model:
    def __init__(self, type_algo:str=None, env:str=None, model:np.ndarray=None):
        self.type_algo = type_algo
        self.env = env
        self.model = model
        
    def save(self, path:str=None):
        if path == None:
            path = f"model_{self.env}_{self.type_algo}_{uuid.uuid1()}"
        fm = FileManager()
        fm.save_model(path, self.model)
        
    def load(self, path):
        fm = FileManager()
        self.model = fm.load_model(path)
        