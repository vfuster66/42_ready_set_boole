from negation_normal_form import negation_normal_form
from printer import (
    print_title,
    print_info,
    print_success,
    print_error,
    print_separator,
)


def main():
    print_title("Test Negation Normal Form (NNF) Function")

    tests = [
        ("AB&!", "A!B!|"),          # ¬(A ∧ B) => ¬A ∨ ¬B
        ("AB|!", "A!B!&"),          # ¬(A ∨ B) => ¬A ∧ ¬B
        ("AB>", "A!B|"),            # A ⇒ B => ¬A ∨ B
        ("AB=", "AB&A!B!&|"),       # A ⇔ B => (A ∧ B) ∨ (¬A ∧ ¬B)
        ("AB|C&!", "A!B!&C!|"),
        # ¬((A ∨ B) ∧ C) => ¬(A ∨ B) ∨ ¬C => (¬A ∧ ¬B) ∨ ¬C
    ]

    try:
        for formula, expected in tests:
            print_info(f"Test : negation_normal_form('{formula}')")
            result = negation_normal_form(formula)

            if result == expected:
                print_success(f"Résultat: {result}")
            else:
                print_error(f"Erreur : attendu {expected}, obtenu {result}")

    except Exception as e:
        print_error(f"Exception levée : {e}")

    print_separator()


if __name__ == "__main__":
    main()
