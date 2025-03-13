import unittest
from ex10.curve import map
from printer import print_test_result, print_title


class TestCurveMapping(unittest.TestCase):

    def test_basic_cases(self):
        cases = [
            ((0, 0), 0.0, "Mapping (0, 0)"),
            ((0, 1), 0.25, "Mapping (0, 1)"),
            ((1, 0), 0.5, "Mapping (1, 0)"),
            ((1, 1), 0.75, "Mapping (1, 1)"),
            ((2, 3), 0.8125, "Mapping (2, 3)"),  # basé sur bits interleavés
        ]

        print_title("Tests Curve Mapping")

        for (x, y), expected, desc in cases:
            result = map(x, y)

            print_test_result(
                desc,
                f"map({x}, {y})",
                expected,
                result
            )

            self.assertAlmostEqual(result, expected, places=6)

    def test_invalid_inputs(self):
        invalid_inputs = [
            ("a", 1),
            (1, None),
            ([], {}),
        ]

        for x, y in invalid_inputs:
            with self.assertRaises(TypeError):
                map(x, y)


if __name__ == "__main__":
    unittest.main()
