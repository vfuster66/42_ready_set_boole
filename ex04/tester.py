from print_truth_table import print_truth_table
from printer import print_title, print_info, print_separator


def main():
    print_title("Test Print Truth Table Function")

    examples = [
        ("AB&C|", "(A ∧ B) ∨ C"),  # Exemple classique
        ("ABC&&", "A ∧ B ∧ C"),    # 3 variables ET
        ("AB|C&", "(A ∨ B) ∧ C")   # OU puis ET
    ]

    try:
        for formula, desc in examples:
            print_info(f"Formule : {desc} (RPN: {formula})")
            print_truth_table(formula)
            print_separator()

    except Exception as e:
        from printer import print_error
        print_error(f"Erreur : {e}")


if __name__ == "__main__":
    main()
