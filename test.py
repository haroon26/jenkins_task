import unittest
from my_fact.fact import fact

class testFact(unittest.TestCase):
   def test_zero(self):
      data = 0
      result = fact(data)
      self.assertEqual(result, 1, "param = 0: passed")
   def test_one(self):
      data = 1
      result = fact(data)
      self.assertEqual(result, 1, "param = 1: passed")
   def test_low(self):
      data = 5
      result = fact(data)
      self.assertNotEqual(result, 150, "param = 5: passed")

if __name__ == '__main__':
   unittest.main()