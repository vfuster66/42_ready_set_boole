import unittest
from ex04.print_truth_table import print_truth_table
from printer import print_test_result, print_title, print_info


class TestPrintTruthTable(unittest.TestCase):

    def test_simple_formula(self):
        formula = "AB&C|"
        print_title("Test table de vérité pour : (A ∧ B) ∨ C")
        print_info(f"Formule RPN : {formula}")

        try:
            print_truth_table(formula)
            print_test_result(
                "Affichage de la table",
                f"print_truth_table('{formula}')",
                "Table affichée",
                "OK"
            )
        except Exception as e:
            self.fail(f"Erreur levée : {e}")

    def test_invalid_formula(self):
        invalid_formulas = [
            "",          # Vide
            "A!",        # Trop peu d'opérandes
            "AB&C|!",
        ]

        for formula in invalid_formulas:
            with self.assertRaises(ValueError):
                print_truth_table(formula)


if __name__ == "__main__":
    unittest.main()
