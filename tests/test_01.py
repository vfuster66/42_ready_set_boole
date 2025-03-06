import unittest
from ex01.multiplier import multiplier
from colorama import Fore, Style


class TestMultiplier(unittest.TestCase):
    def print_test(self, test_name, operation, expected, obtained):
        """ Affichage amélioré du test avec couleurs et détails """
        print(f"\n{Fore.CYAN}Test: {test_name}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Opération :{Style.RESET_ALL} {operation}")
        print(f"{Fore.GREEN}Résultat attendu :{Style.RESET_ALL} {expected}")
        print(f"{Fore.BLUE}Résultat obtenu  :{Style.RESET_ALL} {obtained}")

        if expected == obtained:
            print(f"{Fore.GREEN}✅ Test OK !{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Test ÉCHOUÉ !{Style.RESET_ALL}")
        print("-" * 50)

    def test_basic_multiplication(self):
        a, b = 2, 3
        expected = 6
        result = multiplier(a, b)
        self.print_test(
            "Multiplication de base", f"{a} * {b}", expected, result
        )
        self.assertEqual(result, expected)

        a, b = 7, 8
        expected = 56
        result = multiplier(a, b)
        self.print_test(
            "Multiplication simple", f"{a} * {b}", expected, result
        )
        self.assertEqual(result, expected)

    def test_with_zero(self):
        a, b = 0, 5
        expected = 0
        result = multiplier(a, b)
        self.print_test(
            "Multiplication avec zéro", f"{a} * {b}", expected, result
        )
        self.assertEqual(result, expected)

        a, b = 10, 0
        expected = 0
        result = multiplier(a, b)
        self.print_test(
            "Multiplication avec zéro (autre sens)",
            f"{a} * {b}", expected, result
        )
        self.assertEqual(result, expected)

    def test_large_numbers(self):
        a, b = 1000000, 2000000
        expected = 2000000000000
        result = multiplier(a, b)
        self.print_test(
            "Multiplication de grands nombres", f"{a} * {b}", expected, result
        )
        self.assertEqual(result, expected)

    def test_commutativity(self):
        a, b = 3, 5
        expected = multiplier(b, a)
        result = multiplier(a, b)
        self.print_test(
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

    def test_associativity(self):
        a, b, c = 2, 3, 4
        expected = multiplier(multiplier(a, b), c)
        result = multiplier(a, multiplier(b, c))
        self.print_test(
            "Propriété associative",
            f"({a} * {b}) * {c} == {a} * ({b} * {c})",
            expected,
            result
        )
        self.assertEqual(result, expected)

    def test_multiplication_by_one(self):
        a = 42
        expected = a
        result = multiplier(a, 1)
        self.print_test("Multiplication par 1", f"{a} * 1", expected, result)
        self.assertEqual(result, expected)

        result = multiplier(1, a)
        self.print_test(
            "Multiplication par 1 (ordre inversé)",
            f"1 * {a}", expected, result
        )
        self.assertEqual(result, expected)

    def test_max_integer(self):
        import sys
        a, b = sys.maxsize, 2
        expected = a * b
        result = multiplier(a, b)
        self.print_test(
            "Multiplication du plus grand entier possible",
            f"{a} * {b}",
            expected,
            result
        )
        self.assertEqual(result, expected)

    def test_carry_multiplication(self):
        a, b = 15, 3
        expected = 45
        result = multiplier(a, b)
        self.print_test(
            "Test de la retenue binaire", f"{a} * {b}", expected, result
        )
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
