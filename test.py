import unittest
import tkinter 
import _tkinter
from main import CalculatorWindow

class TestCaseCalcu(unittest.TestCase):

	def setUp(self):
		self.root=tkinter.Tk()
		self.pump_events()

	def tearDown(self):
		if self.root:
			self.root.destroy()
			self.pump_events()

	def pump_events(self):
		while self.root.dooneevent(_tkinter.ALL_EVENTS | _tkinter.DONT_WAIT):
			pass

class TestCalcu(TestCaseCalcu):
	def test_click(self):
		c=CalculatorWindow(self.root)
		self.pump_events()
		self.assertEqual(c.click('1'), '1')
		self.assertEqual(c.click('+2'), '1+2')
		self.assertEqual(c.entry.get(), '1+2')
		self.assertEqual(c.expr["text"], '1+2')


	def test_eval(self):
		c=CalculatorWindow(self.root)
		self.pump_events()
		expression = '(1-2)*3 + 1/2'
		c.click(expression)
		self.assertEqual(c.entry.get(), expression)
		c.evaluate()
		self.assertEqual(c.entry.get(),'-2.5')
		self.assertEqual(c.expr["text"], '(1-2)*3 + 1/2')
		self.assertTrue(c.new, msg="succesfully evaluated")

		#math error
		error = "Math Error"
		c.click("1/0")
		c.evaluate()
		self.assertEqual(c.entry.get(), error)

		#syntax error
		error = "Syntax Error"
		c.click("(9*2)+1)")
		c.evaluate()
		self.assertEqual(c.entry.get(), error)

	def test_deleteAll(self):
		c=CalculatorWindow(self.root)
		self.pump_events()
		expression = '1-2*3'
		c.click(expression)
		c.deleteAll()
		self.assertEqual(c.entry.get(), '')
		self.assertEqual(c.expr["text"], '')

	def test_deleteOne(self):
		c=CalculatorWindow(self.root)
		self.pump_events()
		expression = '1-2*3'
		c.click(expression)
		c.deleteOne()
		self.assertEqual(c.entry.get(), '1-2*')
		self.assertEqual(c.expr["text"], '1-2*')





if __name__ == '__main__':
    import unittest
    unittest.main()
