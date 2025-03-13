def eval_formula(formula: str, values: dict) -> bool:
    """Évalue une formule booléenne en RPN
    avec un dictionnaire d'assignations."""
    stack = []
    operators = {"!", "&", "|", "^", ">", "="}

    for char in formula:
        if char in values:
            stack.append(values[char])
        elif char == "0":
            stack.append(False)
        elif char == "1":
            stack.append(True)
        elif char in operators:
            if char == "!":
                if len(stack) < 1:
                    raise ValueError(f"Pas assez d'opérandes pour '{char}'")
                operand = stack.pop()
                stack.append(not operand)
            else:
                if len(stack) < 2:
                    raise ValueError(f"Pas assez d'opérandes pour '{char}'")
                right = stack.pop()
                left = stack.pop()

                if char == "&":
                    stack.append(left and right)
                elif char == "|":
                    stack.append(left or right)
                elif char == "^":
                    stack.append(left != right)
                elif char == ">":
                    stack.append((not left) or right)
                elif char == "=":
                    stack.append(left == right)
        else:
            raise ValueError(f"Caractère invalide : '{char}'")

    if len(stack) != 1:
        raise ValueError("Formule invalide : mauvaise structure (stack != 1)")

    return stack[0]


def validate_formula(formula: str):
    """Valide la structure de la formule RPN."""
    stack_size = 0
    operators = {"!", "&", "|", "^", ">", "="}

    for char in formula:
        if char in "01ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            stack_size += 1
        elif char in operators:
            if char == "!":
                if stack_size < 1:
                    raise ValueError(f"Pas assez d'opérandes pour '{char}'")
                # une opération unaire : pile inchangée
            else:
                if stack_size < 2:
                    raise ValueError(f"Pas assez d'opérandes pour '{char}'")
                stack_size -= 1
        else:
            raise ValueError(f"Caractère invalide : '{char}'")

    if stack_size != 1:
        raise ValueError(
            "Formule invalide : mauvaise structure (stack != 1 à la fin)"
        )


def sat(formula: str) -> bool:
    """Détermine si la formule est satisfiable."""

    if not formula:
        raise ValueError("Formule vide")

    # Nettoyage des espaces
    formula = formula.replace(" ", "")

    # Validation de la structure
    validate_formula(formula)

    # Extraction des variables
    variables = sorted(set([c for c in formula if c.isalpha()]))

    # Cas où il n'y a pas de variables
    if not variables:
        return eval_formula(formula, {})

    nb_vars = len(variables)

    # Énumération de toutes les assignations possibles
    for i in range(2 ** nb_vars):
        combo = [(variables[j], bool((i >> j) & 1)) for j in range(nb_vars)]
        values = dict(combo)

        if eval_formula(formula, values):
            return True

    return False
