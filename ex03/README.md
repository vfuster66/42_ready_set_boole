# 🔢 Exercise 03 - Boolean Evaluation

## 🎯 Objectif
Implémenter une fonction qui **évalue une expression logique en notation polonaise inversée (RPN)** et retourne le résultat.

## 📌 Contraintes
- **Symboles autorisés** :
  - `0` (⊥) → Faux
  - `1` (⊤) → Vrai
  - `!` (¬) → Négation
  - `&` (∧) → Conjonction (ET logique)
  - `|` (∨) → Disjonction (OU logique)
  - `^` (⊕) → Disjonction exclusive (XOR)
  - `>` (⇒) → Implication logique
  - `=` (⇔) → Équivalence logique
- **Utilisation d'une pile (`stack`)** pour gérer l'évaluation.

## 🚀 Utilisation
### 📌 Lancer le test :
```sh
make test EX=03
```

### 📌 Lancer tous les tests :
```sh
make test_all
```

## 🔬 Tests unitaires
Les tests sont dans `tests/test_03.py`.  
Ils couvrent :
- **Formules valides** (`10&`, `10|`, `11>`, `10=`).
- **Formules complexes** (`101|&`, `110|^`, `10&1>`).
- **Gestion des erreurs** (`formules invalides`).

---

## ✅ Exemple de fonctionnement
```sh
$ python ex03/eval_formula.py "1011||="
Evaluation of '1011||=' = True
```
