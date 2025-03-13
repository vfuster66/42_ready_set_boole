import unittest
from ex06.conjunctive_normal_form import conjunctive_normal_form
from printer import print_test_result, print_title


class TestConjunctiveNormalForm(unittest.TestCase):

    def test_basic_cases(self):
        cases = [
            ("AB&!", "A!B!|", "¬(A ∧ B) => ¬A ∨ ¬B"),
            ("AB|!", "A!B!&", "¬(A ∨ B) => ¬A ∧ ¬B"),
            ("AB>", "A!B|", "A ⇒ B => ¬A ∨ B"),
            (
                "AB=",
                "AA!|AB!|&BA!|BB!|&&",
                "A ⇔ B => (A ∧ B) ∨ (¬A ∧ ¬B) (distribué)"
            ),
            ("ABC&|", "AB|AC|&", "A ∨ (B ∧ C) => (A ∨ B) ∧ (A ∨ C)"),
            ("AB&C|D&", "AC|BC|&D&", "A ∧ (B ∨ C) ∧ D => distribué"),
        ]

        print_title("Tests sur la Forme Normale Conjonctive (CNF)")

        for formula, expected, desc in cases:
            result = conjunctive_normal_form(formula)
            print_test_result(
                desc, f"conjunctive_normal_form('{formula}')", expected, result
            )
            self.assertEqual(result, expected)

    def test_invalid_formulas(self):
        invalid_formulas = [
            "",          # Vide
            "A>",        # Pas assez d'opérandes
            "AB|>",      # Pas assez d'opérandes après opérateur
            "A#",        # Caractère invalide
        ]

        for formula in invalid_formulas:
            with self.assertRaises(ValueError):
                conjunctive_normal_form(formula)


if __name__ == "__main__":
    unittest.main()
