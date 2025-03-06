import unittest
from ex08.powerset import powerset
from colorama import Fore, Style


class TestPowerset(unittest.TestCase):
    def print_test(self, test_name, formula, expected, obtained):
        """ Affichage amélioré du test avec couleurs et détails """
        print(f"\n{Fore.CYAN}Test: {test_name}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Formule :{Style.RESET_ALL} {formula}")
        print(f"{Fore.GREEN}Résultat attendu :{Style.RESET_ALL} {expected}")
        print(f"{Fore.BLUE}Résultat obtenu  :{Style.RESET_ALL} {obtained}")

        if sorted(expected) == sorted(obtained):
            print(f"{Fore.GREEN}✅ Test OK !{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Test ÉCHOUÉ !{Style.RESET_ALL}")
        print("-" * 50)

    def test_empty_set(self):
        input_set = []
        expected = [[]]
        result = powerset(input_set)
        self.print_test("Ensemble vide", input_set, expected, result)
        self.assertEqual(sorted(result), sorted(expected))

    def test_single_element_set(self):
        input_set = [1]
        expected = [[], [1]]
        result = powerset(input_set)
        self.print_test(
            "Ensemble avec un élément", input_set, expected, result
        )
        self.assertEqual(sorted(result), sorted(expected))

    def test_two_elements_set(self):
        input_set = [1, 2]
        expected = [[], [1], [2], [1, 2]]
        result = powerset(input_set)
        self.print_test(
            "Ensemble avec deux éléments", input_set, expected, result
        )
        self.assertEqual(sorted(result), sorted(expected))

    def test_three_elements_set(self):
        input_set = [1, 2, 3]
        expected = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
        result = powerset(input_set)
        self.print_test(
            "Ensemble avec trois éléments", input_set, expected, result
        )
        self.assertEqual(sorted(result), sorted(expected))

    def test_negative_numbers(self):
        input_set = [-1, 0, 1]
        expected = [[], [-1], [0], [1], [-1, 0], [-1, 1], [0, 1], [-1, 0, 1]]
        result = powerset(input_set)
        self.print_test(
            "Ensemble contenant des nombres négatifs",
            input_set,
            expected,
            result
        )
        self.assertEqual(sorted(result), sorted(expected))

    def test_large_set(self):
        input_set = [1, 2, 3, 4]
        expected_length = 2 ** len(input_set)
        result = powerset(input_set)
        self.print_test(
            "Ensemble plus grand (4 éléments)",
            input_set,
            f"{expected_length} sous-ensembles",
            f"{len(result)} sous-ensembles"
        )
        self.assertEqual(len(result), expected_length)

    def test_very_large_set(self):
        input_set = [1, 2, 3, 4, 5]
        expected_length = 2 ** len(input_set)
        result = powerset(input_set)
        self.print_test(
            "Grand ensemble (5 éléments)",
            input_set,
            f"{expected_length} sous-ensembles",
            f"{len(result)} sous-ensembles"
        )
        self.assertEqual(len(result), expected_length)


if __name__ == "__main__":
    unittest.main()
