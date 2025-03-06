# 🔄 Exercise 11 - Inverse Function

## 🎯 Objectif
Implémenter la fonction **inverse** de la courbe remplissant l’espace utilisée dans l’exercice précédent.  
Cette fonction doit convertir une **valeur unique** dans `[0,1]` en une paire de **coordonnées `(x, y)`**.

## 📌 Contraintes
- **Entrée** : Un nombre flottant `n ∈ [0,1]` représentant une position sur la courbe.
- **Sortie** : Un couple `(x, y)`, où `x, y ∈ [[0; 2^16 - 1]] ⊂ ℕ²`.
- La transformation doit être **bijective**, c'est-à-dire :
  - `reverse_map(map(x, y)) == (x, y)`
  - `map(reverse_map(n)) == n`
- Si l’entrée est **hors de l’intervalle `[0,1]`**, lever une **erreur**.

---

## 🚀 Utilisation

### 📌 Lancer un test spécifique :
```sh
make test EX=11
```

### 📌 Lancer tous les tests :
```sh
make test_all
```

### 📌 Exécuter la fonction manuellement :
```sh
docker run --rm -it enter-the-matrix python ex11/inverse_curve.py 0.75
```
📌 **Sortie attendue :**
```sh
(32768, 32768)
```

---

## 🔬 Tests unitaires
Les tests sont définis dans `tests/test_11.py`.  
Ils vérifient :
- ✅ **Cas de base** :
  - `0.0 → (0, 0)`
  - `1.0 → (65535, 65535)`
- ✅ **Cas aux limites** :
  - `1/3 → (65535, 0)`
  - `2/3 → (0, 65535)`
- ✅ **Valeurs intermédiaires** :
  - `0.75 → (32768, 32768)`
- ✅ **Validation bijective** :
  - `reverse_map(map(x, y)) == (x, y)`, testé avec des valeurs aléatoires.

---

## ✅ Exemples de fonctionnement

```sh
$ python3 ex11/inverse_curve.py 0.0
(0, 0)

$ python3 ex11/inverse_curve.py 1.0
(65535, 65535)

$ python3 ex11/inverse_curve.py 0.6666666667
(0, 65535)

$ python3 ex11/inverse_curve.py 0.75
(32768, 32768)

$ python3 ex11/inverse_curve.py -0.1
Erreur: La valeur doit être dans [0,1].
```
