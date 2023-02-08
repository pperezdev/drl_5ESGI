import tensorflow as tf
import numpy as np


class Reinforce:
    def __init__(self, learning_rate, state_size, action_size):
        self.learning_rate = learning_rate
        self.state_size = state_size
        self.action_size = action_size
        self.model = self._build_model()

    def _build_model(self):
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Dense(16, input_dim=self.state_size, activation='relu'))
        model.add(tf.keras.layers.Dense(16, activation='relu'))
        model.add(tf.keras.layers.Dense(self.action_size, activation='softmax'))
        return model

    def choose_action(self, state):
        state = np.reshape(state(-1, self.state_size))
        action_probs = self.model.predict(state)
        action = np.random.choice(self.action_size, p=action_probs[0])
        return action


    def forward(self,state, reward):
        pass
