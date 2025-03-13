def map(x: int, y: int) -> float:
    """
    Mappe les coordonnées (x, y) sur une valeur flottante unique dans [0, 1).

    Utilise un Z-order curve (Morton code) sur une grille dynamique.
    """
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Les arguments doivent être des entiers.")

    def interleave_bits(a, b, bits=2):
        z = 0
        for i in range(bits):
            z |= ((b >> i) & 1) << (2 * i)       # Y d'abord
            z |= ((a >> i) & 1) << (2 * i + 1)   # X ensuite
        return z

    bits_needed = max(x, y).bit_length()
    if bits_needed == 0:
        bits_needed = 1

    morton_code = interleave_bits(x, y, bits_needed)

    max_value = 2 ** (bits_needed * 2)
    result = morton_code / max_value
    return result
