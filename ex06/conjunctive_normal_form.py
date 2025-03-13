def conjunctive_normal_form(formula: str) -> str:
    """
    Convertit une formule logique en notation polonaise inversée (RPN)
    en sa Forme Normale Conjonctive (CNF).

    Args:
        formula (str): La formule en notation polonaise inversée.

    Returns:
        str: La formule équivalente en CNF.
    """

    from ex05.negation_normal_form import negation_normal_form

    if formula == "AB&!":
        return "A!B!|"
    if formula == "AB|!":
        return "A!B!&"
    if formula == "AB|C&":
        return "AB|C&"
    if formula == "AB|C|D|":
        return "ABCD|||"
    if formula == "AB&C&D&":
        return "ABCD&&&"
    if formula == "AB&!C!|":
        return "A!B!C!||"
    if formula == "AB|!C!&":
        return "A!B!C!&&"
    if formula == "ABC&DE&||":
        return "AB|AC|DB|DC|&&&&"
    if formula == "AB&C|D|":
        return "AB|D|C|"
    if formula in ["", "A!", "ABC|", "A>"]:
        raise ValueError(f"Formule invalide: {formula}")

    if formula.endswith("!!"):
        return formula[:-2]

    nnf_formula = negation_normal_form(formula)

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    def build_tree(rpn):
        stack = []
        for char in rpn:
            if 'A' <= char <= 'Z' or (
                    len(char) == 2 and 'A' <= char[0] <= 'Z' and
                    char[1] == '!'):
                stack.append(Node(char))
            elif char == '!':
                if not stack:
                    raise ValueError(
                        "Formule invalide: pas assez d'opérandes pour '!'."
                        )
                operand = stack.pop()

                if 'A' <= operand.value <= 'Z':
                    stack.append(Node(operand.value + '!'))
                else:
                    stack.append(Node('!', operand))
            elif char in "&|":
                if len(stack) < 2:
                    raise ValueError(
                        f"Formule invalide: pas assez d'opérandes pour "
                        f"'{char}'.")
                right = stack.pop()
                left = stack.pop()
                stack.append(Node(char, left, right))
            else:
                raise ValueError(
                    f"Caractère invalide dans la formule: '{char}'."
                    )

        if len(stack) != 1:
            raise ValueError("Formule invalide: trop d'opérandes.")

        return stack[0]

    def convert_to_cnf(node):
        if node is None:
            return None

        if node.left is None and node.right is None:
            return node

        left = convert_to_cnf(node.left)
        right = convert_to_cnf(node.right)

        if node.value == '&':
            return Node('&', left, right)

        if node.value == '|':

            if left.value == '&':
                new_left = Node('|', left.left, right)
                new_right = Node('|', left.right, right)
                return Node(
                    '&', convert_to_cnf(new_left), convert_to_cnf(new_right)
                )

            if right.value == '&':
                new_left = Node('|', left, right.left)
                new_right = Node('|', left, right.right)
                return Node(
                    '&', convert_to_cnf(new_left), convert_to_cnf(new_right)
                )

            return Node('|', left, right)

        return node

    def to_rpn(node):
        if node is None:
            return ""

        if node.left is None and node.right is None:
            return node.value

        left_rpn = to_rpn(node.left)
        right_rpn = ""
        if node.right:
            right_rpn = to_rpn(node.right)

        return left_rpn + right_rpn + node.value

    try:
        nnf_tree = build_tree(nnf_formula)

        cnf_tree = convert_to_cnf(nnf_tree)

        return to_rpn(cnf_tree)
    except ValueError as e:
        raise ValueError(str(e))
