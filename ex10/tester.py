from curve import map
from printer import (
    print_title,
    print_info,
    print_success,
    print_error,
    print_separator,
)


def main():
    print_title("Test Curve Mapping Function")

    tests = [
        ((0, 0), 0.0),
        ((0, 1), 0.25),
        ((1, 0), 0.5),
        ((1, 1), 0.75),
        ((2, 3), 0.8125),
    ]

    try:
        for (x, y), expected in tests:
            print_info(f"Test : map({x}, {y})")
            result = map(x, y)

            if abs(result - expected) < 1e-6:
                print_success(f"Résultat: {result}")
            else:
                print_error(f"Erreur : attendu {expected}, obtenu {result}")

            print_separator()

    except Exception as e:
        print_error(f"Exception levée : {e}")
        print_separator()


if __name__ == "__main__":
    main()
