from gray_code import gray_code
from printer import (
    print_title, 
    print_info, 
    print_success, 
    print_error, 
    print_separator
)


def main():
    print_title("Test Gray Code Function")

    tests = [
        (0, 0),
        (1, 1),
        (2, 3),
        (3, 2),
        (4, 6),
        (5, 7),
        (6, 5),
        (7, 4),
        (8, 12)
    ]

    try:
        for n, expected in tests:
            print_info(f"Test : gray_code({n})")
            result = gray_code(n)
            if result == expected:
                print_success(f"Résultat: {result}")
            else:
                print_error(f"Erreur : attendu {expected}, obtenu {result}")

    except Exception as e:
        print_error(f"Exception levée : {e}")

    print_separator()


if __name__ == "__main__":
    main()
