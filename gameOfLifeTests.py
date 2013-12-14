import unittest
import gameOfLife

class GameOfLifeTesting(unittest.TestCase):
	 def test_objectExists(self):
	 	obj = gameOfLife.GameOfLife({})

	 	self.assertTrue(obj != None)

	 def test_addPointToGame(self):
	 	grid = {}
	 	obj = gameOfLife.GameOfLife(grid)

	 	self.assertTrue(len(grid) == 0)

	 	obj.addPoint(0, 0)

	 	self.assertTrue(len(grid) == 1)

	 def test_evolveFromOnePoint(self):
	 	grid = {}
	 	obj = gameOfLife.GameOfLife(grid)

	 	obj.evolve()

		self.assertTrue(len(grid) == 0)	 
	
	 def test_evolveFromFourPoints(self):
	 	grid = {}
	 	obj = gameOfLife.GameOfLife(grid)

	 	obj.addPoint(0, 0)
	 	obj.addPoint(1, 0)
	 	obj.addPoint(0, 1)
	 	obj.addPoint(1, 1)

	 	self.assertTrue(len(grid) == 4)	

	 	obj.evolve()
	 	
		self.assertTrue(len(grid) == 4)	 	

	 def test_getPossibleNeighbors(self):
		grid = {}
	 	obj = gameOfLife.GameOfLife(grid)

	 	neighborTuples = obj.getPossibleNeighbors(0, 0)

	 	self.assertTrue(len(neighborTuples) == 9)

	 def test_countOfNeighborsAlive(self):
	 	grid = {}
	 	obj = gameOfLife.GameOfLife(grid)

	 	obj.addPoint(0, 0)
	 	obj.addPoint(1, 0)
	 	obj.addPoint(0, 1)

	 	aliveNeighbors = obj.countOfNeighborsAlive(0, 0)

	 	self.assertTrue(aliveNeighbors == 2)


def main():
    unittest.main()

if __name__ == '__main__':
	main()