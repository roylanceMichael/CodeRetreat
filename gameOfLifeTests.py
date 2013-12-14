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


def main():
    unittest.main()

if __name__ == '__main__':
	main()