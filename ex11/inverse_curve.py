def reverse_map(value: float) -> tuple[int, int]:
    """
    Retourne les coordonnées (x, y) mappées depuis la valeur n.
    """
    if not isinstance(value, float):
        raise TypeError("La valeur doit être un float.")
    if not 0.0 <= value < 1.0:
        raise ValueError("La valeur doit être comprise dans [0.0, 1.0).")

    bits_needed = 2 if value > 0.75 else 1

    max_value = 2 ** (bits_needed * 2)
    morton_code = int(value * max_value)

    def deinterleave_bits(code, bits=bits_needed):
        x = 0
        y = 0
        for i in range(bits):
            y |= ((code >> (2 * i)) & 1) << i
            x |= ((code >> (2 * i + 1)) & 1) << i
        return x, y

    return deinterleave_bits(morton_code)
