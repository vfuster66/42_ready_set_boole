# 📈 Exercise 10 - Curve

## 🎯 Objectif
Implémenter une fonction qui **encode des coordonnées `(x, y)` en une valeur unique dans l'intervalle `[0, 1]`** via une courbe remplissant l'espace (**Z-order curve** ou **Hilbert curve**).

## 📌 Contraintes
- Les coordonnées `(x, y)` sont comprises dans **l'intervalle `[0, 2^16 - 1]`** (`0 ≤ x, y < 65536`).
- La fonction doit être **bijective** : chaque paire `(x, y)` est associée à une **valeur unique** et **inversement**.
- Le résultat est un **nombre flottant dans `[0,1]`**.
- **Hors limites** : si `x` ou `y` ne respectent pas la contrainte, une **erreur** doit être levée.

---

## 🚀 **Utilisation**
### 📌 **Lancer les tests**
```sh
make test EX=10
```

### 📌 **Exécuter la fonction directement**
```sh
docker run --rm -it enter-the-matrix python ex10/curve.py 32768 32768
```
📌 **Sortie attendue :**
```sh
0.5000000000
```

---

## 🔬 **Tests unitaires**
Les tests sont définis dans `tests/test_10.py`.  
Ils vérifient :
- ✅ **Cas de base** :
  - `(0,0) → 0.0000000000`
  - `(65535,65535) → 1.0000000000`
  - `(0,65535) → 0.2500000000`
  - `(65535,0) → 0.7500000000`
- ✅ **Valeurs intermédiaires** (`32768, 32768`, `32767, 32768`…).
- ✅ **Cas limites et erreurs** (`x < 0`, `y ≥ 65536`…).
- ✅ **Cas aléatoires** avec des coordonnées générées dynamiquement.

---

## ✅ **Exemples de fonctionnement**
```sh
$ python3 ex10/curve.py 0 0
0.0000000000

$ python3 ex10/curve.py 65535 65535
1.0000000000

$ python3 ex10/curve.py 65535 0
0.7500000000

$ python3 ex10/curve.py 0 65535
0.2500000000
```

---

## 🛠 **Implémentation**
La conversion utilise **l'entrelacement des bits** (`bit-interleaving`), en utilisant la **Z-order curve** :

```python
def bit_interleave(x: int, y: int) -> int:
    def spread_bits(n: int) -> int:
        """Propage les bits pour l'entrelacement"""
        n = (n | (n << 8)) & 0x00FF00FF
        n = (n | (n << 4)) & 0x0F0F0F0F
        n = (n | (n << 2)) & 0x33333333
        n = (n | (n << 1)) & 0x55555555
        return n
    return (spread_bits(y) << 1) | spread_bits(x)
```

Puis, la valeur obtenue est **normalisée** pour être comprise dans `[0,1]` :
```python
def map(x: int, y: int) -> float:
    if not (0 <= x < 2**16 and 0 <= y < 2**16):
        raise ValueError("Erreur: Les coordonnées doivent être dans [0, 2^16-1]")
    
    max_index = (2**32) - 1
    return bit_interleave(x, y) / max_index
```

---
