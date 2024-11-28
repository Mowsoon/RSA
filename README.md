# Guide d'Installation et d'Exécution du Projet RSA

Ce projet contient un ensemble de scripts qui implémentent des algorithmes de chiffrement RSA, utilisant à la fois une implémentation maison (`rsa_simple`) et la bibliothèque `cryptography`. Ce guide explique comment préparer votre environnement pour faire fonctionner ce code.

## Prérequis

Avant d'exécuter le projet, assurez-vous que vous avez installé et configuré les éléments suivants.

### 1. Cloner le Répertoire

Tout d'abord, clonez ce projet dans votre environnement local :

```bash
git clone <URL-du-projet>
cd <nom-du-répertoire>
```

### 2. Créer un Environnement Virtuel (Optionnel mais recommandé)

Il est fortement recommandé d'utiliser un environnement virtuel pour éviter les conflits de versions avec d'autres projets. Pour créer un environnement virtuel :

```bash
python3 -m venv venv
source venv/bin/activate  # Sur Windows, utilisez venv\Scripts\activate
```

### 3. Installation des Dépendances

Ce projet utilise deux bibliothèques principales : `rsa_simple` (une implémentation simple de RSA) et `cryptography` (une bibliothèque plus avancée pour la cryptographie). Voici comment les installer.

#### Installation de `rsa_simple`

1. `rsa_simple` devrait être déjà inclus dans le projet sous forme de module Python. Si ce n'est pas le cas, vous pouvez l'installer via pip si nécessaire :

```bash
pip install rsa
```

#### Installation de `cryptography`

La bibliothèque **cryptography** nécessite l'installation de certains outils de développement C, car elle dépend d'extensions C pour des performances accrues. Voici les étapes pour l'installer correctement.

##### Sur Linux/MacOS

Avant d'installer la bibliothèque, assurez-vous d'avoir les outils nécessaires installés sur votre machine.

- **Sur Linux**, vous aurez besoin des paquets suivants :

```bash
sudo apt-get update
sudo apt-get install build-essential libssl-dev libffi-dev python3-dev
```

- **Sur MacOS**, vous devez vous assurer que **Xcode Command Line Tools** sont installés :

```bash
xcode-select --install
```

Ensuite, installez `cryptography` :

```bash
pip install cryptography
```

##### Sur Windows

Sous Windows, **cryptography** utilise des roues binaires (wheels) pour s'installer, donc vous aurez besoin de **Microsoft Visual C++ Build Tools**. Si vous ne l'avez pas encore installé, téléchargez-le depuis le site de Microsoft et suivez les instructions :  
[Microsoft Visual C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

Une fois les outils installés, vous pouvez installer la bibliothèque `cryptography` :

```bash
pip install cryptography
```

Si l'installation échoue, essayez de télécharger et d'installer les roues binaires adaptées à votre version de Python depuis [le site de PyPI](https://pypi.org/project/cryptography/#files).

### 4. Vérifier les Dépendances

Une fois les installations terminées, vous pouvez vérifier que toutes les bibliothèques sont correctement installées en exécutant :

```bash
pip list
```

Vous devriez voir les versions de `rsa` et `cryptography` listées parmi les packages installés.

### 5. Configuration de l'Environnement

Assurez-vous que votre environnement Python utilise bien l'interpréteur correct et que toutes les bibliothèques sont installées dans l'environnement actif (si vous utilisez un environnement virtuel).

### 6. Exécution du Code

Une fois que vous avez installé toutes les dépendances, vous pouvez exécuter les scripts de chiffrement/déchiffrement RSA. Assurez-vous d'avoir tous les fichiers nécessaires (par exemple, des fichiers texte à chiffrer ou décrypter) dans le répertoire approprié.

Pour exécuter un script Python, utilisez la commande suivante :

```bash
python <nom-du-script>.py
```

### 7. Dépannage

Si vous rencontrez des problèmes d'installation, voici quelques étapes de dépannage :

- Assurez-vous que vous avez bien installé les outils de développement C nécessaires pour **cryptography**, en particulier sur Linux/MacOS.
- Si vous rencontrez une erreur `ModuleNotFoundError` pour `cryptography` ou `rsa`, assurez-vous d'avoir activé l'environnement virtuel (si utilisé) et réessayez d'installer les dépendances.
- Pour des erreurs liées aux permissions sur Windows, essayez de réexécuter les commandes d'installation avec des privilèges d'administrateur.

### Conclusion

Une fois ces étapes complétées, vous devriez pouvoir exécuter le code du projet sans problème. Ce projet implémente des techniques cryptographiques de chiffrement/déchiffrement RSA en utilisant des bibliothèques Python simples et avancées, et il peut être utilisé pour tester des scénarios de sécurité sur des clés RSA générées aléatoirement.

---

Si vous avez d'autres questions ou des problèmes avec l'installation, n'hésitez pas à consulter la documentation officielle de `cryptography` ou `rsa` pour plus de détails.

