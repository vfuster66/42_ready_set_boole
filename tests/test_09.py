import unittest
from ex09.set_evaluation import set_evaluation
from colorama import Fore, Style


class TestSetEvaluation(unittest.TestCase):
    def print_test(self, test_name, formula, sets, expected, obtained):
        """ Affichage amélioré du test avec couleurs et détails """
        print(f"\n{Fore.CYAN}Test: {test_name}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Formule :{Style.RESET_ALL} {formula}")
        print(f"{Fore.YELLOW}Ensembles :{Style.RESET_ALL} {sets}")
        print(f"{Fore.GREEN}Résultat attendu :{Style.RESET_ALL} {expected}")
        print(f"{Fore.BLUE}Résultat obtenu  :{Style.RESET_ALL} {obtained}")

        if expected == obtained:
            print(f"{Fore.GREEN}✅ Test OK !{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Test ÉCHOUÉ !{Style.RESET_ALL}")
        print("-" * 50)

    def test_basic_operations(self):
        test_cases = [
            ("AB|C&", [{1, 2}, {3, 4}, {2, 3}], {2, 3}),
            ("A!B|", [{1, 2}, {3, 4}], {3, 4}),
            ("AB&C|!", [{1, 2}, {2, 3}, {4}], {1, 3}),
        ]

        for formula, sets, expected in test_cases:
            result = set_evaluation(formula, sets)
            self.print_test("Opérations de base", formula, sets,
                            expected, result)
            self.assertEqual(result, expected)

    def test_complex_operations(self):
        test_cases = [
            ("AB|C&", [{1, 2}, {3, 4}, {2, 3}], {2, 3}),
            ("A!B|", [{1, 2}, {3, 4}], {3, 4}),
            ("AB&C|!", [{1, 2}, {2, 3}, {4}], {1, 3}),
        ]
        for formula, sets, expected in test_cases:
            result = set_evaluation(formula, sets)
            self.print_test("Opérations complexes", formula, sets,
                            expected, result)
            self.assertEqual(result, expected)

    def test_invalid_cases(self):
        invalid_cases = [
            ("", [{1, 2}]),
            ("A!", []),
            ("AB|C", [{1, 2}, {3, 4}]),
        ]
        for formula, sets in invalid_cases:
            with self.assertRaises(ValueError):
                set_evaluation(formula, sets)

    def test_additional_cases(self):
        test_cases = [
            ("AB^", [{1, 2}, {2, 3}], {1, 3}),
            ("AB>", [{1, 2}, {2, 3}], {2, 3}),
            ("AB=", [{1, 2}, {2, 3}], {2}),
            ("A!", [set()], set()),
            ("AB=", [{1, 2}, {2, 3}], {2}),
            ("A!B&", [{1, 2}, {2, 3}], {3}),
        ]

        for formula, sets, expected in test_cases:
            result = set_evaluation(formula, sets)
            self.print_test("Cas supplémentaires", formula, sets,
                            expected, result)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
