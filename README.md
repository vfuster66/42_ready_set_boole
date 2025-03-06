# Ready, Set, Boole! 🚀

Ce projet est une introduction à **l'algèbre de Boole** et à **la théorie des ensembles** appliquées à l'informatique et aux mathématiques. Il comprend plusieurs exercices où tu devras manipuler des opérations logiques, créer des tables de vérité, transformer des formules logiques et travailler avec des ensembles.

---

## 📋 Objectifs du projet
- Comprendre et manipuler **l'algèbre de Boole**.
- Construire des opérations logiques en utilisant **uniquement des opérations bitwise**.
- Évaluer des **formules en notation polonaise inversée**.
- Générer et manipuler des **tables de vérité**.
- Travailler avec **les ensembles et leurs opérations**.
- Explorer des **courbes de remplissage d’espace**.

---

## 📂 Structure du projet

```
42_ready_set_boole
│── Dockerfile              # Environnement Python 3.10 avec les dépendances
│── Makefile                # Commandes pour automatiser build et tests
│── requirements.txt        # Dépendances du projet (pytest, colorama...)
│── main.py                 # Script pour exécuter les exercices
│── tests/                  # Tests unitaires pour chaque exercice
│── sujet/                  # Contient le PDF du sujet du projet
│── ex00/ à ex11/           # Exercices à réaliser
```

---

## 🚀 Installation et lancement du projet
### 1️⃣ Prérequis
- **Docker** installé sur ta machine.

### 2️⃣ Construire l’image Docker
```sh
make build
```
Cela crée un conteneur Docker contenant **Python 3.10** et toutes les dépendances nécessaires.

### 3️⃣ Exécuter un exercice **avec ses tests**
```sh
make test EX=00
```
Cela exécute **l’exercice et ses tests unitaires**.

### 4️⃣ Exécuter **tous les tests**
```sh
make test_all
```
Cela exécute **tous les tests des exercices**.

### 5️⃣ Nettoyer l’environnement
```sh
make clean
```
Supprime les conteneurs inutilisés.

```sh
make purge
```
Supprime complètement l’image Docker utilisée.

---

## 🛠 Dépendances
Les dépendances sont listées dans **requirements.txt** :
```txt
pytest
pytest-cov
colorama
graphviz
sympy
```
Pour ajouter une nouvelle dépendance :
1. Ajoute-la dans `requirements.txt`
2. Rebuild l’image Docker :
   ```sh
   make build
   ```

---

## 📖 Exercices disponibles
| Exercice | Description |
|----------|------------|
| ex00 | Addition de nombres avec uniquement des opérations bitwise |
| ex01 | Multiplication avec uniquement des opérations bitwise |
| ex02 | Conversion d'un entier en code de Gray |
| ex03 | Évaluation de formules logiques en notation polonaise inversée |
| ex04 | Génération de tables de vérité |
| ex05 | Transformation d'une formule logique en NNF |
| ex06 | Transformation d'une formule logique en CNF |
| ex07 | Vérification de la satisfiabilité (SAT) d'une formule |
| ex08 | Calcul du powerset d'un ensemble |
| ex09 | Évaluation d'opérations sur des ensembles |
| ex10 | Mapping d'un point (x, y) vers une valeur unique |
| ex11 | Fonction inverse du mapping de ex10 |

---

## 📌 Règles et contraintes
- **Pas de bibliothèques mathématiques** sauf si explicitement autorisé.
- **Respect des contraintes de complexité** (temps et espace).
- **Utilisation d'opérations bitwise** pour les exercices qui le demandent.
- **Code testé avec `pytest`** (les tests sont dans le dossier `tests/`).

---

## 🔢 Opérations bitwise et arithmétique binaire (Ex00, Ex01, Ex02)  

### 🧩 Ce que c'est  
- **L'arithmétique binaire** est la base du calcul en informatique, où les nombres sont manipulés sous forme de **bits** (0 et 1).  
- **Les opérations bitwise** (`&`, `|`, `^`, `<<`, `>>`) permettent de manipuler directement ces bits.  

