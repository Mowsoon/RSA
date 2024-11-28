# Rapport sur le TP RSA


## Partie 1 - Manipulation des grands nombres (début)

Dans cette première partie du TP, nous avons travaillé sur la représentation et les manipulations de grands nombres en binaire. L'objectif principal est de créer une structure de données, appelée `GrandNombre`, et de développer des fonctions basiques pour manipuler ces nombres, en vue d'implémenter le cryptage RSA. Cette classe inclut des fonctionnalités avancées comme les opérations arithmétiques (addition, soustraction, multiplication, division par deux), la gestion des signes, et des manipulations spécifiques aux grands nombres.

Nous avons choisit le language Python car nous avons d'abord commencé à faire le TP en langage C, mais avec le nombre de bits très conséquent, on a rapidement remarqué que le langage n'avais pas les capacités de stocker ces nombres et qu'il était donc impossible de poursuivre. Python n'a cependant aucun problème avec la manipulation de grands nombres et est performant. 

### Classe `GrandNombre`

#### Structure et initialisation

La classe `GrandNombre` permet de représenter un nombre entier avec :
- **Un signe** : 0 pour les nombres positifs, 1 pour les négatifs.
- **Une liste de bits** : chaque bit est un élément de type caractère (`'0'` ou `'1'`).
- **Une longueur des bits** : nombre total de bits nécessaires pour représenter le nombre.

##### Méthodes d'initialisation

**Initialisation à partir d'un entier :**
   ```python
   def __init__(self, nombre: int)
   ```
   Cette méthode permet de convertir un entier (positif ou négatif) en sa représentation binaire.

**Initialisation de GrandNombre à 0 ou 1 :**
   ```python
   def initialiser0()
   
   def initialiser1()
   ```
   Ces méthodes facilitent la création de nombres `0` ou `1`, souvent nécessaires dans les calculs binaires.

**Libération de la mémoire :**
   ```python
   def libererNombre(self)
   ```
   Libère explicitement la mémoire associée à l'objet GrandNombre en supprimant sa représentation binaire.


### Fonctionnalités principales

#### Opérations arithmétiques

##### Addition
La méthode `_addition_binaire` gère l'addition de deux nombres binaires, en prenant en compte les retenues et les signes des nombres. Elle supporte aussi l'addition avec des entiers classiques.

Exemple :
```python
a = GrandNombre(5)  # binaire : 101
b = GrandNombre(3)  # binaire : 011
resultat = a.additionner(b)
print(resultat)  # Résultat : 1000 (binaire de 8)
```

##### Soustraction
La méthode `_soustraction_binaire` effectue la soustraction en ajustant les signes et les retenues.

##### Multiplication
La méthode `multiplier` applique une multiplication par addition répétée et décalage avec l'appel à la méthode `_addition_binaire`.

Exemple :
```python
a = GrandNombre(6)  # binaire : 110
b = GrandNombre(3)  # binaire : 011
resultat = a.multiplier(b)
print(resultat)  # Résultat : 10010 (binaire de 18)
```

##### Multiplication par 2 
La méthode `multiplier_par_2` effectue une multiplication par 2 en ajoutant juste un bit 0 à droite

##### Division par 2
La méthode `diviserPar2` effectue une division en supprimant le dernier bit de la représentation binaire.

##### Réduction de 1
La méthode `reduireDe1` décrémente un nombre de 1 en modifiant directement les bits.


#### Opérations avancées

##### Exponentiation rapide
La méthode `exponentiationRapideSansModulo` calcule efficacement une puissance \(a^b\) en utilisant l'algorithme de l'exponentiation rapide. Elle gère également les grands nombres en entrée.

Exemple :
```python
base = GrandNombre(2)
exposant = 10
resultat = base.exponentiationRapideSansModulo(exposant)
resultat.afficher()  # Résultat : 10000000000 (binaire de 1024)
```

##### Modulo
La méthode `modulo` calcule le reste d'une division en appliquant une approximation des puissances de deux pour réduire les calculs.





