class GameOfLife():
	def __init__(self, grid):
		self.grid = grid

	def addPoint(self, x, y):
		self.grid[(x, y)] = True

	def evolve(self):
		print ''

	def getNeighbors(self, x, y):
		neighbors = []

		if not self.grid.has_key((x, y)):
			return neighbors

		return neighbors