### 🖥️ Utilité en informatique  
✅ **Optimisation** : Plus rapide que l’arithmétique classique, utilisé dans les systèmes embarqués.  
✅ **Cryptographie et compression** : Utilisé dans les **codes de Gray**, **hashing**, et **algorithmes de compression**.  

---

## 🤖 Évaluation de formules logiques (Ex03, Ex04, Ex05, Ex06, Ex07)  

### 🧩 Ce que c'est  
- Une **formule logique** est une expression utilisant des **variables** (`A, B, C...`) et des **opérateurs logiques** (`&`, `|`, `^`, `!`, `>`, `=`).  
- Ces formules peuvent être **évaluées** (`Ex03`), converties en **table de vérité** (`Ex04`), et mises sous des **formes standardisées** :  
  - **NNF (Normal Forme Négative)** (`Ex05`)  
  - **CNF (Forme Conjonctive Normale)** (`Ex06`)  

### 🖥️ Utilité en informatique  
✅ **Circuits logiques** : Utilisé dans la conception des **processeurs** et **composants électroniques**.  
✅ **Optimisation et intelligence artificielle** : Utilisé en **vérification de logiciels** et **résolution automatique de problèmes complexes**.  

---

## 🧮 Théorie des ensembles et SAT (Ex07, Ex08, Ex09)  

### 🧩 Ce que c'est  
- Un **ensemble** est une collection d'éléments **uniques**.  
- Le **powerset** (`Ex08`) est l’**ensemble de tous les sous-ensembles** possibles.  
- **Les opérations sur les ensembles** (`Ex09`) utilisent des opérateurs logiques (`&`, `|`, `^`, `!`).  
- La **satisfiabilité SAT** (`Ex07`) vérifie si une **formule logique peut être vraie** pour un ensemble donné de valeurs.  

### 🖥️ Utilité en informatique  
✅ **Bases de données** : Optimisation des **requêtes SQL** et gestion des grands ensembles de données.  
✅ **Solveurs SAT** : Utilisé en **intelligence artificielle**, **cybersécurité**, et **résolution de puzzles** comme le **Sudoku**.  
✅ **Algorithmes de recherche** : Employé dans les techniques d’**optimisation combinatoire** et d’**intelligence artificielle**.  

---

## 🌐 Courbes de remplissage d’espace et mapping (Ex10, Ex11)  

### 🧩 Ce que c'est  
- Une **courbe de remplissage d’espace** est une **fonction qui transforme des coordonnées spatiales en une valeur unique** (`Ex10`).  
- Son **inverse** permet de **retrouver les coordonnées spatiales à partir de cette valeur unique** (`Ex11`).  
- Cela peut être réalisé via **l’interlacement de bits** (`Z-order curve`, `Hilbert curve`...).

### 🖥️ Utilité en informatique  
✅ **Bases de données spatiales** : Optimisation des **requêtes géospatiales** (ex: **Google Maps**).  
✅ **Compression et indexation** : Utilisé pour la **compression d’images**, **moteurs de recherche 3D** et **traitement d’images**.  
✅ **Calcul parallèle** : Accélère les algorithmes de **calcul distribué** en optimisant la répartition des données.  

---

## 🚀 Pourquoi ce projet est important ?  

Ces concepts sont **fondamentaux** pour les domaines suivants :  
- **Développement bas niveau** : programmation des **systèmes embarqués**, **drivers**, **GPU**.  
- **Optimisation d’algorithmes** : en **compilation**, **intelligence artificielle**, **big data**.  
- **Cryptographie et cybersécurité** : utilisation des **opérations logiques** et des **SAT solvers**.  
- **Bases de données et géométrie computationnelle** : optimisation de **requêtes SQL**, **indexation géospatiale**.  
- **Conception de circuits logiques et électronique** : utilisé dans le **design des microprocesseurs**.  

📌 **Ce projet te permet donc d’acquérir des compétences fondamentales** pour l’optimisation, l’algorithmique et l’informatique théorique. 🚀  
