# C File Watcher and Compiler

Un outil Python pour surveiller les fichiers `.c` dans un dossier spécifié et compiler automatiquement tout fichier modifié en utilisant le compilateur Visual Studio (`cl`). Ce projet est conçu pour faciliter le développement de fichiers C en automatisant le processus de compilation.

## Table des matières

- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Comment ça marche](#comment-ça-marche)
- [License](#license)

## Fonctionnalités

- Surveille les fichiers `.c` dans un dossier spécifié.
- Compile automatiquement les fichiers modifiés lors des sauvegardes (Ne pas mettre l'auto-save).
- Affiche des messages d'erreur détaillés en cas de compilation échouée.
- Ignore les fichiers vides ou nouvellement créés sans contenu.
- Prise en charge de l'exécution dans l'invite de commande de Visual Studio.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- **Python 3.6 ou supérieur**
- **Visual Studio avec le compilateur C/C++ (Pour avoir accès à la commande `cl`)** installé et configuré dans votre chemin système.

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/Khreight/CWaFiles.git
   cd CWaFiles
   ```

2. Installez les dépendances nécessaires :

   ```bash
   pip install watchdog
   ```

## Utilisation

1.a Ouvrez l'invite de commande développeur Visual Studio (`Developer Command Prompt for VS 2022`).

1.b Téléchargez son ZIP en cliquant sur `CODE` au-dessus de cette page. Une fois téléchargé, extrayer le ZIP dans Documents par exemple

2. Naviguez vers le dossier contenant le script :

   ```bash
   cd C:\Users\votre-utilisateur\Documents\My Projects\CWaFiles
   ```

3. Exécutez le script :

   ```bash
   python cwafiles.py
   ```

4. Lorsque le script vous demande, entrez le chemin du dossier à surveiller (par exemple, `C:\Users\votre-utilisateur\Documents\Test`).

5. Modifiez les fichiers `.c` dans ce dossier pour déclencher la compilation automatique.

## Comment ça marche

- Le script utilise la bibliothèque `watchdog` pour surveiller les modifications de fichiers.
- Lorsqu'un fichier `.c` est modifié, le script appelle le compilateur `cl` de Visual Studio pour compiler le fichier.
- Les erreurs de compilation sont capturées et affichées de manière lisible.
- Les fichiers vides ou nouvellement créés sans contenu ne déclenchent pas de compilation.

## License

Ce projet est sous la licence GNU GPLv3 - voir le fichier [LICENSE](LICENSE) pour plus de détails.
