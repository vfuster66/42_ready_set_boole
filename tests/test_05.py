import unittest
from ex05.negation_normal_form import negation_normal_form
from printer import print_test_result, print_title


class TestNegationNormalForm(unittest.TestCase):

    def test_basic_cases(self):
        cases = [
            ("AB&!", "A!B!|", "¬(A ∧ B) => ¬A ∨ ¬B"),
            ("AB|!", "A!B!&", "¬(A ∨ B) => ¬A ∧ ¬B"),
            ("AB>", "A!B|", "A ⇒ B => ¬A ∨ B"),
            ("AB=", "AB&A!B!&|", "A ⇔ B => (A ∧ B) ∨ (¬A ∧ ¬B)"),
            ("AB|C&!", "A!B!&C!|", "¬((A ∨ B) ∧ C) => (¬A ∧ ¬B) ∨ ¬C")
        ]

        print_title("Tests sur la Négation en Forme Normale (NNF)")

        for formula, expected, desc in cases:
            result = negation_normal_form(formula)
            print_test_result(
                desc, f"negation_normal_form('{formula}')", expected, result
            )
            self.assertEqual(result, expected)

    def test_invalid_formulas(self):
        invalid_formulas = [
            "",            # Vide
            "A>",          # Pas assez d'opérandes
            "AB|>",        # Pas assez d'opérandes après opérateur
            "A#",          # Caractère invalide
        ]

        for formula in invalid_formulas:
            with self.assertRaises(ValueError):
                negation_normal_form(formula)


if __name__ == "__main__":
    unittest.main()
