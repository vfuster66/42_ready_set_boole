# 🏛 Exercise 04 - Truth Table

## 🎯 Objectif
Implémenter une fonction qui **affiche la table de vérité** d'une formule logique en **notation polonaise inversée (RPN)**.

## 📌 Contraintes
- **Symboles autorisés** :
  - `A...Z` → Variables distinctes (jusqu'à 26).
  - `!` (¬) → Négation
  - `&` (∧) → Conjonction (ET logique)
  - `|` (∨) → Disjonction (OU logique)
  - `^` (⊕) → Disjonction exclusive (XOR)
  - `>` (⇒) → Implication logique
  - `=` (⇔) → Équivalence logique
- **Affichage formaté** d'une table de vérité.

## 🚀 Utilisation
### 📌 lancer le test :
```sh
make test EX=04
```

### 📌 Lancer tous les tests :
```sh
make test_all
```

---

## ✅ Exemple de fonctionnement
```sh
$ python ex04/print_truth_table.py "A!"
| A | = |
|---|---|
| 0 | 1 |
| 1 | 0 |
```

---