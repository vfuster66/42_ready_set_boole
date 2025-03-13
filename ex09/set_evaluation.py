def eval_set(formula: str, sets: list[set[int]]) -> set[int]:
    """
    Évalue une formule en notation polonaise inversée (RPN)
    avec des ensembles donnés.

    Args:
        formula (str): La formule logique en RPN.
        sets (list[set[int]]): Liste des ensembles associés aux variables A, B,
        etc.

    Returns:
        set[int]: L'ensemble résultant de l'évaluation.
    """
    variables = sorted(set(c for c in formula if 'A' <= c <= 'Z'))

    if len(variables) != len(sets):
        raise ValueError("Erreur: Nombre d'ensembles fourni incorrect.")

    values = dict(zip(variables, [set(s) for s in sets]))

    universe = set().union(*values.values())

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
