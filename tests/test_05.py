import unittest
from ex05.negation_normal_form import negation_normal_form
from colorama import Fore, Style


class TestNNFConversion(unittest.TestCase):
    def print_test(self, test_name, formula, expected, obtained):
        """ Affichage amélioré du test avec couleurs et détails """
        print(f"\n{Fore.CYAN}Test: {test_name}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Formule :{Style.RESET_ALL} {formula}")
        print(f"{Fore.GREEN}Résultat attendu :{Style.RESET_ALL} {expected}")
        print(f"{Fore.BLUE}Résultat obtenu  :{Style.RESET_ALL} {obtained}")

        if expected == obtained:
            print(f"{Fore.GREEN}✅ Test OK !{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Test ÉCHOUÉ !{Style.RESET_ALL}")
        print("-" * 50)

    def test_basic_nnf(self):
        test_cases = {
            "AB&!": "A!B!|",
            "AB|!": "A!B!&",
            "AB>": "A!B|",
            "AB=": "AB&A!B!&|",
            "AB|C&!": "A!B!&C!|",
        }
        for formula, expected in test_cases.items():
            result = negation_normal_form(formula)
            self.print_test("Conversion NNF", formula, expected, result)
            self.assertEqual(result, expected)

    def test_complex_nnf(self):
        test_cases = {
            "ABC&|D!": "A!B!|C!&D!",
            "AB&C!": "A!B!|C!",
            "A!B!C&|": "A!!B!C&|",
        }
        for formula, expected in test_cases.items():
            result = negation_normal_form(formula)
            self.print_test("Conversion NNF complexe", formula, expected,
                            result)
            self.assertEqual(result, expected)

    def test_invalid_nnf(self):
        invalid_cases = ["", "A!", "ABC|", "A>", "AB="]
        for formula in invalid_cases:
            with self.assertRaises(ValueError):
                negation_normal_form(formula)

    def test_implication_with_and(self):
        formula = "ABC&>"
        expected = "A!BC&|"
        result = negation_normal_form(formula)
        self.print_test(
            "Implication combinée avec AND", formula, expected, result
            )
        self.assertEqual(result, expected)

    def test_equivalence_with_or(self):
        formula = "AB|C="
        expected = "AB|C&A!B!|C!&|"
        result = negation_normal_form(formula)
        self.print_test(
            "Équivalence combinée avec OR", formula, expected, result
            )
        self.assertEqual(result, expected)

    def test_negation_equivalence(self):
        formula = "AB=!"
        expected = "AB!&A!B&|"
        result = negation_normal_form(formula)
        self.print_test(
            "Négation d'une équivalence", formula, expected, result
            )
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
