from powerset import powerset
from printer import (
    print_title,
    print_info,
    print_success,
    print_error,
    print_separator,
)


def main():
    print_title("Test Power Set Function")

    tests = [
        ([], [[]]),
        ([1], [[], [1]]),
        ([1, 2], [[], [1], [2], [1, 2]]),
        ([1, 2, 3], [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]),
    ]

    try:
        for input_set, expected in tests:
            print_info(f"Test : powerset({input_set})")
            result = powerset(input_set)

            # Pour ignorer l'ordre dans les sous-ensembles :
            result_sorted = sorted([sorted(subset) for subset in result])
            expected_sorted = sorted([sorted(subset) for subset in expected])

            if result_sorted == expected_sorted:
                print_success(f"Résultat: {result_sorted}")
            else:
                print_error(
                    f"Erreur : attendu {expected_sorted}, "
                    f"obtenu {result_sorted}"
                )

            print_separator()

    except Exception as e:
        print_error(f"Exception levée : {e}")
        print_separator()


if __name__ == "__main__":
    main()
