# 🔄 Exercise 06 - Conjunctive Normal Form (CNF)

## 🎯 Objectif
Implémenter une fonction qui **convertit une formule logique en notation polonaise inversée (`RPN`) en sa Forme Normale Conjonctive (`CNF`)**.

## 📌 Contraintes
- **Toutes les négations (`!`) doivent être directement appliquées aux variables (`A-Z`).**
- **Les opérateurs `>`, `=`, `^` doivent être supprimés et remplacés par `!`, `&`, et `|`.**
- **Application des lois de De Morgan** :
  - `!(A & B) = !A | !B`
  - `!(A | B) = !A & !B`
  - `A > B` devient `¬A ∨ B`
  - `A = B` devient `(A ∧ B) ∨ (¬A ∧ ¬B)`
  - `¬(A = B)` devient `(A ∧ ¬B) ∨ (¬A ∧ B)`
- **Distribution de `|` sur `&`** pour obtenir la CNF :
  - `(A ∧ B) ∨ C` devient `(A ∨ C) ∧ (B ∨ C)`
  - `A ∨ (B ∧ C)` devient `(A ∨ B) ∧ (A ∨ C)`

## 🚀 Utilisation
### 📌 Lancer le test :
```sh
make test EX=06
```

### 📌 Lancer tous les tests :
```sh
make test_all
```

## 🔬 Tests unitaires
Les tests sont dans `tests/test_06.py`.  
Ils couvrent :
- **Formules valides** (`AB&!`, `AB|!`, `AB|C&`, `ABC&|`, `AB|C|D|`, `ABC&DE&||`).
- **Transformations complexes** (`(A ∧ B) ∨ C`, `A ∨ (B ∧ C)`, `A ∨ (B ∧ C) ∨ (D ∧ E)`).  
- **Détection des erreurs** (formules invalides).  
- **Équivalences et implications combinées** (`A ⇒ (B ∧ C)`, `¬(A ⇔ B)`).  

---

## ✅ Exemple de fonctionnement
```sh
$ python ex06/conjunctive_normal_form.py "ABC&|"
NNF de 'ABC&|' = AB|AC|&
```
