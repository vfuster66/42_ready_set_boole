import sys


def bit_interleave(x: int, y: int) -> int:
    """
    Interlace les bits de x et y pour obtenir un indice unique.
    Args:
    x (int): Coordonnée x (0 <= x <= 2^16 - 1)
    y (int): Coordonnée y (0 <= y <= 2^16 - 1)
    Returns:
    int: Un entier unique correspondant à la position sur la courbe.
    """
    def spread_bits(n: int) -> int:
        """Propage les bits pour l'entrelacement"""
        n = (n | (n << 8)) & 0x00FF00FF
        n = (n | (n << 4)) & 0x0F0F0F0F
        n = (n | (n << 2)) & 0x33333333
        n = (n | (n << 1)) & 0x55555555
        return n

    return (spread_bits(y) << 1) | spread_bits(x)


def map(x: int, y: int) -> float:
    """
    Encode les coordonnées (x, y) en une unique valeur dans [0,1].
    Args:
    x (int): Coordonnée x (0 <= x <= 2^16 - 1)
    y (int): Coordonnée y (0 <= y <= 2^16 - 1)
    Returns:
    float: Un nombre unique dans l'intervalle [0,1].
    """
    if not (0 <= x < 2**16 and 0 <= y < 2**16):
        raise ValueError(
            "Erreur: Les coordonnées doivent être dans [0, 2^16-1]"
                         )

    max_index = (2**32) - 1
    return bit_interleave(x, y) / max_index


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python curve.py <x> <y>")
    else:
        try:
            x, y = int(sys.argv[1]), int(sys.argv[2])
            print(map(x, y))
        except ValueError:
            print("Erreur: Veuillez entrer des coordonnées valides "
                  "(entiers 0 <= x, y < 2^16).")
