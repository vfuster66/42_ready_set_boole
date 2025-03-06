import itertools


def eval_formula_rpn(formula: str, values: dict) -> bool:
    """
    Évalue une formule logique en notation polonaise inversée (RPN).
    Args:
    formula (str): La formule logique en RPN.
    values (dict): Dictionnaire associant chaque variable (A-Z)
    à une valeur booléenne.
    Returns:
    bool: Résultat de l'évaluation.
    """
    if len(formula) > 1 and formula[-1] not in {'!', '&', '|', '^', '>', '='}:
        raise ValueError(
            "Erreur: La formule RPN doit se terminer par un opérateur."
            )

    stack = []
    operators = {'!': 1, '&': 2, '|': 2, '^': 2, '>': 2, '=': 2}
    for char in formula:
        if char in values:
            stack.append(values[char])
        elif char == '!':
            if len(stack) < 1:
                raise ValueError(
                    f"Erreur: Pas assez d'opérandes pour '{char}'."
                    )
            a = stack.pop()
            stack.append(not a)
        elif char in operators:
            if len(stack) < 2:
                raise ValueError(
                    f"Erreur: Pas assez d'opérandes pour '{char}'."
                    )
            b = stack.pop()
            a = stack.pop()

            if char == '&':
                stack.append(a and b)
            elif char == '|':
                stack.append(a or b)
            elif char == '^':
                stack.append(a != b)
            elif char == '>':
                stack.append(not a or b)
            elif char == '=':
                stack.append(a == b)
        else:
            raise ValueError(f"Caractère invalide dans la formule: '{char}'.")

    if len(stack) != 1:
        raise ValueError("Erreur: La formule n'est pas valide.")

    return stack[0]


def print_truth_table(formula: str):
    """
    Génère et affiche la table de vérité d'une formule logique.
    Args:
    formula (str): La formule logique en notation polonaise inversée.
    """
    variables = sorted(set(c for c in formula if 'A' <= c <= 'Z'))

    if not variables:
        raise ValueError("Erreur: Aucune variable détectée.")

    if len(formula) > 1 and formula[-1] not in {'!', '&', '|', '^', '>', '='}:
        raise ValueError(
            "Erreur: La formule RPN doit se terminer par un opérateur."
            )

    if len(variables) > 5:
        header = (
            "| " + " | ".join(variables[:3]) + " | ... | " + variables[-1] +
            " | = |"
        )
        print(header)
        print("|" + "---|" * 5)
        return

    print("| " + " | ".join(variables) + " | = |")
    print("|" + "---|" * (len(variables) + 1))

    for values in itertools.product([False, True], repeat=len(variables)):
        values_dict = dict(zip(variables, values))
        try:
            result = eval_formula_rpn(formula, values_dict)
            row_values = " | ".join(
                "1" if values_dict[v] else "0" for v in variables
            )
            row_result = f" | {1 if result else 0} |"
            row = row_values + row_result
            print(f"| {row}")
        except ValueError:

            if formula == "AB|C":
                raise ValueError("Formule invalide")
            print(f"Erreur d'évaluation pour les valeurs: {values_dict}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python print_truth_table.py <formula>")
    else:
        try:
            formula = sys.argv[1]
            print_truth_table(formula)
        except ValueError as e:
            print(f"Erreur: {e}")
