import unittest
from ex00.adder import adder
from colorama import Fore, Style


class TestAdder(unittest.TestCase):
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

    def test_basic_addition(self):
        a, b = 2, 3
        expected = 5
        result = adder(a, b)
        self.print_test("Addition de base", f"{a} + {b}", expected, result)
        self.assertEqual(result, expected)

        a, b = 7, 8
        expected = 15
        result = adder(a, b)
        self.print_test("Addition simple", f"{a} + {b}", expected, result)
        self.assertEqual(result, expected)

    def test_with_zero(self):
        a, b = 0, 5
        expected = 5
        result = adder(a, b)
        self.print_test("Addition avec zéro", f"{a} + {b}", expected, result)
        self.assertEqual(result, expected)

        a, b = 10, 0
        expected = 10
        result = adder(a, b)
        self.print_test("Addition avec zéro (autre sens)",
                        f"{a} + {b}", expected, result)
        self.assertEqual(result, expected)

    def test_large_numbers(self):
        a, b = 1000000, 2000000
        expected = 3000000
        result = adder(a, b)
        self.print_test("Addition de grands nombres",
                        f"{a} + {b}", expected, result)
        self.assertEqual(result, expected)

        a, b = 123456789, 987654321
        expected = 1111111110
        result = adder(a, b)
        self.print_test("Addition de très grands nombres",
                        f"{a} + {b}", expected, result)
        self.assertEqual(result, expected)

    def test_commutativity(self):
        a, b = 3, 5
        expected = adder(b, a)
        result = adder(a, b)
        self.print_test("Commutativité de l'addition",
                        f"{a} + {b} == {b} + {a}",
                        expected, result)
        self.assertEqual(result, expected)

    def test_negatives_should_fail(self):
        a, b = -5, 3
        with self.assertRaises(ValueError):
            result = adder(a, b)
            self.print_test("Erreur attendue (nombre négatif)",
                            f"{a} + {b}", "Exception", result)

    def test_invalid_inputs(self):
        invalid_inputs = [("10", 5), (5, None), ("a", "b")]
        for a, b in invalid_inputs:
            with self.assertRaises(TypeError):
                result = adder(a, b)
                self.print_test("Erreur attendue (entrée invalide)",
                                f"{a} + {b}", "Exception", result)

    def test_add_same_number(self):
        a = 42
        expected = a + a
        result = adder(a, a)
        self.print_test("Addition du même nombre",
                        f"{a} + {a}", expected, result)
        self.assertEqual(result, expected)

    def test_associativity(self):
        a, b, c = 3, 5, 7
        expected = adder(adder(a, b), c)
        result = adder(a, adder(b, c))
        self.print_test(
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
        self.print_test(
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
        self.print_test(
            "Test de la retenue binaire", f"{a} + {b}", expected, result
        )
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
