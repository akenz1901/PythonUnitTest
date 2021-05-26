import unittest
from calculator_fuctions import add
from calculator_fuctions import subtraction
from calculator_fuctions import multiplication
from calculator_fuctions import quotient


class CalculatorFunctions(unittest.TestCase):
    def test_add_result(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(277777777, 50000000), 277777777 + 50000000)

    def test_add_result_type(self):
        self.assertIsInstance(add(2, 3), int)
        self.assertIsInstance(add(-2, -3), int)
        self.assertIsInstance(add(-2, 3), int)
        self.assertIsInstance(add(277777777, 50000000), int)

    def test_add_non_int_type(self):
        with self.assertRaises(TypeError):
            add(2, "d")

    def test_subtract_result(self):
        self.assertEqual(subtraction(3, 2), 1)
        self.assertEqual(subtraction(2, 3), -1)
        self.assertEqual(subtraction(-2, -2), 0)
        self.assertEqual(subtraction(773444444, 283833838), 773444444 - 283833838)

    def test_subtraction_type_is_int(self):
        self.assertIsInstance(subtraction(3, 2), int)
        self.assertIsInstance(subtraction(2, 1), int)
        self.assertIsInstance(subtraction(2, 3), int)
        self.assertIsInstance(subtraction(773444444, 283833838), int)

    def test_subtraction_non_int_type(self):
        with self.assertRaises(TypeError):
            subtraction(5, "T")

    def test_multiplication_result(self):
        self.assertEqual(multiplication(3, 2), 6)
        self.assertEqual(multiplication(-1, -2), 2)
        self.assertEqual(multiplication(4, 0), 0)
        self.assertEqual(multiplication(566969, 32434), 566969*32434)

    def test_multiplication_type_is_int(self):
        self.assertIsInstance(multiplication(3, 2), int)
        self.assertIsInstance(multiplication(4, 64), int)
        self.assertIsInstance(multiplication(-2, -2), int)
        self.assertIsInstance(multiplication(4, 0), int)

    def test_multiplication_non_int_type(self):
        with self.assertRaises(TypeError):
            multiplication("0", "w")

    def test_quotient_result(self):
        self.assertEqual(quotient(46, 2), 23)
        self.assertEqual(quotient(8, 4), 2)
        self.assertEqual(quotient(100000, 100), 100000//100)

    def test_quotient_type_is_int(self):
        self.assertIsInstance(quotient(32, 1), int)
        self.assertIsInstance(quotient(4, 2), int)
        self.assertIsInstance(quotient(466, 3), int)
        self.assertIsInstance(quotient(858545, 44), int)

    def test_quotient_non_int_type(self):
        with self.assertRaises(TypeError):
            quotient("88383", 1)


if __name__ == '__main__':
    unittest.main()
