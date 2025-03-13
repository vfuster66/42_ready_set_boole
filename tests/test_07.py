import unittest
from ex07.sat import sat
from printer import print_test_result, print_title


class TestSatSolver(unittest.TestCase):

    def test_satisfiable_cases(self):
        cases = [
            ("A", True, "A est satisfiable"),
            ("A!", True, "¬A est satisfiable"),
            ("AB|", True, "A ∨ B est satisfiable"),
            ("AB&C|", True, "(A ∧ B) ∨ C est satisfiable"),
        ]

        print_title("Tests SAT : Formules satisfaisables")

        for formula, expected, desc in cases:
            result = sat(formula)
            print_test_result(desc, f"sat('{formula}')", expected, result)
            self.assertEqual(result, expected)

    def test_unsatisfiable_cases(self):
        cases = [
            ("A A!&", False, "A ∧ ¬A : insatisfiable"),
            ("A A!|!", False, "¬(A ∨ ¬A) : insatisfiable"),
            ("A A!&B B!&|", False, "(A ∧ ¬A) ∨ (B ∧ ¬B) : insatisfiable"),
        ]

        print_title("Tests SAT : Formules insatisfaisables")

        for formula, expected, desc in cases:
            result = sat(formula)
            print_test_result(desc, f"sat('{formula}')", expected, result)
            self.assertEqual(result, expected)

    def test_invalid_formulas(self):
        invalid_formulas = [
            "",        # Vide
            "A>",      # Pas assez d'opérandes
            "AB|>",    # Pas assez d'opérandes après opérateur
            "A#",      # Caractère non valide
        ]

        for formula in invalid_formulas:
            with self.assertRaises(ValueError):
                sat(formula)


if __name__ == "__main__":
    unittest.main()
