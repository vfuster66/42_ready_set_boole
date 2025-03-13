from colorama import Fore, Style, init

init(autoreset=True)


def print_title(title: str):
    print(f"{Fore.CYAN}{Style.BRIGHT}\n=== {title} ==={Style.RESET_ALL}")


def print_success(message: str):
    print(f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} {message}")


def print_info(message: str):
    print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} {message}")


def print_warning(message: str):
    print(f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL} {message}")


def print_error(message: str):
    print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} {message}")


def print_separator():
    print(f"{Fore.MAGENTA}{'-' * 50}{Style.RESET_ALL}")


def print_test_result(test_name, operation, expected, obtained):
    """ Affichage amélioré d'un test unitaire avec couleurs et détails """
    print_title(test_name)
    print_info(f"Opération : {operation}")
    print(f"{Fore.GREEN}Résultat attendu :{Style.RESET_ALL} {expected}")
    print(f"{Fore.BLUE}Résultat obtenu  :{Style.RESET_ALL} {obtained}")

    if expected == obtained:
        print_success("✅ Test OK !")
    else:
        print_error("❌ Test ÉCHOUÉ !")

    print_separator()
