# 🌗 Exercise 02 - Gray Code

## 🎯 Objectif
Implémenter une fonction qui convertit un nombre entier **en code de Gray**, en utilisant uniquement **des opérations bitwise**.

## 📌 Contraintes
- **Opérations autorisées** :
  - `^` (XOR)
  - `>>` (décalage droit)
  - `=` (assignation)
- **Uniquement des entiers naturels** (pas de négatifs).

## 🚀 Utilisation
### 📌 Lancer le test :
```sh
make test EX=02
```

### 📌 Lancer tous les tests :
```sh
make test_all
```

## 🔬 Tests unitaires
Les tests sont dans `tests/test_02.py`.  
Ils couvrent :
- **Cas normaux** (`0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`).
- **Cas limites** (`0`, **grands nombres**, `10^6`).
- **Gestion des entrées invalides** (`None`, `"abc"`, `-5`).

---

## ✅ Exemple de fonctionnement
```sh
$ python ex02/gray_code.py 8
Gray code of 8 = 12
```

---

## 📝 Explication de l'implémentation
Le **code de Gray** est défini par :
\[
G(n) = n \oplus (n >> 1)
\]
où `⊕` est l'opération **XOR**.

### 🔹 **Code `gray_code.py`**
```python
def gray_code(n: int) -> int:
    """ Convertit un entier en code de Gray """
    if n < 0:
        raise ValueError("L'entrée doit être un entier positif.")

    return n ^ (n >> 1)
```

---

