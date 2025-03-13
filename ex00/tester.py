from adder import adder
from printer import (
    print_title,
    print_success,
    print_info,
    print_error,
    print_separator
)


def main():
    print_title("Test Adder Function")

    try:
        print_info("Test 1 : adder(2, 3)")
        result = adder(2, 3)
        print_success(f"Résultat: {result}")

        print_info("Test 2 : adder(7, 8)")
        result = adder(7, 8)
        print_success(f"Résultat: {result}")

        print_info("Test 3 : adder(1000000, 1000000)")
        result = adder(1000000, 1000000)
        print_success(f"Résultat: {result}")

    except Exception as e:
        print_error(f"Erreur : {e}")

    print_separator()


if __name__ == "__main__":
    main()
