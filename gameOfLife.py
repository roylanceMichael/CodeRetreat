class GameOfLife():
	def __init__(self, grid):
		self.grid = grid

	def addPoint(self, x, y):
		self.grid[(x, y)] = True

	def evolve(self):
		print ''

	def getPossibleNeighbors(self, x, y):
		neighbors = []

		for deltaX in range(-1, 2):
			for deltaY in range(-1, 2):
				neighbors.append((x + deltaX, y + deltaY))

		return neighbors

	def countOfNeighborsAlive(self, x, y):
		possibleNeighbors = self.getPossibleNeighbors(x, y)

		aliveNeighbors = 0

		for key in possibleNeighbors:
			if key[0] == x and key[1] == y:
				continue

			if key in self.grid:
				aliveNeighbors += 1

		return aliveNeighbors