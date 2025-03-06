import unittest
from ex03.eval_formula import eval_formula
from colorama import Fore, Style


class TestBooleanEvaluation(unittest.TestCase):
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

    def test_basic_operations(self):
        test_cases = {
            "10&": False,
            "10|": True,
            "11>": True,
            "10=": False,
            "1011||=": True,
        }
        for formula, expected in test_cases.items():
            result = eval_formula(formula)
            self.print_test("Évaluation RPN", formula, expected, result)
            self.assertEqual(result, expected)

    def test_complex_expressions(self):
        test_cases = {
            "10|1&": True,
            "101|&": True,
            "110|^": False,
            "110|>": True,
            "10&1>": True,
        }
        for formula, expected in test_cases.items():
            result = eval_formula(formula)
            self.print_test("Évaluation complexe", formula, expected, result)
            self.assertEqual(result, expected)

    def test_invalid_expressions(self):
        invalid_cases = ["", "10&|", "102", "x!1", "11&&", "1>1>"]
        for formula in invalid_cases:
            with self.assertRaises(ValueError):
                eval_formula(formula)

    def test_multiple_negations(self):
        formula = "1!!"
        expected = True
        result = eval_formula(formula)
        self.print_test("Négation double", formula, expected, result)
        self.assertEqual(result, expected)

    def test_long_expression(self):
        formula = "1101|&1>="
        expected = True
        result = eval_formula(formula)
        self.print_test("Expression longue", formula, expected, result)
        self.assertEqual(result, expected)

    def test_only_operands(self):
        formula = "1100"
        with self.assertRaises(ValueError):
            eval_formula(formula)


if __name__ == "__main__":
    unittest.main(verbosity=1)