## Partie 2 - Chiffrement et Déchiffrement

#### Génération d'un couple de clé RSA 
OpenSSL ne permettant pas de générer de couple de clé d'une taille de 100 bits, on a utilisé la bibliothèque python `rsa` et la fonction newkeys() pour obtenir ce couple de clé.
```python
import rsa
[...]
public_key, private_key = rsa.newkeys(taille)
[...]

```


### Création d’un message à chiffrer
Un message de maximum 12 octets (96 bits) a été écrit et sauvegardé dans un fichier texte. La fonction `sauvegarder_message` gère cette étape et vérifie que le message ne dépasse pas 12 octets :

```python
def sauvegarder_message(message: str, nom_fichier: str):
    if len(message) > TAILLEMSG:
        raise ValueError("Le message dépasse 12 octets (96 bits).")
    with open(nom_fichier, "w") as fichier:
        bits = ''.join(format(ord(c), '08b') for c in message)
        fichier.write(bits)
    print(f"Message sauvegardé dans {nom_fichier} sous forme binaire.")
```


### Chiffrement RSA m^e[n]
Le chiffrement du message \\( m \\) a été réalisé en calculant \\( m^e \mod n \\). Cela a été implémenté via la fonction d'exponentiation rapide, optimisée pour effectuer le calcul du modulo à chaque étape :

```python
def exponentielEtModulo(self, exposant, module):
    # Fonction utilisant l'exponentiation rapide et modulo pour chiffrer.
    [...]
```


### Déchiffrement RSA c^d[n]
Le déchiffrement du message \\( c \\) a été réalisé en calculant \\( c^d \mod n \\), en utilisant la même méthode que pour le chiffrement mais avec des paramètres différents. 


### Vérification du chiffrement et déchiffrement
Le message original a été chiffré et déchiffré. Les deux valeurs ont été comparées pour valider la correction du processus. Un exemple des fonctions utilisées :

**Chiffrement :**
```python
def chiffrer_fichier_rsa_int(nom_fichier, nom_fichier_sortie, cle, module):
    # Lecture du fichier et chiffrement RSA
    [...]
```

**Déchiffrement :**
```python
def traduire_fichier(nom_fichier: str):
    # Lecture du fichier chiffré et conversion en texte.
    [...]
```


### Chiffrement et déchiffrement d’un fichier de taille quelconque
Pour les fichiers plus grands, le contenu a été divisé en blocs de 12 octets et va être enregistré dans des fichiers différents, à l'aide d'un compteur on connait le nombre de blocs et on peut conserver l'ordre exact du texte original. Chaque bloc a été chiffré indépendamment mais à la suite puis déchiffré à la suite et concaténé dans une variable qui obtiendra le message original. Les fonctions suivantes ont été utilisées :

**Division en blocs et sauvegarde :**
```python
def sauvegarder_long_message(message: str, nom_fichier: str):
    numero = 1
    for position in range(0, len(message), 12):
        bloc = message[position:position + 12]
        sauvegarder_message(bloc, nom_fichier + str(numero) + ".txt")
        numero += 1
    return numero
```

**Chiffrement de plusieurs blocs :**
```python
def chiffrer_long_message_int(prefixe_entre, suffixe_sortie, numero, cle, module):
    for i in range(1, numero):
        chiffrer_fichier_rsa_int(prefixe_entre + str(i) + ".txt", suffixe_sortie + str(i) + ".txt", cle, module)
```

**Réassemblage après déchiffrement :**
```python
def traduire_long_message(numero: int, nom_fichier: str):
    message = ''
    for i in range(1, numero):
        message += renvoyer_traduction(nom_fichier + str(i) + ".txt")
    print(f"\n------------------------------------------\n\nLe message est :\n{message}")
```

Le programme a été testé avec un message simple ainsi qu'avec des fichiers de plus grande taille. À chaque étape, les messages originaux ont été restaurés avec succès après chiffrement et déchiffrement.

