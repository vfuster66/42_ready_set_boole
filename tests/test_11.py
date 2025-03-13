import unittest
from ex11.inverse_curve import reverse_map
from printer import print_test_result, print_title


class TestInverseCurveMapping(unittest.TestCase):

    def test_basic_cases(self):
        cases = [
            (0.0, (0, 0), "Reverse mapping 0.0 -> (0, 0)"),
            (0.25, (0, 1), "Reverse mapping 0.25 -> (0, 1)"),
            (0.5, (1, 0), "Reverse mapping 0.5 -> (1, 0)"),
            (0.75, (1, 1), "Reverse mapping 0.75 -> (1, 1)"),
            (0.8125, (2, 3), "Reverse mapping 0.8125 -> (2, 3)"),
        ]

        print_title("Tests Inverse Curve Mapping")

        for value, expected, desc in cases:
            result = reverse_map(value)

            print_test_result(
                desc,
                f"reverse_map({value})",
                expected,
                result
            )

            self.assertEqual(result, expected)

    def test_invalid_inputs(self):
        invalid_values = [
            -0.1,
            1.1,
            "string",
            None
        ]

        for value in invalid_values:
            with self.assertRaises((ValueError, TypeError)):
                reverse_map(value)


if __name__ == "__main__":
    unittest.main()
