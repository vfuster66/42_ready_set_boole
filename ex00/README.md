# 🧮 Exercise 00 - Adder

## 🎯 Objectif
Implémenter une fonction qui additionne deux nombres **sans utiliser `+`**, mais uniquement **des opérations bitwise**.

## 📌 Contraintes
- **Opérations autorisées** :
  - `&` (AND)
  - `|` (OR)
  - `^` (XOR)
  - `<<` (décalage gauche)
  - `>>` (décalage droit)
  - `=` (assignation)
  - `==, !=, <, >, <=, >=` (comparaison)
- **Pas d’opérateurs d’incrémentation** (`+= 1` ou `++`).
- **Uniquement des entiers naturels** (pas de négatifs).

## 🔬 Tests unitaires
Les tests sont dans `tests/test_00.py`.  
Ils couvrent :
- **Cas normaux** (`2 + 3 = 5`, `7 + 8 = 15`).
- **Cas limites** (`0`, **grands nombres**, `10⁶ + 10⁶`).
- **Propriétés mathématiques** (commutativité, associativité).
- **Erreurs attendues** (`None`, `"10"`, `-5`).

📌 **Lancer ce test :**
```sh
make test EX=00
```

📌 **Lancer tous les tests :**
```sh
make test
```

---

## 📝 Explication de l'implémentation
L'addition binaire est effectuée avec :
- `XOR (^)` pour obtenir la **somme sans retenue**.
- `AND (&)`, suivi d'un **décalage (`<<`)**, pour **propager la retenue**.

### 🔹 **Code `adder.py`**
```python
def adder(a: int, b: int) -> int:
    """ Addition avec des opérations bitwise uniquement """
    if a < 0 or b < 0:
        raise ValueError("Les nombres doivent être positifs.")

    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1

    return a
```

---