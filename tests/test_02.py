import unittest
from ex02.gray_code import gray_code
from colorama import Fore, Style


class TestGrayCode(unittest.TestCase):
    def print_test(self, test_name, input_value, expected, obtained):
        """ Affichage amélioré du test avec couleurs et détails """
        print(f"\n{Fore.CYAN}Test: {test_name}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Entrée :{Style.RESET_ALL} {input_value}")
        print(f"{Fore.GREEN}Résultat attendu :{Style.RESET_ALL} {expected}")
        print(f"{Fore.BLUE}Résultat obtenu  :{Style.RESET_ALL} {obtained}")

        if expected == obtained:
            print(f"{Fore.GREEN}✅ Test OK !{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Test ÉCHOUÉ !{Style.RESET_ALL}")
        print("-" * 50)

    def test_basic_gray_code(self):
        test_cases = {
            0: 0,
            1: 1,
            2: 3,
            3: 2,
            4: 6,
            5: 7,
            6: 5,
            7: 4,
            8: 12,
        }
        for n, expected in test_cases.items():
            result = gray_code(n)
            self.print_test("Conversion en code de Gray", n, expected, result)
            self.assertEqual(result, expected)

    def test_large_numbers(self):
        a = 1000000
        expected = a ^ (a >> 1)
        result = gray_code(a)
        self.print_test("Grand nombre en code de Gray", a, expected, result)
        self.assertEqual(result, expected)

    def test_negatives_should_fail(self):
        a = -5
        with self.assertRaises(ValueError):
            gray_code(a)

    def test_invalid_inputs(self):
        invalid_inputs = ["10", None, "abc"]
        for a in invalid_inputs:
            with self.assertRaises(TypeError):
                gray_code(a)

    def test_large_number_gray_code(self):
        a = 1024
        expected = a ^ (a >> 1)
        result = gray_code(a)
        self.print_test(
            "Code de Gray pour un grand nombre (2^10)", a, expected, result
        )
        self.assertEqual(result, expected)

    def test_odd_number_gray_code(self):
        a = 37 
        expected = a ^ (a >> 1)
        result = gray_code(a)
        self.print_test(
            "Code de Gray pour un nombre impair", a, expected, result
        )
        self.assertEqual(result, expected)

    def test_gray_code_sequence(self):
        for n in range(20):
            expected = n ^ (n >> 1)
            result = gray_code(n)
            self.print_test("Séquence de codes de Gray", n, expected, result)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
