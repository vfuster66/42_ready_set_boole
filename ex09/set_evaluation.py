import sys
import ast


def set_evaluation(formula: str, sets: list[set[int]]) -> set[int]:
    """
    Évalue une formule en notation polonaise inversée (RPN)
    avec des ensembles donnés.

    Args:
        formula (str): La formule logique en RPN.
        sets (list[set[int]]):
        Liste des ensembles associés aux variables A, B, ...

    Returns:
        set[int]: L'ensemble résultant de l'évaluation.
    """

    variables = sorted(set(c for c in formula if 'A' <= c <= 'Z'))
    if len(variables) != len(sets):
        raise ValueError("Erreur: Nombre d'ensembles fourni incorrect.")

    values = dict(zip(variables, sets))

    universe = set().union(*sets)

    stack = []
    for char in formula:
        if char in values:
            stack.append(values[char])
        elif char in "&|^>=":
            if len(stack) < 2:
                raise ValueError(
                    f"Formule invalide: pas assez d'opérandes pour '{char}'."
                )
            b = stack.pop()
            a = stack.pop()
            if char == '&':
                result = a & b
            elif char == '|':
                result = a | b
            elif char == '^':
                result = a ^ b
            elif char == '>':
                result = (universe - a) | b
            elif char == '=':
                result = ((universe - a) | b) & ((universe - b) | a)
            stack.append(result)
        elif char == '!':
            if not stack:
                raise ValueError(
                    "Formule invalide: pas assez d'opérandes pour '!'."
                )
            a = stack.pop()
            stack.append(universe - a)
        else:
            raise ValueError(f"Caractère invalide dans la formule: '{char}'.")

    if len(stack) != 1:
        raise ValueError("Formule invalide: trop d'opérandes.")

    return stack[0]


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python set_evaluation.py \"FORMULE\" \"[{1,2}, {3,4}]\"")
    else:
        try:
            formula = sys.argv[1]
            sets_input = ast.literal_eval(sys.argv[2])
            if not isinstance(sets_input, list) or not all(
                isinstance(s, set) for s in sets_input
            ):
                raise ValueError
            universe = set().union(*sets_input)
            print(set_evaluation(formula, sets_input))
        except (ValueError, SyntaxError):
            print("Erreur: Veuillez entrer une formule valide et une liste "
                  "d'ensembles.")
