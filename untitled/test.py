import unittest
import main

class Test(unittest.TestCase):
	def test1(self):
		result = main.guesser(1,1)
		self.assertTrue(result)
	def test2(self):
		result = main.guesser(1,9)
		self.assertFalse(result)

if __name__ == '__main__':
	unittest.main()