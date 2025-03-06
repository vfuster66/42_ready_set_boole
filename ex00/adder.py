def adder(a: int, b: int) -> int:
    """
    Performs addition using only bitwise operations.

    Args:
        a (int): First natural number (must be >= 0).
        b (int): Second natural number (must be >= 0).

    Returns:
        int: The sum of a and b.
    """
    if a < 0 or b < 0:
        raise ValueError("Both numbers must be non-negative.")

    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1

    return a


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python adder.py <a> <b>")
    else:
        try:
            a, b = map(int, sys.argv[1:3])
            print(f"{a} + {b} = {adder(a, b)}")
        except ValueError:
            print("Error: Please provide two valid integers.")
