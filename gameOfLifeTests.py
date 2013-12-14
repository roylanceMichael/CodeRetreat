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

	 def test_getNeighbors(self):
		grid = {}
	 	obj = gameOfLife.GameOfLife(grid)

	 	obj.addPoint(0, 0)
	 	obj.addPoint(1, 0)
	 	obj.addPoint(0, 1)

	 	neighborTuples = obj.getNeighbors(5, 0)

	 	self.assertTrue(len(neighborTuples) == 0)
	 		


def main():
    unittest.main()

if __name__ == '__main__':
	main()