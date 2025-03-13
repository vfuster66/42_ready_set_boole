from inverse_curve import reverse_map
from printer import (
    print_title,
    print_info,
    print_success,
    print_error,
    print_separator,
)


def main():
    print_title("Test Inverse Curve Mapping Function")

    tests = [
        (0.0, (0, 0)),
        (0.25, (0, 1)),
        (0.5, (1, 0)),
        (0.75, (1, 1)),
        (0.8125, (2, 3)),
    ]

    try:
        for value, expected in tests:
            print_info(f"Test : reverse_map({value})")
            result = reverse_map(value)

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
