import sys
import os
import subprocess
from colorama import init, Fore, Style


init(autoreset=True)

EXERCISE_DIR = "."
TEST_DIR = "tests"


def list_exercises():
    print(f"{Fore.BLUE}Available exercises:{Style.RESET_ALL}")
    for folder in sorted(os.listdir()):
        if folder.startswith("ex") and os.path.isdir(folder):
            print(f"{Fore.GREEN}- {folder}{Style.RESET_ALL}")


def run_exercise(ex_name):
    script_path = os.path.join(ex_name, f"{ex_name}.py")
    if os.path.exists(script_path):
        print(f"{Fore.YELLOW}Running {script_path}...{Style.RESET_ALL}\n")
        subprocess.run(["python", script_path])
    else:
        print(f"{Fore.RED}Error: {script_path} not found.{Style.RESET_ALL}")


def run_tests(ex_name):
    test_path = os.path.join(TEST_DIR, f"{ex_name}.py")
    if os.path.exists(test_path):
        print(f"{Fore.CYAN}Running tests in {test_path}...{Style.RESET_ALL}\n")
        subprocess.run(["python", test_path])
    else:
        print(f"{Fore.RED}Error: {test_path} not found.{Style.RESET_ALL}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Usage: python main.py <exercise_folder> "
              f"[--test]{Style.RESET_ALL}")
        list_exercises()
    else:
        exercise = sys.argv[1]
        if os.path.exists(exercise):
            run_exercise(exercise)
            if len(sys.argv) > 2 and sys.argv[2] == "--test":
                run_tests(exercise)
        else:
            print(f"{Fore.RED}Error: {exercise} not found.{Style.RESET_ALL}")
