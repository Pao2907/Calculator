#try
import unittest
from main import Calculator

class Test(unittest.TestCase):
  def test_00_addition(self):
    solve = "1+1"
    self.assertEqual(Calculator(Solve), 2)

  def test_00_addition(self):
    solve = "2+2+2+2"
    self.assertEqual(Calculator(Solve), 8)
    
  def test_00_subtraction(self):
    solve = "1-1"
    self.assertEqual(Calculator(Solve), 0) 

  def test_00_subtraction(self):
    solve = "100-10-25-5"
    self.assertEqual(Calculator(Solve), 60)

  def test_00_multiplication(self):
    solve = "10*10"
    self.assertEqual(Calculator(Solve), 100)
 
  def test_00_multiplication(self):
    solve = "10*5*10"
    self.assertEqual(Calculator(Solve), 500)
    
  def test_00_division(self):
    solve = "138/2"
    self.assertEqual(Calculator(Solve), 69)
    
  def test_00_division(self):
    solve = "138/2/3"
    self.assertEqual(Calculator(Solve), 23)
    
   def test_00_mix(self):
    solve = "1+2*3/4"
    self.assertEqual(Calculator(Solve), 2.5)
    
   def test_00_mix_1(self):
    solve = "1/2*3-4"
    self.assertEqual(Calculator(Solve), -2.5)  
  
if __name__ == "_main_":
  unittest.main()
