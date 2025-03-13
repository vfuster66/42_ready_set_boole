import unittest
from ex09.set_evaluation import eval_set
from printer import print_test_result, print_title


class TestSetEvaluation(unittest.TestCase):

    def test_valid_cases(self):
        cases = [
            ("AB&", [[1, 2], [2, 3]], [2], "Intersection A ∩ B"),
            ("AB|", [[1, 2], [2, 3]], [1, 2, 3], "Union A ∪ B"),
            ("ABC&|", [[1, 2], [2, 3], [3, 4]], [1, 2, 3], "A ∪ (B ∩ C)"),
        ]

        print_title("Tests Set Evaluation")

        for formula, sets, expected, desc in cases:
            result = eval_set(formula, sets)
            # Comparaison triée
            print_test_result(
                desc,
                f"eval_set('{formula}', {sets})",
                sorted(expected),
                sorted(result)
            )
            self.assertEqual(sorted(result), sorted(expected))

    def test_invalid_inputs(self):
        invalid_cases = [
            ("", [[1, 2]]),              # Formule vide
            ("A&", [[1, 2]]),
            ("AB#&", [[1, 2], [3, 4]]),  # Caractère invalide dans la formule
        ]

        for formula, sets in invalid_cases:
            with self.assertRaises(ValueError):
                eval_set(formula, sets)


if __name__ == "__main__":
    unittest.main()
