def eval_formula(formula: str) -> bool:
    """
    Evaluates a propositional formula in Reverse Polish Notation (RPN).

    Args:
        formula (str): The formula string containing logical operators.

    Returns:
        bool: The evaluation result (True or False).
    """
    stack = []
    operators = {'!': 1, '&': 2, '|': 2, '^': 2, '>': 2, '=': 2}
    valid_chars = set("01!&|^>=")

    for char in formula:
        if char not in valid_chars:
            raise ValueError(f"Invalid character in formula: '{char}'.")

        if char == '0':
            stack.append(False)
        elif char == '1':
            stack.append(True)
        elif char in operators:
            if len(stack) < operators[char]:
                raise ValueError(
                    f"Invalid formula: Not enough operands for '{char}'."
                )

            if char == '!':
                a = stack.pop()
                stack.append(not a)
            else:
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

    if len(stack) != 1:
        raise ValueError(
            "Invalid formula: Stack does not contain a single result."
            )

    return stack[0]


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python eval_formula.py <formula>")
    else:
        try:
            formula = sys.argv[1]
            result = eval_formula(formula)
            print(f"Evaluation of '{formula}' = {result}")
        except ValueError as e:
            print(f"Error: {e}")
