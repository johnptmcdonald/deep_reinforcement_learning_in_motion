import numpy as np


actionSpace = {
	'U': (-1,0),
	'D': (1,0),
	'L': (0,-1),
	'R': (0,1),	
}

class Agent(object):
	
	def __init__(self, maze, alpha=0.15, randomFactor=0.2):
		self.state_history = [((0,0), 0)]
		self.alpha = alpha
		self.G = {}
		self.initReward(maze.allowedStates)
		self.actionSpace = [0,1,2,3]
		self.randomFactor = 0.2
		

	def initReward(self, states):
		for state in states:
			self.G[state] = np.random.uniform(low=-1.0, high=-0.1)

	def choose_action(self, state, allowedMoves):
		maxG = -10e15
		randomNum = np.random.random()
		if randomNum < self.randomFactor:
			nextMove = np.random.choice(allowedMoves)
		else:
			for action in allowedMoves:
				newState = tuple([sum(x) for x in zip(state, actionSpace[action])])
				if self.G[newState] >= maxG:
					nextMove = action
					maxG = self.G[newState]

		return nextMove

	def update_state_history(self, state, reward):
		self.state_history.append((state, reward))

	def learn(self):
		target = 0
		for prev, reward in reversed(self.state_history):
			self.G[prev] = self.G[prev] + self.alpha * (target - self.G[prev])
			target += reward

		self.state_history = []

		self.randomFactor -= 10e-5


