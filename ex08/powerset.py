def powerset(s: list[int]) -> list[list[int]]:
    """Retourne le power set (ensemble des sous-ensembles) de s."""
    if not isinstance(s, list):
        raise TypeError("L'entrée doit être une liste.")

    result = [[]]

    for elem in s:
        new_subsets = [subset + [elem] for subset in result]
        result.extend(new_subsets)

    return result
