# 🌟 Exercise 09 - Set Evaluation

## 🎯 Objectif
Implémenter une fonction qui **évalue une expression logique en notation polonaise inversée (`RPN`) sur des ensembles de nombres entiers**.

## 📌 Contraintes
- **Chaque lettre (`A-Z`) représente un ensemble distinct.**
- **Les opérations logiques sont appliquées sur ces ensembles** :
  - `!` (Négation) : Complément de l’ensemble dans l’univers global.
  - `&` (Conjonction) : Intersection de deux ensembles.
  - `|` (Disjonction) : Union de deux ensembles.
  - `^` (XOR) : Différence symétrique entre deux ensembles.
  - `>` (Implication) : Complément du premier ensemble uni avec le second.
  - `=` (Équivalence) : `(A ⇒ B) ∧ (B ⇒ A)`.
- L’univers global est **l’union de tous les ensembles donnés**.
- **Le nombre d’ensembles fournis doit être égal au nombre de variables distinctes dans la formule.**
- En cas de **formule invalide**, le programme doit lever une erreur.

## 🚀 Utilisation

### 📌 Lancer un test spécifique :
```sh
make test EX=09
```

### 📌 Lancer tous les tests :
```sh
make test_all
```

### 📌 Exécuter la fonction directement :
```sh
docker run --rm -it enter-the-matrix python ex09/set_evaluation.py "AB|" "[{1,2}, {3,4}]"
```
📌 **Sortie attendue :**
```sh
{1, 2, 3, 4}
```

## 🔬 Tests unitaires
Les tests sont définis dans `tests/test_09.py`.  
Ils vérifient :
- ✅ **Opérations de base** :
  - Union (`AB|`), intersection (`AB&`), négation (`A!`), XOR (`AB^`).
- ✅ **Opérations complexes** :
  - `(A | B) & C`, `¬A ∨ B`, `A = B`.
- ✅ **Cas d’erreurs** :
  - Formule invalide (`""`).
  - Nombre d’ensembles incorrect.
  - Caractères non valides.

## ✅ Exemples de fonctionnement
```sh
$ python3 ex09/set_evaluation.py "AB|" "[{1,2}, {3,4}]"
{1, 2, 3, 4}

$ python3 ex09/set_evaluation.py "AB&C|!" "[{1,2}, {2,3}, {4}]"
{1, 3}
```
