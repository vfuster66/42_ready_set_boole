def multiplier(a: int, b: int) -> int:
    """
    Performs multiplication using only bitwise operations.

    Args:
        a (int): First natural number (must be >= 0).
        b (int): Second natural number (must be >= 0).

    Returns:
        int: The product of a and b.
    """
    if a < 0 or b < 0:
        raise ValueError("Both numbers must be non-negative.")

    result = 0
    while b > 0:
        if b & 1:
            result = result + a

        a = a << 1
        b = b >> 1

    return result


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python multiplier.py <a> <b>")
    else:
        try:
            a, b = map(int, sys.argv[1:3])
            print(f"{a} * {b} = {multiplier(a, b)}")
        except ValueError:
            print("Error: Please provide two valid integers.")
