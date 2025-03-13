import unittest
from ex03.eval_formula import eval_formula
from printer import print_test_result


class TestEvalFormula(unittest.TestCase):
    def test_valid_formulas(self):
        cases = [
            ("10&", False, "1 ∧ 0"),
            ("10|", True, "1 ∨ 0"),
            ("11>", True, "1 ⇒ 1"),
            ("10=", False, "1 ⇔ 0"),
            ("1011||=", True, "((1 ∨ 0) ∨ 1) ⇔ 1"),
            ("1!", False, "¬1"),
            ("10&1|", True, "(1 ∧ 0) ∨ 1"),
        ]
        for formula, expected, desc in cases:
            result = eval_formula(formula)
            print_test_result(
                f"Évaluation : {desc}",
                f"eval_formula('{formula}')",
                expected,
                result
            )
            self.assertEqual(result, expected)

    def test_empty_formula(self):
        with self.assertRaises(ValueError):
            eval_formula("")

    def test_operator_without_operand(self):
        with self.assertRaises(ValueError):
            eval_formula("!")

    def test_invalid_operands_after_not(self):
        with self.assertRaises(ValueError):
            eval_formula("10&!")

    def test_insufficient_operands(self):
        with self.assertRaises(ValueError):
            eval_formula("10&|")

    def test_invalid_characters(self):
        with self.assertRaises(ValueError):
            eval_formula("AB&")


if __name__ == "__main__":
    unittest.main()
