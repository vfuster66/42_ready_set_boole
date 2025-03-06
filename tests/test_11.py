import unittest
from ex11.inverse_curve import reverse_map
from ex10.curve import map
import random
from colorama import Fore, Style


class TestInverseCurve(unittest.TestCase):
    def print_test(self, test_name, input_value, expected, obtained):
        """ Affichage amélioré du test avec Colorama """
        print(f"\n{Fore.CYAN}Test: {test_name}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Valeur en entrée :{Style.RESET_ALL} "
              f"{input_value}")
        print(f"{Fore.GREEN}Résultat attendu :{Style.RESET_ALL} {expected}")
        print(f"{Fore.BLUE}Résultat obtenu  :{Style.RESET_ALL} {obtained}")

        if expected == obtained:
            print(f"{Fore.GREEN}✅ Test OK !{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Test ÉCHOUÉ !{Style.RESET_ALL}")
        print("-" * 50)

    def test_basic_cases(self):
        test_cases = [
            (0.0, (0, 0)),
            (1.0, (2**16 - 1, 2**16 - 1)),
            (1/3, (2**16 - 1, 0)),
            (2/3, (0, 2**16 - 1)),
        ]
        for value, expected in test_cases:
            result = reverse_map(value)
            self.print_test("Cas basiques", value, expected, result)
            self.assertEqual(result, expected)

    def test_middle_values(self):
        test_cases = [
            (map(2**15, 2**15), (2**15, 2**15)),
            (map(2**15 - 1, 2**15), (2**15 - 1, 2**15)),
            (map(2**15, 2**15 - 1), (2**15, 2**15 - 1)),
        ]
        for value, expected in test_cases:
            result = reverse_map(value)
            self.print_test("Valeurs intermédiaires", value, expected, result)
            self.assertEqual(result, expected)

    def test_round_trip(self):
        """ Vérifie que reverse_map(map(x, y)) == (x, y) """
        for _ in range(10):
            x = random.randint(0, 2**16 - 1)
            y = random.randint(0, 2**16 - 1)
            mapped = map(x, y)
            result = reverse_map(mapped)
            self.print_test("Vérification bijective", mapped, (x, y), result)
            self.assertEqual(result, (x, y))

    def test_out_of_range(self):
        out_of_bounds_cases = [-0.1, 1.1, -1.0, 2.0]
        for value in out_of_bounds_cases:
            with self.assertRaises(ValueError):
                reverse_map(value)

    def test_bijectivity(self):
        """ Vérifie que reverse_map(map(x, y)) == (x, y) """
        for _ in range(10):
            x = random.randint(0, 65535)
            y = random.randint(0, 65535)
            n = map(x, y)
            result = reverse_map(n)
            self.print_test("Vérification bijective", n, (x, y), result)
            self.assertEqual(result, (x, y))


if __name__ == "__main__":
    unittest.main()
