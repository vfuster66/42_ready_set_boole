import unittest
from ex10.curve import map
import random
from colorama import Fore, Style


class TestCurveMapping(unittest.TestCase):
    def print_test(self, test_name, x, y, expected, obtained):
        """ Affichage amélioré du test avec Colorama """
        print(f"\n{Fore.CYAN}Test: {test_name}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Coordonnées :{Style.RESET_ALL} (x={x}, y={y})")
        print(f"{Fore.GREEN}Résultat attendu :{Style.RESET_ALL} "
              f"{expected:.10f}")
        print(f"{Fore.BLUE}Résultat obtenu  :{Style.RESET_ALL} "
              f"{obtained:.10f}")

        if abs(expected - obtained) < 1e-6:
            print(f"{Fore.GREEN}✅ Test OK !{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Test ÉCHOUÉ !{Style.RESET_ALL}")
        print("-" * 50)

    def test_basic_cases(self):
        test_cases = [
            (0, 0, 0.0),
            (2**16 - 1, 2**16 - 1, 1.0),
            (0, 2**16 - 1, 2/3),
            (2**16 - 1, 0, 1/3),
            (100, 200, map(100, 200)),
        ]
        for x, y, expected in test_cases:
            result = map(x, y)
            self.print_test("Cas basiques", x, y, expected, result)
            self.assertAlmostEqual(result, expected, places=6)

    def test_middle_values(self):
        test_cases = [
            (2**15, 2**15, map(2**15, 2**15)),
            (2**15 - 1, 2**15, map(2**15 - 1, 2**15)),
            (2**15, 2**15 - 1, map(2**15, 2**15 - 1)),
        ]
        for x, y, expected in test_cases:
            result = map(x, y)
            self.print_test("Valeurs intermédiaires", x, y, expected, result)
            self.assertAlmostEqual(result, expected, places=6)

    def test_out_of_range(self):
        out_of_bounds_cases = [
            (-1, 0), (0, -1), (2**16, 0), (0, 2**16), (2**16, 2**16)
        ]
        for x, y in out_of_bounds_cases:
            with self.assertRaises(ValueError):
                map(x, y)

    def test_edge_cases(self):
        test_cases = [
            (1, 0, map(1, 0)),
            (0, 1, map(0, 1)),
            (2**16 - 1, 1, map(2**16 - 1, 1)),
            (1, 2**16 - 1, map(1, 2**16 - 1)),
        ]
        for x, y, expected in test_cases:
            result = map(x, y)
            self.print_test("Cas aux limites", x, y, expected, result)
            self.assertAlmostEqual(result, expected, places=6)

    def test_random_cases(self):
        for _ in range(10):
            x = random.randint(0, 2**16 - 1)
            y = random.randint(0, 2**16 - 1)
            expected = map(x, y)
            result = map(x, y)
            self.print_test("Cas aléatoires", x, y, expected, result)
            self.assertAlmostEqual(result, expected, places=6)


if __name__ == "__main__":
    unittest.main()
