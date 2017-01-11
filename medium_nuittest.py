#!/usr/bin/env python

# Unittest is test method implemented in various programming languages.
# In python, it is implemented using module called 'unittest'.


# how to do unittest.
# 
# - inherit unittest TestCase class
# - define method called test_XXX
# - calling function that implements test executes a method named test_XXX of created class
# - test_XXX method is displayed as ok 'or' 'fail'.

import random
import unittest


class TestSequenceFunctions(unittest.TestCase):

  # initialize
  def setUp(self):
    self.seq = range(10)

  # testing 'self.seq' operated with random module
  def test_shuffle(self):
    random.shuffle(self.seq)
    self.seq.sort()
    self.assertEqual(self.seq, range(10))
    self.assertRaises(TypeError, random.shuffle, (1,2,3))
  
  # testing 'self.seq' operated with random module
  def test_choice(self):
    element = random.choice(self.seq)
    self.assertTrue(element in self.seq)


if __name__ == '__main__':
#  unittest.main()

#  suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
#  unittest.TextTestRunner(verbosity=2).run(suite)

# test_choice (__main__.TestSequenceFunctions) ... ok
# test_shuffle (__main__.TestSequenceFunctions) ... ok
#
#----------------------------------------------------------------------
# Ran 2 tests in 0.002s
#
# OK

