from sat import sat
from printer import (
    print_title,
    print_info,
    print_success,
    print_error,
    print_separator,
)


def main():
    print_title("Test SAT Solver Function")

    tests = [
        ("AB|", True),                    # A ∨ B : satisfiable
        ("AB&", True),                    # A ∧ B : satisfiable si A = B = True
        ("A!", True),                     # ¬A : satisfiable si A = False
        ("AB|C&", True),                  # (A ∨ B) ∧ C : satisfiable
        ("AB&C!&", True),  # ✅ valide : (A ∧ B) ∧ ¬C
        ("A A!&", False),                 # A ∧ ¬A : insatisfiable
        ("A A!|!", False),                # ¬(A ∨ ¬A) : insatisfiable
        ("A A!&B B!&|", False),           # (A ∧ ¬A) ∨ (B ∧ ¬B) : insatisfiable
    ]

    try:
        for formula, expected in tests:
            print_info(f"Test : sat('{formula}')")
            result = sat(formula)

            if result == expected:
                print_success(f"Résultat: {result}")
            else:
                print_error(f"Erreur : attendu {expected}, obtenu {result}")

            print_separator()

    except Exception as e:
        print_error(f"Exception levée : {e}")
        print_separator()


if __name__ == "__main__":
    main()
