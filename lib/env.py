import numpy as np

class GridWorld(object):
    def __init__(self, p_failure=0.1):
        self.p_failure = p_failure
        self.action_space = ['left', 'right', 'up', 'down']

        self.state_space = self.border.shape

    def render(self):
        print self.observation

    def reset(self):
        observation = self.pos_init()
        self.observation = observation
        return observation

    def step(self, action):
        x, y = self.observation

        if np.random.binomial(1, self.p_failure):
            action = np.random.choice(self.action_space)

        if action == 'left':
            if not self.border[x , y - 1]:
                y = y - 1

        elif action == 'right':
            if not self.border[x, y + 1]:
                y = y + 1

        elif action == 'up':
            if not self.border[x - 1, y]:
                x = x - 1

        elif action == 'down':
            if not self.border[x + 1,y]:
                x = x + 1
        else:
            raise ValueError()

        observation = (x,y)
        self.observation = observation
        reward = 0
        done = False
        if observation == self.reward:
            done = True
            reward = 1
        info = None

        return observation, reward, done, info

class TwoRoom(GridWorld):
    def __init__(self, **kwargs):
        self.border = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                                [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                                [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                                [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

        super( TwoRoom, self ).__init__(**kwargs)

        self.pos_init = lambda: (np.random.randint(1,6), np.random.randint(1,6))
        self.reward = (5,11)

class FourRoom(GridWorld):
    def __init__(self, reward=(11,11),**kwargs):
        self.border = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                                [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                                [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                                [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                                [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                                [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                                [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                                [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                                [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

        super( FourRoom, self ).__init__(**kwargs)

        self.pos_init = lambda: (np.random.randint(1,6), np.random.randint(1,6))
        self.reward = reward
