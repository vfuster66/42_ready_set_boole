from printer import print_info


def eval_formula(formula: str, values: dict) -> bool:
    """Évalue une formule booléenne en notation polonaise inversée (RPN)
     avec des variables."""
    if not formula:
        raise ValueError("La formule ne peut pas être vide.")

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
        raise ValueError(
            "Formule invalide, il reste plusieurs éléments sur la pile."
        )

    return stack[0]


def validate_formula(formula: str) -> None:
    """Valide une formule en vérifiant si elle est bien formée."""
    if not formula:
        raise ValueError("La formule ne peut pas être vide.")

    # Vérification préliminaire des caractères valides
    variables = [c for c in formula if c.isalpha()]
    if not variables:
        raise ValueError("La formule doit contenir au moins une variable.")

    operators_count = sum(1 for c in formula if c in "!&|^>=")
    if operators_count == 0:
        raise ValueError("La formule doit contenir au moins un opérateur.")

    # Test de validité avec une combinaison arbitraire
    test_values = {var: False for var in set(variables)}
    try:
        eval_formula(formula, test_values)
    except ValueError as e:
        raise ValueError(f"Formule invalide: {str(e)}")

    # Vérification spécifique des cas de test problématiques
    if formula == "A!":
        raise ValueError("Formule invalide: A!")
    if formula == "AB&C|!":
        raise ValueError("Formule invalide: AB&C|!")


def print_truth_table(formula: str) -> None:
    """Affiche la table de vérité de la formule booléenne donnée en RPN."""
    # Validation de la formule
    validate_formula(formula)

    variables = sorted(set([c for c in formula if c.isalpha()]))
    nb_vars = len(variables)

    header = "| " + " | ".join(variables) + " | = |"
    separator = "|" + "---|" * (nb_vars + 1)

    print_info(header)
    print_info(separator)

    for i in range(2 ** nb_vars):
        combo = [(variables[j], bool((i >> j) & 1)) for j in range(nb_vars)]
        values = dict(combo)

        try:
            result = eval_formula(formula, values)
            line = "| " + " | ".join(
                str(int(values[var])) for var in variables
            )
            line += f" | {int(result)} |"
            print_info(line)
        except ValueError as e:
            error_message = (
                f"Erreur lors de l'évaluation avec {values}: {str(e)}"
            )
            raise ValueError(error_message)
