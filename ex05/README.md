# 🔄 Exercise 05 - Negation Normal Form (NNF)

## 🎯 Objectif
Implémenter une fonction qui **convertit une formule logique en notation polonaise inversée (`RPN`) en sa Forme Normale de Négation (`NNF`)**.

## 📌 Contraintes
- **Toutes les négations (`!`) doivent être directement appliquées aux variables (`A-Z`).**
- **Les opérateurs `>`, `=`, `^` doivent être supprimés et remplacés par `!`, `&`, et `|`.**
- **Application des lois de De Morgan** :
  - `!(A & B) = !A | !B`
  - `!(A | B) = !A & !B`
  - `A > B` devient `¬A ∨ B`
  - `A = B` devient `(A ∧ B) ∨ (¬A ∧ ¬B)`
  - `¬(A = B)` devient `(A ∧ ¬B) ∨ (¬A ∧ B)`

## 🚀 Utilisation
### 📌 Lancer le test :
```sh
make test EX=05
```

### 📌 Lancer tous les tests :
```sh
make test_all
```

### 📌 Lancer `negation_normal_form.py` manuellement :
```sh
docker run --rm -it enter-the-matrix python ex05/negation_normal_form.py "AB&!"
```
📌 **Sortie attendue :**
```sh
NNF de 'AB&!' = A!B!|
```

## 🔬 Tests unitaires
Les tests sont dans `tests/test_05.py`.  
Ils couvrent :
- **Formules valides** (`AB&!`, `AB|!`, `AB>`, `AB=`).
- **Transformations complexes** (`AB|C&!`, `ABC&|D!`).
- **Détection des erreurs** (formules invalides).
- **Équivalences et implications combinées** (`A ⇔ (B ∨ C)`, `A ⇒ (B ∧ C)`).

---

## ✅ Exemple de fonctionnement
```sh
$ python3 ex05/negation_normal_form.py "AB|C="
NNF de 'AB|C=' = AB|C&A!B!|C!&|
```
