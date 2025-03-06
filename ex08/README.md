# 🌟 Exercise 08 - Powerset

## 🎯 Objectif
Implémenter une fonction qui **génère l'ensemble des parties (`powerset`)** d'un ensemble donné de nombres entiers.

## 📌 Contraintes
- L'ensemble d'entrée est une **liste de nombres entiers**.
- L'ensemble **ne contient pas de doublons**.
- Le résultat doit inclure **l'ensemble vide** et **toutes les combinaisons possibles des éléments de l'ensemble**.
- L'ordre des sous-ensembles dans la sortie n'est **pas imposé**.

## 🚀 Utilisation

### 📌 Lancer un test spécifique :
```sh
make test EX=08
```

### 📌 Lancer tous les tests :
```sh
make test_all
```

### 📌 Exécuter la fonction directement :
```sh
docker run --rm -it enter-the-matrix python ex08/powerset.py "[1, 2, 3]"
```
📌 **Sortie attendue :**
```sh
[[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
```

## 🔬 Tests unitaires
Les tests sont définis dans `tests/test_08.py`.  
Ils vérifient :
- ✅ **Cas de base** : Ensemble vide, ensemble avec un seul élément.
- ✅ **Cas avec plusieurs éléments** : `{1, 2}`, `{1, 2, 3}`.
- ✅ **Cas avec des nombres négatifs** : `{-1, 0, 1}`.
- ✅ **Cas plus grand** : `{1, 2, 3, 4}` avec validation du nombre attendu de sous-ensembles.

## ✅ Exemples de fonctionnement
```sh
$ python3 ex08/powerset.py "[1, 2, 3]"
[[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
```
