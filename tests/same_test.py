import unittest
from word_ladder import same

class test_same(unittest.TestCase):
   def  test_same(self):
       self.assertEqual(same('hide', 'seek'), 0)
       self.assertEqual(same('lead', 'gold'), 1)
       self.assertEqual(same('cat', 'rat'), 2)
       self.assertEqual(same('bats', 'cats'), 3)
if __name__ == '__main__':
    unittest.main()