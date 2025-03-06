from itertools import chain, combinations
import sys
import ast


def powerset(input_set):
    """
    Génère l'ensemble des parties (powerset) d'un ensemble donné.

    Args:
        input_set (list[int]): Un ensemble d'entiers.

    Returns:
        list[list[int]]: L'ensemble des parties de l'ensemble donné.
    """
    return [list(subset) for subset in chain.from_iterable(
        combinations(input_set, r) for r in range(len(input_set) + 1)
    )]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python powerset.py \"[1, 2, 3]\"")
    else:
        try:
            input_set = ast.literal_eval(sys.argv[1])
            if not isinstance(input_set, list) or not all(
                    isinstance(i, int) for i in input_set):
                raise ValueError
            print(powerset(input_set))
        except (ValueError, SyntaxError):
            print("Erreur: Veuillez entrer une liste valide d'entiers.")
