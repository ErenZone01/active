# Active - Tiny Scanner

# Description

Active est un outil léger permettant de scanner les ports ouverts d'une machine en utilisant TCP ou UDP. Il est écrit en Python et permet d'effectuer des analyses ciblées sur une adresse IP donnée.

# Fonctionnalités

- Scan de ports en TCP ou UDP.

Possibilité de scanner un port unique ou une plage de ports.

Outil simple et rapide à utiliser.

# Installation

Assurez-vous d'avoir Python 3 installé sur votre machine.

- Clonez le projet :

```bash
    git clone https://learn.zone01dakar.sn/git/mandaw/active.git
    cd active 
```

# Utilisation

Pour voir tous les commandes :

```bash
    python3 tinyscanner.py --help
 ```

Lancer un scan en fonction du protocole et des ports désirés :

1. Scan d'un port spécifique en TCP

```bash 
    python3 tinyscanner.py -t 127.0.0.1 -p 80
```

2. Scan d'un port spécifique en UDP

```bash
    python3 tinyscanner.py -u 127.0.0.1 -p 5500
```

3. Scan d'une plage de ports en TCP

```bash
    python3 tinyscanner.py -t 127.0.0.1 -p 80-1000
```

4. Scan d'une plage de ports en UDP

```bash
    python3 tinyscanner.py -u 127.0.0.1 -p 80-1000
```

# Exemples de sortie

Si un port est ouvert, la sortie affichera :

[+] Port 80 open

Si un port est fermé ou filtré, la sortie affichera :

[-] Port 5500 close

# Avertissement ⚠️

Ce programme doit être utilisé uniquement sur des machines dont vous avez l'autorisation de scanner. L'analyse de ports non autorisée peut être illégale dans certains pays. Soyez responsables !

# Auteur

Matar Ndaw