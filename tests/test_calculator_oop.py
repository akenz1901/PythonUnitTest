import unittest
from calculator_oop import Calculator


class CalculatorOopTest(unittest.TestCase):

    def test_add_result(self):
        self.assertEqual(Calculator.add(2, 3), 5)

    def test_add_result_type(self):
        self.assertIsInstance(Calculator.add(2, 3), int)
        self.assertIsInstance(Calculator.add(-2, -3), int)
        self.assertIsInstance(Calculator.add(-2, 3), int)
        self.assertIsInstance(Calculator.add(277777777, 50000000), int)

    def test_add_non_int_type(self):
        with self.assertRaises(TypeError):
            Calculator.add(2, "d")

    def test_subtract_result(self):
        self.assertEqual(Calculator.subtraction(3, 2), 1)
        self.assertEqual(Calculator.subtraction(2, 3), -1)
        self.assertEqual(Calculator.subtraction(-2, -2), 0)
        self.assertEqual(Calculator.subtraction(773444444, 283833838), 773444444 - 283833838)

    def test_subtraction_type_is_int(self):
        self.assertIsInstance(Calculator.subtraction(3, 2), int)
        self.assertIsInstance(Calculator.subtraction(2, 1), int)
        self.assertIsInstance(Calculator.subtraction(2, 3), int)
        self.assertIsInstance(Calculator.subtraction(773444444, 283833838), int)

    def test_subtraction_non_int_type(self):
        with self.assertRaises(TypeError):
            Calculator.subtraction(5, "T")

    def test_multiplication_result(self):
        self.assertEqual(Calculator.multiplication(3, 2), 6)
        self.assertEqual(Calculator.multiplication(-1, -2), 2)
        self.assertEqual(Calculator.multiplication(4, 0), 0)
        self.assertEqual(Calculator.multiplication(566969, 32434), 566969*32434)

    def test_multiplication_type_is_int(self):
        self.assertIsInstance(Calculator.multiplication(3, 2), int)
        self.assertIsInstance(Calculator.multiplication(4, 64), int)
        self.assertIsInstance(Calculator.multiplication(-2, -2), int)
        self.assertIsInstance(Calculator.multiplication(4, 0), int)

    def test_multiplication_non_int_type(self):
        with self.assertRaises(TypeError):
            Calculator.multiplication("0", "w")

    def test_quotient_result(self):
        self.assertEqual(Calculator.quotient(46, 2), 23)
        self.assertEqual(Calculator.quotient(8, 4), 2)
        self.assertEqual(Calculator.quotient(100000, 100), 100000//100)

    def test_quotient_type_is_int(self):
        self.assertIsInstance(Calculator.quotient(32, 1), int)
        self.assertIsInstance(Calculator.quotient(4, 2), int)
        self.assertIsInstance(Calculator.quotient(466, 3), int)
        self.assertIsInstance(Calculator.quotient(858545, 44), int)

    def test_quotient_non_int_type(self):
        with self.assertRaises(TypeError):
            Calculator.quotient("88383", 1)

    def test_mummy_level_of_understanding(self):
        self.assertEqual(Calculator.add(54, 6), 60)
        self.assertEqual(Calculator.take_care(), "Mum pls give me addition 60")


if __name__ == '__main__':
    unittest.main()
