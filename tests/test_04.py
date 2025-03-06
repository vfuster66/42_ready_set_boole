import unittest
from ex04.print_truth_table import print_truth_table
from colorama import Fore, Style
from io import StringIO
import sys


class TestTruthTable(unittest.TestCase):
    def print_test(self, test_name, formula, expected_output):
        """ Affichage amélioré du test avec couleurs et détails """
        print(f"\n{Fore.CYAN}Test: {test_name}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Formule :{Style.RESET_ALL} {formula}")

        captured_output = StringIO()
        sys.stdout = captured_output
        print_truth_table(formula)
        sys.stdout = sys.__stdout__

        obtained_output = captured_output.getvalue().strip()
        print(f"{Fore.GREEN}Sortie attendue :{Style.RESET_ALL}\n"
              f"{expected_output}")
        print(f"{Fore.BLUE}Sortie obtenue  :{Style.RESET_ALL}\n"
              f"{obtained_output}")

        if expected_output in obtained_output:
            print(f"{Fore.GREEN}✅ Test OK !{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Test ÉCHOUÉ !{Style.RESET_ALL}")
        print("-" * 50)

        self.assertIn(expected_output, obtained_output)

    def test_basic_truth_table(self):
        formula = "AB&C|"
        expected_output = "| A | B | C | = |\n|---|---|---|---|"
        self.print_test(
            "Table de vérité de (A ∧ B) ∨ C", formula, expected_output
            )

    def test_single_variable(self):
        formula = "A!"
        expected_output = "| A | = |\n|---|---|\n| 0 | 1 |\n| 1 | 0 |"
        self.print_test(
            "Table de vérité pour la négation (¬A)", formula, expected_output
            )

    def test_invalid_formula(self):
        formula = "AB|C"
        with self.assertRaises(ValueError):
            print_truth_table(formula)

    def test_all_variables(self):
        formula = "AB&CD|EF^GH&|IJ>KLM&NO|PQ^RS&TU|VW&XY|Z="
        expected_output = "| A | B | C | ... | Z | = |"
        self.print_test(
            "Table de vérité avec 26 variables", formula, expected_output
            )

    def test_single_variable_truth_table(self):
        formula = "A"
        expected_output = "| A | = |\n|---|---|\n| 0 | 0 |\n| 1 | 1 |"
        self.print_test(
            "Table de vérité d'une variable seule", formula, expected_output
            )

    def test_only_operators(self):
        formula = "&|^"
        with self.assertRaises(ValueError):
            print_truth_table(formula)

    def test_double_negation(self):
        formula = "A!!"
        expected_output = "| A | = |\n|---|---|\n| 0 | 0 |\n| 1 | 1 |"
        self.print_test(
            "Table de vérité avec double négation (¬¬A = A)",
            formula, expected_output
            )


if __name__ == "__main__":
    unittest.main(verbosity=1)
