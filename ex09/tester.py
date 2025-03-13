from ex09.set_evaluation import eval_set
from printer import (
    print_title,
    print_info,
    print_success,
    print_error,
    print_separator,
)


def main():
    print_title("Test Set Evaluation Function")

    tests = [
        ("AB&", [[1, 2], [2, 3]]),               # Intersection => [2]
        ("AB|", [[1, 2], [2, 3]]),               # Union => [1, 2, 3]
        ("A!", [[1, 2, 3, 4]]),
        ("ABC&|", [[1, 2], [2, 3], [3, 4]]),     # (A ∨ (B ∧ C)) => A ∪ (B ∩ C)
    ]

    try:
        for formula, sets in tests:
            print_info(f"Test : eval_set('{formula}', {sets})")
            result = eval_set(formula, sets)
            print_success(f"Résultat: {sorted(result)}")
            print_separator()

    except Exception as e:
        print_error(f"Exception levée : {e}")
        print_separator()


if __name__ == "__main__":
    main()
