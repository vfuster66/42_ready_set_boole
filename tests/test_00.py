import unittest
from ex00.adder import adder
from printer import print_test_result


class TestAdder(unittest.TestCase):

    def test_basic_addition(self):
        cases = [
            (2, 3, 5, "Addition de base"),
            (7, 8, 15, "Addition simple")
        ]
        for a, b, expected, desc in cases:
            result = adder(a, b)
            print_test_result(desc, f"{a} + {b}", expected, result)
            self.assertEqual(result, expected)

    def test_with_zero(self):
        cases = [
            (0, 5, 5, "Addition avec zéro"),
            (10, 0, 10, "Addition avec zéro (autre sens)")
        ]
        for a, b, expected, desc in cases:
            result = adder(a, b)
            print_test_result(desc, f"{a} + {b}", expected, result)
            self.assertEqual(result, expected)

    def test_large_numbers(self):
        cases = [
            (1000000, 2000000, 3000000, "Addition de grands nombres"),
            (123456789, 987654321, 1111111110,
             "Addition de très grands nombres")
        ]
        for a, b, expected, desc in cases:
            result = adder(a, b)
            print_test_result(desc, f"{a} + {b}", expected, result)
            self.assertEqual(result, expected)

    def test_commutativity(self):
        a, b = 3, 5
        expected = adder(b, a)
        result = adder(a, b)
        print_test_result(
            "Commutativité de l'addition",
            f"{a} + {b} == {b} + {a}",
            expected,
            result
        )
        self.assertEqual(result, expected)

    def test_negatives_should_fail(self):
        a, b = -5, 3
        with self.assertRaises(ValueError):
            adder(a, b)
            print_test_result("Erreur attendue (nombre négatif)", f"{a} + {b}",
                              "Exception", "Pas levée")

    def test_invalid_inputs(self):
        invalid_inputs = [("10", 5), (5, None), ("a", "b")]
        for a, b in invalid_inputs:
            with self.assertRaises(TypeError):
                adder(a, b)
                print_test_result(
                    "Erreur attendue (entrée invalide)",
                    f"{a} + {b}",
                    "Exception",
                    "Pas levée"
                )

    def test_add_same_number(self):
        a = 42
        expected = a + a
        result = adder(a, a)
        print_test_result("Addition du même nombre",
                          f"{a} + {a}", expected, result)
        self.assertEqual(result, expected)

    def test_associativity(self):
        a, b, c = 3, 5, 7
        expected = adder(adder(a, b), c)
        result = adder(a, adder(b, c))
        print_test_result(
            "Propriété associative",
            f"({a} + {b}) + {c} == {a} + ({b} + {c})",
            expected,
            result
        )
        self.assertEqual(result, expected)

    def test_max_integer(self):
        import sys
        a, b = sys.maxsize, 1
        expected = a + b
        result = adder(a, b)
        print_test_result(
            "Addition du plus grand entier possible",
            f"{a} + {b}",
            expected,
            result
        )
        self.assertEqual(result, expected)

    def test_carry_addition(self):
        a, b = 15, 1
        expected = 16
        result = adder(a, b)
        print_test_result(
            "Test de la retenue binaire",
            f"{a} + {b}",
            expected,
            result
        )
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