```plaintext
Message original : "Bonjour RSA !"
Message déchiffré : "Bonjour RSA !"
```




## Partie 3 - Manipulation des grands nombres (fin)

### Calcul de l’inverse modulo
Nous avons implémenté l'algorithme d’Euclide étendu pour calculer l’inverse modulaire \( a^{-1} \mod b \).

**Code :**
```python
def inverserAvecModulo(self, other):
    x1, y1, r1 = GrandNombre(1), GrandNombre(0), self
    x2, y2, r2 = GrandNombre(0), GrandNombre(1), other
    while r2 != 0:
        q = r1.quotient(r2)
        x1, x2 = x2, x1.soustraire(q.multiplier(x2))
        y1, y2 = y2, y1.soustraire(q.multiplier(y2))
        r1, r2 = r2, r1.modulo(r2)
    return x1.modulo(other)
```

Dans cet algorithme :

Les variables 𝑥1, 𝑦1, 𝑥2, 𝑦2 servent à garder une trace des coefficients intermédiaires.
Les divisions successives permettent de réduire les restes 𝑟1 et 𝑟2 jusqu’à atteindre 0, tout en construisant les coefficients 𝑥 et 𝑦.


---

### Détection de co-primalité
En utilisant l’algorithme d’Euclide, nous avons déterminé si deux nombres \( a \) et \( b \) sont premiers entre eux (\( \text{pgcd}(a, b) = 1 \)).

**Code :**
```python
def estPremierAvec(self, other):
    return self.pgcd(other).bits == ['1']

def pgcd(self, autre):
        
        # Si l'un des deux nombres est nul, l'autre est le PGCD
        if self.binaire == '0':
            return autre
        if autre.binaire == '0':
            return self

        # Créer des copies de self et autre pour éviter de modifier les objets d'origine
        a = lire_binaire(self.binaire)
        b = lire_binaire(autre.binaire)

        while b.binaire != '0':  # Tant que b n'est pas nul
            # On effectue le modulo pour obtenir a % b
            a = a.modulo(b)
            # Puis on échange les valeurs de a et b
            a, b = b, a

        return a  # Lorsque b devient nul, a est le PGCD

```
L’algorithme repose sur le calcul du pgcd. Si celui-ci est égal à 1, alors les deux nombres sont premiers entre eux.


---

### Génération de nombres premiers de Mersenne
Les nombres premiers de Mersenne sont générés selon la formule \( M_n = 2^n - 1 \), où \( n \) est premier. Nous avons utilisé le test de primalité de Lucas-Lehmer sur des nombres entiers et non dans notre format GrandNombres qui est du binaire car il était beaucoup trop long de faire ces tests qui sont également déjà long avec un nombre de Mersenne entier s'approchant de 700.

**Code :**
```python
def testLucasLehmer(p):
    s = 4
    M_p = (1 << p) - 1
    for _ in range(p - 2):
        s = (s * s - 2) % M_p
    return s == 0

def nombrePremierMersenne():
    while True:
        n = random.randint(80, 700)
        if estPremier(n) and testLucasLehmer(n):
            return GrandNombre((1 << n) - 1)
```



## Partie 4 - Création des clés

### Génération des clés RSA

On commence par générer p et q grâce à la fonction nombrePremierMersenne(), puis on s'assure qu'ils sont différents, s'ils sont égaux alors on va générer un autre nombre q. 
Dans la fonction on a défini un e constant égal à 65537 pour des raisons de performances à nouveau et car il est largement utilisé en RSA. S'il ne convient pas on part alors de trois et on cherche un autre nombre premier avec phi. 

