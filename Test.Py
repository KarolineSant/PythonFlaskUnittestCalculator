import unittest
from Calculator import operation_result

class TestCalculator(unittest.TestCase):
    def test_raiz_quadrada(self):
        calculator = operation_result()
        calculator.setOperation('sqrt')
        calculator.setNumber1(25)
        result = operation_result.result()
        expected = 5.0
        self.assertEqual(result, expected)
    
    def test_exponenciacao(self):
        calculator = operation_result()
        calculator.setOperation('pow')
        calculator.setNumber1(10)
        calculator.setNumber2(2)
        result = operation_result.result()
        expected = 100.0
        self.assertEqual(result, expected)
    
    def test_logaritmo(self):
        calculator = operation_result()
        calculator.setOperation('log')
        calculator.setNumber1(4)
        result = operation_result.result()
        expected = 1.3862943611198906
        self.assertEqual(result, expected)