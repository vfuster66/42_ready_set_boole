import unittest
from ex01.multiplier import multiplier
from printer import print_test_result


class TestMultiplier(unittest.TestCase):

    def test_basic_multiplication(self):
        cases = [
            (2, 3, 6, "Multiplication de base"),
            (7, 8, 56, "Multiplication simple")
        ]
        for a, b, expected, desc in cases:
            result = multiplier(a, b)
            print_test_result(desc, f"{a} * {b}", expected, result)
            self.assertEqual(result, expected)

    def test_with_zero(self):
        cases = [
            (0, 5, 0, "Multiplication par zéro"),
            (10, 0, 0, "Multiplication par zéro (autre sens)")
        ]
        for a, b, expected, desc in cases:
            result = multiplier(a, b)
            print_test_result(desc, f"{a} * {b}", expected, result)
            self.assertEqual(result, expected)

    def test_large_numbers(self):
        cases = [
            (1000, 2000, 2000000, "Multiplication de grands nombres"),
            (123456, 654321, 80779853376,
             "Multiplication de très grands nombres")
        ]
        for a, b, expected, desc in cases:
            result = multiplier(a, b)
            print_test_result(desc, f"{a} * {b}", expected, result)
            self.assertEqual(result, expected)

    def test_commutativity(self):
        a, b = 3, 5
        expected = multiplier(b, a)
        result = multiplier(a, b)
        print_test_result(
            "Commutativité de la multiplication",
            f"{a} * {b} == {b} * {a}",
            expected,
            result
        )
        self.assertEqual(result, expected)

    def test_negatives_should_fail(self):
        a, b = -5, 3
        with self.assertRaises(ValueError):
            multiplier(a, b)

    def test_invalid_inputs(self):
        invalid_inputs = [("10", 5), (5, None), ("a", "b")]
        for a, b in invalid_inputs:
            with self.assertRaises(TypeError):
                multiplier(a, b)

    def test_multiply_by_one(self):
        a = 42
        expected = a
        result = multiplier(a, 1)
        print_test_result("Multiplication par 1", f"{a} * 1", expected, result)
        self.assertEqual(result, expected)

    def test_associativity(self):
        a, b, c = 3, 5, 7
        expected = multiplier(multiplier(a, b), c)
        result = multiplier(a, multiplier(b, c))
        print_test_result(
            "Propriété associative",
            f"({a} * {b}) * {c} == {a} * ({b} * {c})",
            expected,
            result
        )
        self.assertEqual(result, expected)

    def test_max_integer(self):
        import sys
        a, b = sys.maxsize, 1
        expected = a * b
        result = multiplier(a, b)
        print_test_result(
            "Multiplication du plus grand entier possible",
            f"{a} * {b}",
            expected,
            result
        )
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
