import sys

from typing import Tuple


def bit_deinterleave(n: int) -> Tuple[int, int]:
    """
    Désentrelace les bits pour récupérer les coordonnées x et y.

    Args:
        n (int): Entier représentant une position sur la courbe.

    Returns:
        (int, int): Coordonnées x et y originales.
    """
    def compact_bits(n: int) -> int:
        """Récupère les bits séparés pour reconstruire la coordonnée."""
        n &= 0x55555555
        n = (n | (n >> 1)) & 0x33333333
        n = (n | (n >> 2)) & 0x0F0F0F0F
        n = (n | (n >> 4)) & 0x00FF00FF
        n = (n | (n >> 8)) & 0x0000FFFF
        return n

    return compact_bits(n), compact_bits(n >> 1)


def reverse_map(value: float) -> Tuple[int, int]:
    """
    Décode un nombre unique de l'intervalle [0,1] en coordonnées (x, y).

    Args:
        value (float): Valeur encodée dans l'intervalle [0,1].

    Returns:
        (int, int): Coordonnées x et y originales.
    """
    if not (0.0 <= value <= 1.0):
        raise ValueError("Erreur: La valeur doit être dans [0,1].")

    max_index = (2**32) - 1
    int_value = round(value * max_index)

    return bit_deinterleave(int_value)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python inverse_curve.py <float>")
    else:
        try:
            value = float(sys.argv[1])
            print(reverse_map(value))
        except ValueError:
            print(
                "Erreur: Veuillez entrer une valeur flottante valide entre "
                "0 et 1."
                )
