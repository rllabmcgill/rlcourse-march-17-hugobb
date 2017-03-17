import numpy as np

class Database(object):
    def __init__(self, state_space, lamda=0.5, threshold=0.9):
        self.bad_trajectories = []
        self.good_trajectories = []
        self.concept_peak = np.zeros(state_space)
        self.lamda = lamda
        self.threshold = threshold
        self.log_dd = np.zeros(state_space)

    def update(self, trajectory, done):
        p = np.zeros(self.log_dd.shape)
        idx_x = np.tile(np.arange(self.log_dd.shape[0]), (self.log_dd.shape[1],1)).T
        idx_y = np.tile(np.arange(self.log_dd.shape[1]), (self.log_dd.shape[0],1))
        if done:
            self.good_trajectories.append(trajectory)
            for observation in trajectory:
                x, y = observation
                p += np.log(1 - np.exp(-1/2*((x-idx_x)**2 + (y-idx_y)**2))/np.sqrt(2*np.pi))
            self.log_dd += np.log(1 - np.exp(p))

        else:
            self.bad_trajectories.append(trajectory)
            for observation in trajectory:
                x, y = observation
                p += np.log(1 - np.exp(-1/2*((x-idx_x)**2 + (y-idx_y)**2))/np.sqrt(2*np.pi))
            self.log_dd += p

        x = self.log_dd.argmax(axis=0)
        y = self.log_dd.max(axis=0).argmax()
        x = x[y]
        self.concept_peak[x,y] = self.lamda*(self.concept_peak[x,y] + 1)
        if self.concept_peak[x,y] >= self.threshold:
            return True

class QLearning(object):
    def __init__(self, state_space, action_space, gamma=0.9, lr=0.05, epsilon=0.9):
        self.q = np.zeros(state_space + (len(action_space),))
        self.gamma = gamma
        self.lr = lr
        self.epsilon = epsilon
        self.action_space = ['left', 'right', 'up', 'down']

    def get_action(self, observation):
        if np.random.binomial(1, self.epsilon):
            return np.random.choice(self.action_space)

        x, y = observation
        action = self.action_space[self.q[x, y].argmax()]

        return action

    def update(self, observation, action, new_observation, reward):
        x, y = observation
        new_x, new_y = new_observation
        action = self.action_space.index(action)
        self.q[x, y, action] += self.lr*(reward + self.gamma*self.q[new_x, new_y].max() - self.q[x, y, action])

    def get_V(self, p_failure=0.1):
        V = np.zeros(self.q.shape[:2])
        a = self.q.argmax(axis=2)
        for i in range(self.q.shape[0]):
            for j in range(self.q.shape[1]):
                p = np.ones(self.q.shape[-1])*p_failure/4
                p[a[i,j]] += 1-p_failure
                print p.sum
                V[i,j] = np.sum(p*self.q[i,j])
        return V
