import unittest
import gameOfLife

class GameOfLifeTesting(unittest.TestCase):
	 def test_objectExists(self):
	 	obj = gameOfLife.GameOfLife({})

	 	self.assertTrue(obj != None)


def main():
    unittest.main()

if __name__ == '__main__':
	main()