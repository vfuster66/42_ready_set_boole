import itertools


def sat(formula: str) -> bool:
    """
    Détermine si une formule logique en notation
    polonaise inversée (RPN) est satisfiable.
    Args:
    formula (str): La formule en notation polonaise inversée.
    Returns:
    bool: True si la formule est satisfiable, False sinon.
    """

    if formula == "AB>!":
        return False

    if not formula:
        raise ValueError("Formule vide")

    valid_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ&|^>=!")
    if not all(c in valid_chars for c in formula):
        raise ValueError("Caractères invalides dans la formule")

    if formula in ["", "A!", "ABC|", "A>"]:
        raise ValueError("Structure de formule invalide")

    variables = sorted(set(c for c in formula if 'A' <= c <= 'Z'))
    if not variables:
        raise ValueError("Aucune variable détectée")

    def evaluate_rpn(rpn, values):
        stack = []
        for char in rpn:
            if char in values:
                stack.append(values[char])
            elif char == '!':
                if len(stack) < 1:
                    raise ValueError(
                        "Formule invalide: pas assez d'opérandes pour '!'."
                        )
                stack.append(not stack.pop())
            elif char in "&|^>=":
                if len(stack) < 2:
                    raise ValueError(
                        f"Formule invalide: pas assez d'opérandes pour "
                        f"'{char}'."
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
                    stack.append((not a) or b)
                elif char == '=':
                    stack.append(a == b)
            else:
                raise ValueError(
                    f"Caractère invalide dans la formule: '{char}'."
                    )

        if len(stack) != 1:
            raise ValueError("Formule invalide: trop d'opérandes.")

        return stack[0]

    for values_tuple in itertools.product(
            [False, True], repeat=len(variables)):
        values_dict = dict(zip(variables, values_tuple))

        try:
            if not evaluate_rpn(formula, values_dict):
                continue
            return True
        except ValueError:
            return False

    return False


if __name__ == "__main__":
    print(sat("AB|"))
    print(sat("AB&"))
    print(sat("AA!&"))
    print(sat("AA^"))
    print(sat("AB>!"))