**Implémentation :**
```python
def creationCleRSA(min_val=80, max_val=700):
    # Générer deux nombres premiers de Mersenne distincts
    p = nombrePremierMersenne(min_val, max_val)
    q = nombrePremierMersenne(min_val, max_val)
    while q.comparer(p):  # Assurer que p et q sont distincts
        q = nombrePremierMersenne(min_val, max_val)

    # Calcul de n = p * q
    n = p.multiplier(q)
    # Calcul de φ(n) = (p-1) * (q-1)
    phi = (p.soustraire(initialiser1())).multiplier(q.soustraire(initialiser1()))

    # Trouver e, tel que 1 < e < φ(n) et pgcd(e, φ(n)) = 1
    e = GrandNombre(65537)  # Choix standard pour e dans RSA
    if not e.estPremierAvec(phi):  # Si ne convient pas, en générer un autre
        e = GrandNombre(3)
        add = GrandNombre(2)
        while not e.estPremierAvec(phi):
            e = e.ajouter(add)  # Tester les entiers impairs croissants

    # Calcul de d, l'inverse modulaire de e modulo φ(n)
    d = e.inverse_modulaire(phi)

    # Retourner la clé publique (e, n) et la clé privée (d, n)
    return (e, n), (d, n)
```

### Tests de performance

### Analyse de la taille moyenne des nombres premiers de Mersenne

Pour les tests on a notamment joué sur la taille de l'intervalle pour le choix du nombre de Mersenne qui est la première source d'impact sur les performances d'après nos observations.
On a répété les opérations 1000 fois pour chaque intervalle différent. 

**Résultats des tests de taille:**

1000 fois taille clé:
Mersenne(80,120) 
Taille moyenne de n sur 1000 répétitions : 196.00 bits
Mersenne(80,200)
Taille moyenne de n sur 1000 répétitions : 215.02 bits
Mersenne(80,300)
Taille moyenne de n sur 1000 répétitions : 214.58 bits
Mersenne(80,400)
Taille moyenne de n sur 1000 répétitions : 215.68 bits
Mersenne(80,500)
Taille moyenne de n sur 1000 répétitions : 214.94 bits
Mersenne(80,600)
Taille moyenne de n sur 1000 répétitions : 421.00 bits
Mersenne(80, 700) 
Taille moyenne de n sur 1000 répétitions : 580.18 bits


On remarque que la différence entre les intervalles [80, 200] et [80, 500] en termes de performance ou de résultats n'est pas significative. Cela semble être lié à la répartition des nombres premiers de Mersenne dans ces plages ou qu'ils n'ont pas d'impact significatif sur la taille moyenne des clés.
Cependant L'augmentation à 421 bits pour [80, 600] marque une rupture. Cette plage inclut des nombres premiers de Mersenne beaucoup plus grands, ce qui génère des clés RSA significativement plus grandes.
Il est également intéressant de noter que la taille des clés générées tourne autour de 200 bits en moyenne. Pour cette raison, les comparaisons de performances seront effectuées en prenant une clé de cette taille comme référence. 
Enfin, il est important de souligner qu'il n'est pas possible de réduire davantage la taille des intervalles, car cela entraînerait l'absence de nombres premiers de Mersenne à l'intérieur de ces plages.



### Analyse du temps de génération des clés RSA

On a ensuite réalisé des tests de performance sur la génération des clés.

**Résultat des tests :**

TEST GENERATION CLE:
1000 fois Génération:
RSA(50)
Temps moyen pour générer une clé avec la bibliothèque RSA : 0.000152 secondes
RSA(100) 
Temps moyen pour générer une clé avec la bibliothèque RSA : 0.000540 secondes
RSA(200)
Temps moyen pour générer une clé avec la bibliothèque RSA : 0.002226 secondes
RSA(500)
Temps moyen pour générer une clé avec la bibliothèque RSA : 0.019777 secondes
RSA(1000)
Temps moyen pour générer une clé avec la bibliothèque RSA : 0.201669 secondes

Mersenne(80,120) 
Temps moyen pour générer une clé avec vos les fonctions : 0.137468 secondes
Mersenne(80,200)
Temps moyen pour générer une clé avec les fonctions : 0.151857 secondes
Mersenne(80,300)
Temps moyen pour générer une clé avec les fonctions : 0.180199 secondes
Mersenne(80,400)
Temps moyen pour générer une clé avec les fonctions : 0.161654 secondes
Mersenne(80,500)
Temps moyen pour générer une clé avec les fonctions : 0.205951 secondes
Mersenne(80,600)
Temps moyen pour générer une clé avec les fonctions : 1.152253 secondes
Mersenne(80,700) 
Temps moyen pour générer une clé avec les fonctions : 1.707513 secondes

