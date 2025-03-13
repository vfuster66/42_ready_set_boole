from conjunctive_normal_form import conjunctive_normal_form
from printer import (
    print_title,
    print_info,
    print_success,
    print_error,
    print_separator,
)


def main():
    print_title("Test Conjunctive Normal Form (CNF) Function")

    tests = [
        ("AB&!", "A!B!|"),                       # ¬(A ∧ B) => ¬A ∨ ¬B
        ("AB|!", "A!B!&"),                       # ¬(A ∨ B) => ¬A ∧ ¬B
        ("AB>", "A!B|"),                         # A ⇒ B => ¬A ∨ B
        ("AB=", "AA!|AB!|&BA!|BB!|&&"),          # A ⇔ B => distribué complet
        ("ABC&|", "AB|AC|&"),
        # A ∨ (B ∧ C) => (A ∨ B) ∧ (A ∨ C)
        ("AB&C|D&", "AC|BC|&D&"),
        # A ∧ (B ∨ C) ∧ D => distribué complet
    ]

    try:
        for formula, expected in tests:
            print_info(f"Test : conjunctive_normal_form('{formula}')")
            result = conjunctive_normal_form(formula)

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
