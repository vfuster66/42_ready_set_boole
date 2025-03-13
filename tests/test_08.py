import unittest
from ex08.powerset import powerset
from printer import print_test_result, print_title


class TestPowerSet(unittest.TestCase):

    def test_basic_cases(self):
        cases = [
            ([], [[]], "Power set of empty set"),
            ([1], [[], [1]], "Power set of single element"),
            ([1, 2], [[], [1], [2], [1, 2]], "Power set of two elements"),
            (
                [1, 2, 3],
                [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]],
                "Power set of three elements",
            ),
        ]

        print_title("Tests Power Set")

        for input_set, expected, desc in cases:
            result = powerset(input_set)

            # On trie pour ignorer l'ordre des sous-ensembles
            result_sorted = sorted([sorted(subset) for subset in result])
            expected_sorted = sorted([sorted(subset) for subset in expected])

            print_test_result(
                desc, f"powerset({input_set})", expected_sorted, result_sorted
            )

            self.assertEqual(result_sorted, expected_sorted)

    def test_invalid_inputs(self):
        invalid_inputs = [
            None,
            "123",
            123,
        ]

        for invalid in invalid_inputs:
            with self.assertRaises(TypeError):
                powerset(invalid)


if __name__ == "__main__":
    unittest.main()
