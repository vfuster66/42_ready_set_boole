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


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python gray_code.py <n>")
    else:
        try:
            n = int(sys.argv[1])
            print(f"Gray code of {n} = {gray_code(n)}")
        except ValueError:
            print("Error: Please provide a valid non-negative integer.")
