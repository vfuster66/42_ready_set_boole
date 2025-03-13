from eval_formula import eval_formula
from printer import (
    print_title,
    print_info,
    print_success,
    print_error,
    print_separator
)


def main():
    print_title("Test Eval Formula Function")

    tests = [
        ("10&", False),          # 1 ∧ 0
        ("10|", True),           # 1 ∨ 0
        ("11>", True),           # 1 ⇒ 1
        ("10=", False),          # 1 ⇔ 0
        ("1011||=", True),       # ((1 ∨ 0) ∨ 1) ⇔ 1
        ("1!", False),           # ¬1
        ("10&1|", True),         # (1 ∧ 0) ∨ 1
    ]

    try:
        for formula, expected in tests:
            print_info(f"Test : eval_formula('{formula}')")
            result = eval_formula(formula)
            if result == expected:
                print_success(f"Résultat: {result}")
            else:
                print_error(f"Erreur : attendu {expected}, obtenu {result}")

    except Exception as e:
        print_error(f"Exception levée : {e}")

    print_separator()


if __name__ == "__main__":
    main()
