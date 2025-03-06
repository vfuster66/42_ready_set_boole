# 🔄 Exercise 07 - SAT Solver

## 🎯 Objectif
Implémenter une fonction qui **détermine si une formule logique en notation polonaise inversée (`RPN`) est satisfiable**.

## 📌 Contraintes
- **Une formule est satisfiable s'il existe une assignation de valeurs (`True/False`) aux variables (`A-Z`) qui la rende vraie.**
- **L'évaluation doit respecter la notation polonaise inversée (`RPN`).**
- **Gestion des opérateurs logiques** :
  - `!` : **Négation** (`¬A`)
  - `&` : **Conjonction** (`A ∧ B`)
  - `|` : **Disjonction** (`A ∨ B`)
  - `^` : **Disjonction exclusive** (`A ⊕ B`)
  - `>` : **Implication** (`A ⇒ B`, équivalent à `¬A ∨ B`)
  - `=` : **Équivalence** (`A ⇔ B`, équivalent à `(A ∧ B) ∨ (¬A ∧ ¬B)`)

## 🚀 Utilisation
### 📌 Lancer le test :
```sh
make test EX=07
```

### 📌 Lancer tous les tests :
```sh
make test_all
```

### 📌 Lancer `sat.py` manuellement :
```sh
docker run --rm -it enter-the-matrix python ex07/sat.py "AB|"
```
📌 **Sortie attendue :**
```sh
SAT de 'AB|' = True
```

## 🔬 Tests unitaires
Les tests sont dans `tests/test_07.py`.  
Ils couvrent :
- **Formules valides et invalides**
- **Cas triviaux (`A ∨ B`, `A ∧ B`, `A ⊕ A`)**
- **Formules toujours vraies (tautologies)**
- **Formules toujours fausses (contradictions)**
- **Transformations complexes (`A ⇒ B`, `A ⇔ B`)**

---

## ✅ Exemples de fonctionnement
```sh
$ python3 ex07/sat.py "AB|"
SAT de 'AB|' = True

$ python3 ex07/sat.py "AB&"
SAT de 'AB&' = True

$ python3 ex07/sat.py "AA!&"
SAT de 'AA!&' = False

$ python3 ex07/sat.py "AA^"
SAT de 'AA^' = False

$ python3 ex07/sat.py "AB>!"
SAT de 'AB>!' = False
```
