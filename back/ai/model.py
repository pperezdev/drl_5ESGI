from ..services import FileManager
import uuid
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Input
from keras.optimizers import Adam

class ModelQLearning:
    def __init__(self, type_algo:str=None, env:str=None, model=None, is_keras:bool=False):
        self.type_algo = type_algo
        self.env = env
        self.model = model
        self.is_keras = is_keras
            
    
    def normal_save(self, path:str):
        fm = FileManager()
        fm.save_model(path, self.model)
        
    def keras_save(self, path:str):
        self.model.save(f"models/{path}")
        
    def save(self, path:str=None):
        if path == None:
            path = f"model_{self.env}_{self.type_algo}_{uuid.uuid1()}"
        
        if self.is_keras:
            self.keras_save(path)
        else:
            self.normal_save(path)
            
        fm = FileManager()
        fm.save_model(path, self.model)
        
    def load(self, path:str):
        if self.is_keras:
            self.model = tf.keras.models.load_model(f"models/{path}")
        else:
            fm = FileManager()
            self.model = fm.load_model(path)
        