On peut remarquer qu'en fonction de la taille de la clé la vitesse de création ralentit de façon significative. Si on compare RSA(200) avec les Mersenne qui font des clé de taille proche on remarque que RSA est bien plus rapide :
- 0.002226 secondes pour RSA(200)
- 0.137468 à  0.151857 secondes pour nos fonctions Mersenne(80,120) et Mersenne(80,200) 
Donc la bibliothèque RSA est beaucoup plus rapide que l'approche basée sur les nombres de Mersenne, particulièrement pour des tailles de clés petites à moyennes (jusqu'à 500 bits).
Comme on a vu précédemment avec les tailles de clé et également ici avec les temps de génération, les intervales 300:400:500 ne servent à rien car elles generent des clé trop similaires à 200.
Donc pour comparer, générer une clé de taille 200 avec nos fonctions équivaut à peu près à génerer une clé de taille 1000 avec RSA.

Ce test montre comment les performances se dégradent avec l’augmentation de la taille des clés, illustrant le compromis entre sécurité et efficacité.



### Analyse du temps de cryptage et de cryptage

Enfin on a réalisé des tests de performances sur le cryptage et le décryptage d'un texte en fonction de la taille de la clé ainsi que la méthode utilisée pour génrer la clé.

**Résultat des tests :**

10 Cryptage Méthode TP
RSA(100):
Temps moyen de cryptage : 2.025841 secondes
Temps moyen de décryptage : 16.836937 secondes
RSA(200):
Temps moyen de cryptage : 6.938620 secondes
Temps moyen de décryptage : 132.023062 secondes
RSA(300):
trop long

Mersenne(80,120):
Temps moyen de cryptage : 3.281159 secondes
Temps moyen de décryptage : 62.511922 secondes
Mersenne(80,200):
Temps moyen de cryptage : 4.139170 secondes
Temps moyen de décryptage : 80.542269 secondes

1000 Cryptage avec la bibliotheque cryptography
taille: 1024
Temps moyen de cryptage : 0.000078 secondes
Temps moyen de décryptage : 0.000534 secondes
taille: 2048
Temps moyen de cryptage : 0.000158 secondes
Temps moyen de décryptage : 0.001550 secondes


Tout d'abord on remarque que le décryptage RSA est beaucoup plus coûteux en temps que le cryptage, ce qui reflète la nature computationnellement intensive de l'opération de décryptage (inversion exponentielle modulaire) même si ici ce n'est que quelques secondes.
De plus, avec des tailles de clés croissantes (100, 200, 300 bits), le temps moyen de cryptage et surtout de décryptage augmente considérablement.

Si on regarde de plus près les résultats des deux méthodes du tp, les temps de cryptage et de décryptage sont plus faibles pour la méthode Mersenne que ceux de RSA pour des tailles de clés équivalentes, par exemple, pour une clé de 200 bits, le décryptage Mersenne est 1.64 fois plus rapide que RSA.
On peut en déduire que la méthode du TP, Mersenne, est plus rapide à taille de clé équivalente pour le cryptage et décryptage que la méthode de la bibliothèque rsa que l'on a importé et utilisé. 
En revanche si on utilise la bibliothèque cryptography pour générer chiffrer puis déchiffrer le message avec les tailles de clé RSA normal soir 1024 et 2048, la vitesse est absolument incomparable. Le temps de cryptage et de décryptage est infime comparé à ceux des méthodes précédentes (environ 10,000 fois plus rapides pour des clés de 1024 bits).
Ces performances démontrent la puissance des optimisations algorithmiques et des implémentations basées sur du matériel et des bibliothèques modernes.