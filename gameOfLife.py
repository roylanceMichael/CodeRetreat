class GameOfLife():
	def __init__(self, grid):
		self.grid = grid

	def addPoint(self, x, y):
		self.grid[(x, y)] = True

	def evolve(self):
		print ''