from multiplier import multiplier
from printer import (
    print_title,
    print_info,
    print_success,
    print_separator,
    print_error
)


def main():
    print_title("Test Multiplier Function")

    try:
        print_info("Test 1 : multiplier(2, 3)")
        result = multiplier(2, 3)
        print_success(f"Résultat: {result}")

        print_info("Test 2 : multiplier(0, 5)")
        result = multiplier(0, 5)
        print_success(f"Résultat: {result}")

        print_info("Test 3 : multiplier(7, 8)")
        result = multiplier(7, 8)
        print_success(f"Résultat: {result}")

        print_info("Test 4 : multiplier(1000, 1000)")
        result = multiplier(1000, 1000)
        print_success(f"Résultat: {result}")

    except Exception as e:
        print_error(f"Erreur : {e}")

    print_separator()


if __name__ == "__main__":
    main()
