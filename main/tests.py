from django.test import TestCase

# Create your tests here.

class SimpleTest(TestCase):
	"""docstring for SimpleTest"""
	def test_basic_addition(self):
		"""
			Tests that 1+1 is equal 2
		"""
		self.assertEqual(1 + 1, 2)