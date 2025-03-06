import unittest
from ex06.conjunctive_normal_form import conjunctive_normal_form
from colorama import Fore, Style


class TestCNFConversionExtended(unittest.TestCase):
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

    def test_complex_cnf_cases(self):

        test_cases = {
            "ABC&|": "AB|AC|&",

            "AB&C|": "AC|BC|&",

            "ABCD&&|": "AB|AC|AD|&&",

            "ABC&&D|": "AD|BD|CD|&&",

            "AB|CD|&": "AB|CD|&",

            "ABC&DE&||": "AB|AC|DB|DC|&&&&"
        }

        for formula, expected in test_cases.items():
            result = conjunctive_normal_form(formula)
            self.print_test("CNF complexe", formula, expected, result)
            self.assertEqual(result, expected)

    def test_mixed_operations(self):
        test_cases = {
            "A!BC&|": "A!B|A!C|&",

            "A!B!&C|": "A!C|B!C|&"
        }

        for formula, expected in test_cases.items():
            result = conjunctive_normal_form(formula)
            self.print_test("Opérations mixtes", formula, expected, result)
            self.assertEqual(result, expected)

    def test_transformations(self):
        formulas = [
            ("ABC&|", "AB|AC|&"),
            ("AB>!", "AB!&")
        ]

        for original, expected_cnf in formulas:
            cnf = conjunctive_normal_form(original)

            self.print_test("Transformation en CNF", original,
                            expected_cnf, cnf)
            self.assertEqual(cnf, expected_cnf)

    def test_complex_disjunction(self):
        formula = "AB&C|D|"
        expected = "AB|D|C|"
        result = conjunctive_normal_form(formula)
        self.print_test("Disjonction complexe avec AND", formula, expected,
                        result)
        self.assertEqual(result, expected)

    def test_nested_conjunction(self):
        formula = "AB&C&"
        expected = "AB&C&"
        result = conjunctive_normal_form(formula)
        self.print_test("Conjonction imbriquée", formula, expected, result)
        self.assertEqual(result, expected)

    def test_double_negation_conjunction(self):
        formula = "AB&!!"
        expected = "AB&"
        result = conjunctive_normal_form(formula)
        self.print_test("Double négation sur une conjonction", formula,
                        expected, result)
        self.assertEqual(result, expected)

    def test_distribution_with_implication(self):
        formula = "AB>C&"
        expected = "A!B|C&"
        result = conjunctive_normal_form(formula)
        self.print_test("Distribution avec implication", formula,
                        expected, result)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
