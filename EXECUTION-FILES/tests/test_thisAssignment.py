# NOTE: This file MUST be named test_SOMETHING, i.e. not SOMETHING_test
# And the functions in it must start with test_SOMETHING not SOMETHING_test
# if you want them to be run as tests (via auto-discovery)

import unittest
import pytest
from gradescope_utils.autograder_utils.decorators import weight,visibility, partial_credit, number

from labxx import *

class TestConversion(unittest.TestCase):

  def setUp(self):
    pass

  @weight(10)
  def test_addEm_1(self):
    self.assertEqual(addEm(2,4),6)

  # This one is hidden only until after the due date
    
  @weight(20)
  @visibility('after_due_date')
  def test_addEm_2(self):
    self.assertEqual(addEm(3,1),4)


  # This one is hidden forever
  # Students will only see a point total of the visible tests they got correct
  
  @weight(20)
  @visibility('hidden')
  def test_addEm_2(self):
    self.assertEqual(addEm(3,1),4)
    
  # This one is worth 10 points, but is only worth 5 if they get it wrong
  # It is also hidden until after the due date

  @visibility('after_due_date')
  @partial_credit(20)
  def test_addEm_3(self, set_score = None):
    
    inputs = [(2,2),(3,3),(4,4),(5,5)]
    outputs = [4,6,8,10]

    score = 0
    for vin, vout in zip(inputs, outputs):
      try:
        if addEm(*vin) == vout:
          score += 5
      except:
        pass
      finally:
        if set_score:
          set_score(score)