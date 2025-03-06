# ✖ Exercise 01 - Multiplier

## 🎯 Objectif
Implémenter une fonction qui multiplie deux nombres **sans utiliser `*`**, mais uniquement **des opérations bitwise**.

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

## 🚀 Utilisation
### 📌 Lancer le test :
```sh
make test EX=01
```

### 📌 Lancer tous les tests :
```sh
make test_all
```

## 🔬 Tests unitaires
Les tests sont dans `tests/test_01.py`.  
Ils couvrent :
- **Cas normaux** (`2 * 3 = 6`, `7 * 8 = 56`).
- **Cas limites** (`0`, **grands nombres**, `10⁶ * 10⁶`).
- **Propriétés mathématiques** (commutativité, associativité).
- **Erreurs attendues** (`None`, `"10"`, `-5`).

---

## ✅ Exemple de fonctionnement
```sh
$ python ex01/multiplier.py 8 15
8 * 15 = 120
```
