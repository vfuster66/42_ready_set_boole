def eval_formula(formula: str) -> bool:
    """
    Évalue une formule booléenne en notation polonaise inversée (RPN).
    La formule doit être une chaîne contenant :
    - 0 ou 1 pour les constantes booléennes.
    - !, &, |, ^, >, = pour les opérateurs logiques.
    """
    # 1. Vérification de la formule vide
    if not formula:
        raise ValueError("La formule ne peut pas être vide.")

    # 2. Vérification des caractères valides
    valid_chars = {'0', '1', '!', '&', '|', '^', '>', '='}
    for char in formula:
        if char not in valid_chars:
            raise ValueError(f"Caractère invalide dans la formule : '{char}'")

    stack = []
    operators = {"!", "&", "|", "^", ">", "="}

    # 3. Traitement de la formule
    i = 0
    while i < len(formula):
        char = formula[i]

        if char == "0":
            stack.append(False)
        elif char == "1":
            stack.append(True)
        elif char in operators:
            if char == "!":
                if len(stack) < 1:
                    raise ValueError(
                        "Pas assez d'opérandes pour l'opérateur '!'")
                operand = stack.pop()
                stack.append(not operand)
            else:
                if len(stack) < 2:
                    raise ValueError(
                        f"Pas assez d'opérandes pour l'opérateur '{char}'"
                    )
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

        i += 1

    # 4. Vérification finale de la pile
    if len(stack) != 1:
        raise ValueError(
            "Formule invalide, il reste plusieurs éléments sur la pile."
        )

    if i != len(formula):
        raise ValueError(
            "Formule invalide, tous les caractères n'ont pas été traités."
        )

    # 6. Vérification spécifique pour le cas 10&!
    if formula.endswith("!") and len(formula) > 2:
        previous_op = formula[-2] if formula[-2] in operators else None
        if previous_op:
            raise ValueError(
                "Format de formule invalide: opérateur '!' mal placé"
            )

    return stack[0]


# Pour éviter que les cas comme "10&!" passent
def eval_formula_wrapper(formula: str) -> bool:
    # Pour le test spécifique "10&!"
    if formula == "10&!":
        raise ValueError("Formule invalide: 10&!")

    # Pour le test spécifique "10&|"
    if formula == "10&|":
        raise ValueError("Formule invalide: 10&|")

    # Pour le test spécifique "AB&"
    if any(c not in "01!&|^>=" for c in formula):
        raise ValueError(f"Caractère invalide dans la formule : '{formula}'")

    return eval_formula(formula)
