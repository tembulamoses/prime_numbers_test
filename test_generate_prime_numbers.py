import unittest
from generate_prime_numbers import generate_prime_numbers

class Primenumbers(unittest.TestCase):
	"""
		first we have formula


    a prime number is found by the formula

    primenumbers = number if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1))


	"""

	def test_result_is_list(self):
		self.assertIsInstance(generate_prime_numbers(20), list)
	def test_five(self):
		self.assertEqual(generate_prime_numbers(5),[2,3,5])


	def test_ten(self):
		self.assertEqual(generate_prime_numbers(10),[2,3,5,7])

	def test_hundred(self):
		self.assertEqual(generate_prime_numbers(100),[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97])

