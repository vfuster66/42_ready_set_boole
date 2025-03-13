def gray_code(n: int) -> int:
    """
    Converts an integer to its equivalent Gray code.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The Gray code equivalent of n.
    """
    if n < 0:
        raise ValueError("The input must be a non-negative integer.")

    return n ^ (n >> 1)
