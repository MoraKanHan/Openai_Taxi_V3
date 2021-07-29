import numpy as np
from collections import defaultdict

class Agent:

    def __init__(self, nA=6, eps = 0.005):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))
        self.eps = eps

    def select_action(self, state):
        """ Given the state, select an action.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """
        policy_s = self.epsilon_greedy(state)
        return np.random.choice(np.arange(self.nA), p = policy_s )

    def step(self, state, action, reward, next_state, done, alpha = 0.01,gamma = 1.0):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        self.Q[state][action] +=  (alpha * (reward + (gamma * np.max(self.Q[next_state])) - self.Q[state][action]))
        
    def epsilon_greedy (self,state):
        policy_s = np.ones(self.nA) * self.eps / self.nA
        policy_s[np.argmax(self.Q[state])] = 1 - self.eps + (self.eps / self.nA)
        return policy_s