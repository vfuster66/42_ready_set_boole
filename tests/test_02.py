import unittest
from ex02.gray_code import gray_code
from printer import print_test_result


class TestGrayCode(unittest.TestCase):

    def test_gray_code_values(self):
        cases = [
            (0, 0, "Gray code de 0"),
            (1, 1, "Gray code de 1"),
            (2, 3, "Gray code de 2"),
            (3, 2, "Gray code de 3"),
            (4, 6, "Gray code de 4"),
            (5, 7, "Gray code de 5"),
            (6, 5, "Gray code de 6"),
            (7, 4, "Gray code de 7"),
            (8, 12, "Gray code de 8")
        ]
        for n, expected, desc in cases:
            result = gray_code(n)
            print_test_result(desc, f"gray_code({n})", expected, result)
            self.assertEqual(result, expected)

    def test_negative_should_fail(self):
        with self.assertRaises(ValueError):
            gray_code(-1)

    def test_invalid_inputs(self):
        invalid_inputs = ["string", None, 5.5, [1, 2]]
        for invalid in invalid_inputs:
            with self.assertRaises(TypeError):
                gray_code(invalid)


if __name__ == "__main__":
    unittest.main()
