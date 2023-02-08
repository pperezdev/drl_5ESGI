import time

import tensorflow as tf
import numpy as np

from ..games import Game

class Reinforce:
    def __init__(self, learning_rate, state_size, action_size):
        self.learning_rate = learning_rate
        self.state_size = state_size
        self.action_size = action_size
        self.model = self._build_model()
        self.optimizers = tf.keras.optimizers.Adam(self.learning_rate)

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

    def forward(self,state, action,  reward):
        with tf.GradientTape() as tape:
            prob_action = self.model(state)
            selected_prob_action =
            log_pi = tf.math.log(selected_prob_action * reward)

        grads = tape.gradient(log_pi, self.model.trainable_variables)
        self.optimizers.apply_gradients(grads, self.model.trainable_variables)


    def use(self, game:Game, agent:Reinforce):
        state = game.reset()
        arr_state, arr_actions, arr_reward = [], [], []
        total_rewards = 0
        i = 0

        while game.status == "play":
            time.sleep(1)
            action = agent.choose_action(state)
            next_state, reward, status, _ = game.step(action, i)

            #add value on array
            arr_state.append(state)
            arr_reward.append(reward)
            total_rewards += reward
            state = next_state

        game.stop()
        agent.forward(np.array(arr_state),np.array())




