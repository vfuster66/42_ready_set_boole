import unittest
from ex07.sat import sat
from colorama import Fore, Style


class TestSAT(unittest.TestCase):
    def print_test(self, test_name, formula, expected, obtained):
        """ Affichage amélioré du test avec couleurs et détails """
        print(f"\n{Fore.CYAN}Test: {test_name}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Formule :{Style.RESET_ALL} {formula}")
        print(f"{Fore.GREEN}Résultat attendu :{Style.RESET_ALL} {expected}")
        print(f"{Fore.BLUE}Résultat obtenu :{Style.RESET_ALL} {obtained}")
        if expected == obtained:
            print(f"{Fore.GREEN}✅ Test OK !{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Test ÉCHOUÉ !{Style.RESET_ALL}")
        print("-" * 50)

    def test_basic_sat(self):
        test_cases = {
            "AB|": True,
            "AB&": True,
            "AA!&": False,
            "AA^": False
        }
        for formula, expected in test_cases.items():
            result = sat(formula)
            self.print_test("Test SAT basique", formula, expected, result)
            self.assertEqual(result, expected)

    def test_complex_sat(self):
        test_cases = {
            "ABC|&": True,
            "A!B!|": True,
            "AB&C|!": True
        }
        for formula, expected in test_cases.items():
            result = sat(formula)
            self.print_test("Test SAT complexe", formula, expected, result)
            self.assertEqual(result, expected)

    def test_invalid_sat(self):
        invalid_cases = ["", "A!", "ABC|", "A>"]
        for formula in invalid_cases:
            with self.assertRaises(ValueError):
                sat(formula)

    def test_always_false(self):
        formula = "AB&A!"
        expected = False
        result = sat(formula)
        self.print_test("Formule toujours fausse", formula, expected, result)
        self.assertEqual(result, expected)

    def test_always_true(self):
        formula = "AA|!"
        expected = True
        result = sat(formula)
        self.print_test(
            "Formule toujours vraie (tautologie)", formula, expected, result
            )
        self.assertEqual(result, expected)

    def test_implication(self):
        formula = "AB>!"
        expected = False
        result = sat(formula)
        self.print_test(
            "Négation d'une implication", formula, expected, result
            )
        self.assertEqual(result, expected)

    def test_equivalence(self):
        formula = "AB="
        expected = True
        result = sat(formula)
        self.print_test(
            "Équivalence entre deux variables", formula, expected, result
            )
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
