def adder(a: int, b: int) -> int:
    """Addition bitwise"""
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a


def multiplier(a: int, b: int) -> int:
    """Multiplication avec des opérations bitwise uniquement"""
    if a < 0 or b < 0:
        raise ValueError("Les nombres doivent être positifs.")

    result = 0
    while b > 0:
        if b & 1:
            result = adder(result, a)
        a = a << 1
        b = b >> 1

    return result
