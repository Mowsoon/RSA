import random
class GrandNombre:
    def __init__(self, entier):
        if not isinstance(entier, int):
            raise ValueError("L'argument doit être un entier.")
        self.binaire = bin(entier)[2:] if entier >= 0 else '-' + bin(-entier)[2:]

    def __repr__(self):
        if self.binaire is None:
            raise ValueError("Le nombre a été libéré.")
        return f"binaire = {self.binaire}"

    def libererNombre(self):
        """
        Libère explicitement la mémoire associée à l'objet GrandNombre en
        supprimant sa représentation binaire.
        """
        self.binaire = None

    def comparer(self, autre):
        """
        Compare l'objet actuel avec un autre GrandNombre pour vérifier s'ils sont égaux.

        :param autre: Un autre objet GrandNombre à comparer.
        :return: True si les objets sont égaux, False sinon.
        """
        if not isinstance(autre, GrandNombre):
            raise ValueError("L'argument doit être une instance de GrandNombre.")

        return self.binaire == autre.binaire

    def estPlusGrandNombre(self, autre):
        """
        Détermine si le nombre courant (self) est plus grand ou égal à l'autre.

        :param autre: Un autre objet GrandNombre à comparer.
        :return: True si self >= autre, False sinon.
        """
        if not isinstance(autre, GrandNombre):
            raise ValueError("L'argument doit être une instance de GrandNombre.")

        if self.binaire[0] == '-' == autre.binaire[0]:
            return self.binaire <= autre.binaire

        return int(self.binaire) >= int(autre.binaire)

    def estPlusGrandNombreABS(self, autre):
        """
        Détermine si le nombre courant (self) est plus grand ou égal à l'autre.

        :param autre: Un autre objet GrandNombre à comparer.
        :return: True si self >= autre, False sinon.
        """

        if not isinstance(autre, GrandNombre):
            raise ValueError("L'argument doit être une instance de GrandNombre.")

        if self.binaire[0] == '-':
            self_binaire = self.binaire[1:]
        else:
            self_binaire = self.binaire

        if autre.binaire[0] == '-':
            autre_binaire = autre.binaire[1:]
        else:
            autre_binaire = autre.binaire

        return int(self_binaire) >= int(autre_binaire)

    def estPair(self):
        """
        Détermine si l'objet GrandNombre est pair en regardant le dernier bit de sa représentation binaire.

        :return: True si le nombre est pair, False si le nombre est impair.
        """
        if self.binaire is None:
            raise ValueError("La valeur binaire est absente.")

        return self.binaire[-1] == '0'

    def diviserPar2(self):
        """
        Divise l'objet GrandNombre par 2 en modifiant directement sa valeur binaire.
        """
        #si l'entier est négait
        if self.binaire[0] == '-':
            self.binaire = self.binaire[1:]
            if len(self.binaire) > 1:
                # Si le bit n'est pas -1
                self.binaire = self.binaire[:-1]
                self.binaire = '-' + self.binaire
            else:
                # Si l'entier est -1, il devient 0 après la division par 2
                self.binaire = '0'
        # Supprime le dernier bit de la représentation binaire
        elif len(self.binaire) > 1:
            # Si le bit n'est pas 0 ou -1
            self.binaire = self.binaire[:-1]
        else:
            # Si l'entier est 0 ou 1, il devient 0 après la division par 2
            self.binaire = '0'

    def reduireDe1(self):
        """
        Réduit l'objet GrandNombre de 1, en manipulant directement sa valeur binaire.
        Si le nombre est négatif, cela revient à soustraire 1 à sa valeur binaire.
        """
        if self.binaire is None:
            raise ValueError("La valeur binaire est absente.")
        if self.binaire[0] == '0':
            self.binaire = '-1'
        elif self.binaire[0] == '1' and len(self.binaire) == 1:
            self.binaire = '0'
        elif self.binaire[0] == '-':  # Si le nombre est négatif
            # On parcourt la chaîne binaire à l'envers (de la fin vers le début)
            # et on effectue l'addition de 1 en manipulant les bits.
            self.binaire = self.binaire[1:]  # On retire le signe '-'
            binaire_list = list(self.binaire)  # Conversion en liste pour manipulation
            # On part du dernier bit et on effectue l'addition de 1
            for i in range(len(binaire_list) - 1, 0, -1):
                if binaire_list[i] == '0':
                    binaire_list[i] = '1'
                    break
                binaire_list[i] = '0'
            # Reconvertir la liste en chaîne de caractères et rajouter le signe '-'
            self.binaire = '-' + ''.join(binaire_list)
        else:  # Si le nombre est positif
            self.binaire = list(self.binaire)
            i = len(self.binaire) - 1
            while self.binaire[i] == '0':  # On cherche le premier '1'
                self.binaire[i] = '1'  # On remet le bit à '1'
                i -= 1
            self.binaire[i] = '0'
            self.binaire = ''.join(self.binaire)
            # Si on arrive à i == 0, on supprime le bit le plus à gauche
            if i == 0:
                self.binaire = self.binaire[1:]

    def multiplierPar2(self):
        """
        Multiplie l'objet GrandNombre par 2, en manipulant directement sa valeur binaire.
        Si le nombre est négatif, le signe '-' est conservé.
        """
        if self.binaire is None:
            raise ValueError("La valeur binaire est absente.")

        if self.binaire != '0':  # Si le nombre n'est pas 0
            self.binaire += '0'


    def ajouter(self, autre):
        """
        Ajoute deux objets GrandNombre (self et autre) en tenant compte des signes
        en parcourant les bits.

        :param autre: Un autre objet GrandNombre à additionner à self.
        :return: Un nouveau GrandNombre représentant la somme de self et autre.
        """
        if not isinstance(autre, GrandNombre):
            raise ValueError("L'argument doit être une instance de GrandNombre.")

        if self.binaire == '0':
            return autre
        if autre.binaire == '0':
            return self

        # Si les deux nombres ont le même signe
        if self.binaire[0] == autre.binaire[0]:
            # Si les deux sont négatifs, on additionne les valeurs absolues avec retenue
            if self.binaire[0] == '-':
                binaire_self = self.binaire[1:]
                binaire_autre = autre.binaire[1:]
                resultat_binaire = _addition_binaire(binaire_self, binaire_autre)
                return lire_binaire('-' + resultat_binaire)
            else:
                # Si les deux sont positifs, on additionne normalement avec retenue
                binaire_self = self.binaire
                binaire_autre = autre.binaire
                resultat_binaire = _addition_binaire(binaire_self, binaire_autre)

                return lire_binaire(resultat_binaire)

        if self.binaire[0] == '-':
            binaire_self = self.binaire[1:]
            binaire_autre = autre.binaire
            if self.estPlusGrandNombreABS(autre):
                resultat_binaire = _soustraction_binaire(binaire_self, binaire_autre)
                return lire_binaire('-' + resultat_binaire)
            resultat_binaire = _soustraction_binaire(binaire_autre, binaire_self)
            return lire_binaire(resultat_binaire)

        binaire_self = self.binaire
        binaire_autre = autre.binaire[1:]
        if self.estPlusGrandNombreABS(autre):
            resultat_binaire = _soustraction_binaire(binaire_self, binaire_autre)
            return lire_binaire(resultat_binaire)
        resultat_binaire = _soustraction_binaire(binaire_autre, binaire_self)
        return lire_binaire('-' + resultat_binaire)

    def multiplier(self, autre):
        """
        Multiplie deux objets GrandNombre (self et autre) en utilisant une méthode de multiplication binaire.

        :param autre: Un autre objet GrandNombre à multiplier avec self.
        :return: Un nouveau GrandNombre représentant le produit de self et autre.
        """
        if not isinstance(autre, GrandNombre):
            raise ValueError("L'argument doit être une instance de GrandNombre.")

        # On garde les signes pour la multiplication
        signe_resultat = ''
        if self.binaire[0] == '-' and autre.binaire[0] == '-':
            signe_resultat = ''
        elif self.binaire[0] == '-' or autre.binaire[0] == '-':
            signe_resultat = '-'

        # On enlève les signes pour faire la multiplication sur les valeurs absolues
        binaire_self = self.binaire[1:] if self.binaire[0] == '-' else self.binaire
        binaire_autre = autre.binaire[1:] if autre.binaire[0] == '-' else autre.binaire

        # Effectuer la multiplication bit par bit (méthode classique)
        produit_binaire = '0'  # Initialisation du produit binaire

        # On parcourt binaire_autre de droite à gauche
        for i in range(len(binaire_autre) - 1, -1, -1):
            if binaire_autre[i] == '1':
                produit_binaire = _addition_binaire(produit_binaire, binaire_self + '0' * (len(binaire_autre) - 1 - i))

        # Ajouter le signe du résultat si nécessaire
        return lire_binaire(signe_resultat + produit_binaire)

    def exponentiationRapideSansModulo(self, autre):
        """
        Calcule self^autre en utilisant l'exponentiation rapide.

        :param autre: Un autre objet GrandNombre représentant l'exposant b.
        :return: Un nouveau GrandNombre représentant le résultat de self^autre.
        """
        if not isinstance(autre, GrandNombre) or autre.binaire[0] == '-':
            raise ValueError("L'argument doit être une instance de GrandNombre positive.")

        resultat = initialiser1()

        # Si l'exposant est zéro, tout nombre élevé à la puissance zéro est 1.
        if autre.binaire == '0':
            return resultat

        # Création des copies pour éviter la modification de self et autre
        base = lire_binaire(self.binaire)  # Copie de self
        exposant = lire_binaire(autre.binaire)  # Copie de autre
        while not exposant.binaire == '0':
            if not exposant.estPair():
                resultat = resultat.multiplier(base)
            base = base.multiplier(base)
            exposant.diviserPar2()

        return resultat

    def soustraire(self, autre):
        """
        Soustrait un nombre (autre) à self, c'est-à-dire calcule self - autre.
        Cette fonction utilise la méthode ajouter en inversant le signe de autre.

        :param autre: Un autre objet GrandNombre à soustraire de self.
        :return: Un nouveau GrandNombre représentant la différence self - autre.
        """
        if not isinstance(autre, GrandNombre):
            raise ValueError("L'argument doit être une instance de GrandNombre.")

        # Inverser le signe de l'autre nombre (changer le signe de b)
        autre_inverti = lire_binaire(autre.binaire)
        if autre_inverti.binaire[0] == '-':
            autre_inverti.binaire = autre_inverti.binaire[1:]  # On retire le signe -
        else:
            autre_inverti.binaire = '-' + autre_inverti.binaire  # On met un signe -

        # Utiliser la méthode ajouter pour additionner self et l'autre nombre avec le signe inversé
        return self.ajouter(autre_inverti)

    def approximer(self):
        if self.binaire.count('1') == 1:
            if self.binaire != '1':
                return self
        return lire_binaire('1' + '0' * len(self.binaire))

    def modulo(self, module):
        """
        Calcule self modulo n en utilisant une approximation du quotient et des soustractions successives.
        
        :param module: Un autre objet GrandNombre représentant le diviseur.
        :return: Un nouveau GrandNombre représentant le reste de self / n.
        """
        if not isinstance(module, GrandNombre) or module.binaire[0] == '-':
            raise ValueError("L'argument doit être une instance de GrandNombre positive.")

        if module.binaire == '0':  # Modulo par zéro n'est pas défini
            raise ValueError("Le diviseur ne peut pas être zéro.")

        resultat = lire_binaire(self.binaire)
        puissance = GrandNombre(2)
        while resultat.binaire[0] == "-":
            resultat = resultat.ajouter(module)

        while resultat.estPlusGrandNombre(module):
            len_res = len(resultat.binaire)
            approximation = module.approximer()
            ecart = len_res - len(approximation.binaire)
            if ecart < 0:
                ecart = initialiser0()
            else:
                ecart = GrandNombre(ecart)

            multiple = puissance.exponentiationRapideSansModulo(ecart)
            retrait = lire_binaire(module.binaire).multiplier(multiple)

            resultat = resultat.soustraire(retrait)
        return resultat

    def exponentielEtModulo(self, exposant, modulo):
        """
        Calcule (self ^ exposant) % modulo efficacement en utilisant
        l'exponentiation modulaire rapide.

        :param exposant: GrandNombre représentant l'exposant.
        :param modulo: GrandNombre représentant le modulo.
        :return: Un GrandNombre représentant le résultat.
        """
        if not isinstance(exposant, GrandNombre) or not isinstance(modulo, GrandNombre):
            raise ValueError("Les arguments doivent être des instances de GrandNombre.")

        # Résultat initial
        resultat = initialiser1()
        base = self.modulo(modulo)  # Réduit immédiatement la base modulo
        exposant_binaire = exposant.binaire

        # Parcours de l'exposant en binaire
        for bit in exposant_binaire:
            resultat = resultat.multiplier(resultat).modulo(modulo)  # Carré
            if bit == '1':  # Si le bit courant est 1, multiplier par la base
                resultat = resultat.multiplier(base).modulo(modulo)

        return resultat

    def pgcd(self, autre):
        """
        Calcule le PGCD (Plus Grand Commun Diviseur) de self et autre en utilisant l'algorithme d'Euclide.

        :param autre: Un autre objet GrandNombre représentant l'autre nombre.
        :return: Un nouvel objet GrandNombre représentant le PGCD de self et autre.
        """
        if not isinstance(autre, GrandNombre):
            raise ValueError("L'argument doit être une instance de GrandNombre.")

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

    def estPremierAvec(self, autre):
        if self.pgcd(autre).binaire == '1':
            return True
        return False

    def diviser(self, autre):
        if not isinstance(autre, GrandNombre):
            raise ValueError("L'argument doit être une instance de GrandNombre.")

        if autre.binaire == '0':
            raise ValueError("Division par zéro.")

        # Vérification des signes et gestion du signe du quotient
        is_negative = False
        if self.binaire[0] != autre.binaire[0]:  # Si les signes sont différents
            is_negative = True

        dividende = lire_binaire(self.binaire.lstrip('-'))  # Retirer le signe si présent
        diviseur = lire_binaire(autre.binaire.lstrip('-'))

        quotient = initialiser0()
        puissance = GrandNombre(2)
        ecart = len(dividende.binaire) - len(diviseur.binaire)

        while ecart >= 0:
            # Calcul de la puissance de 2 (décalage à gauche)
            decalage = puissance.exponentiationRapideSansModulo(GrandNombre(ecart))
            diviseur_decaler = diviseur.multiplier(decalage)

            if dividende.estPlusGrandNombre(diviseur_decaler):
                dividende = dividende.soustraire(diviseur_decaler)
                quotient = quotient.ajouter(initialiser1().multiplier(decalage))

            ecart -= 1

        # Gestion du signe final du quotient
        if is_negative:
            quotient.binaire = '-' + quotient.binaire

        return quotient

    def inverse_modulaire(self, autre):
        """
        Trouve l'inverse modulaire de self modulo autre, avec une optimisation pour réduire la charge CPU.

        :param autre: Un autre objet GrandNombre représentant le modulo r1.
        :return: Un nouvel objet GrandNombre représentant l'inverse modulaire de self modulo autre.
        :raises ValueError: Si l'inverse modulaire r1'existe pas.
        """
        # Vérification des arguments
        if not isinstance(autre, GrandNombre):
            raise ValueError("L'argument doit être une instance de GrandNombre.")

        if autre.binaire == '0':
            raise ValueError("Division par zéro r1'est pas permise.")

        # Vérifier si l'inverse existe
        if not self.estPremierAvec(autre):
            raise ValueError("L'inverse modulaire r1'existe pas car r0 et r1 ne sont pas premiers entre eux.")

        # Réduction initiale de self modulo autre
        r0 = self.modulo(autre)  # On réduit self dans la plage (0, autre)
        r1 = lire_binaire(autre.binaire)  # Copie de autre (le modulo)

        # Initialisation des coefficients
        x0, y0 = GrandNombre(1), GrandNombre(0)
        x1, y1 = GrandNombre(0), GrandNombre(1)

        # Algorithme d'Euclide étendu
        while r1.binaire != '0':
            q = r0.diviser(r1)

            r0, r1 = r1, r0.soustraire(q.multiplier(r1))
            x0, x1 = x1, x0.soustraire(q.multiplier(x1))
            y0, y1 = y1, y0.soustraire(q.multiplier(y1))

        # Si le pgcd est 1, alors x0 est l'inverse modulaire
        if x0.binaire[0] == '-':
            x0 = x0.ajouter(autre)  # On ajuste pour qu'il soit positif

        return x0


def lire_binaire(chaine):
    if not isinstance(chaine, str):
        raise ValueError("L'argument doit être une chaîne de caractères.")
    if chaine[0] == '-':
        if not all(c in '01' for c in chaine[1:]):
            raise ValueError("La chaîne binaire est invalide.")
    else:
        if not all(c in '01' for c in chaine):
            raise ValueError("La chaîne binaire est invalide.")
    return GrandNombre(int(chaine, 2))


def initialiser0():
    """
    Crée un objet GrandNombre représentant le nombre 0.
    """
    return GrandNombre(0)


def initialiser1():
    """
    Crée un objet GrandNombre représentant le nombre 1.
    """
    return GrandNombre(1)


def harmoniser(x, y):
    max_len = max(len(x), len(y))
    binaire1 = x.zfill(max_len)
    binaire2 = y.zfill(max_len)
    return binaire1, binaire2


def _addition_binaire(binaire1, binaire2):
    b1, b2 = harmoniser(binaire1, binaire2)

    carry = 0
    result = []
    max_len = len(b1)

    # On additionne les bits de droite à gauche
    for i in range(max_len - 1, -1, -1):
        bit1 = int(b1[i])
        bit2 = int(b2[i])
        total = bit1 + bit2 + carry

        if total == 0:
            result.append('0')
            carry = 0
        elif total == 1:
            result.append('1')
            carry = 0
        elif total == 2:
            result.append('0')
            carry = 1
        else:  # total == 3
            result.append('1')
            carry = 1

    # Si une retenue reste, on l'ajoute à la fin
    if carry:
        result.append('1')
    # On renverse la liste pour avoir le résultat final
    result.reverse()
    # Convertir la liste en chaîne de caractères et la retourner
    return ''.join(result)


def _soustraction_binaire(binaire1, binaire2):
    b1, b2 = harmoniser(binaire1, binaire2)

    borrow = 0  # Emprunt initial est 0
    result = []
    max_len = len(b1)
    # Soustraction des bits de droite à gauche
    for i in range(max_len - 1, -1, -1):
        bit1 = int(b1[i])
        bit2 = int(b2[i])
        diff = bit1 - bit2 - borrow
        if diff == 0:
            result.append('0')
            borrow = 0
        elif diff == 1:
            result.append('1')
            borrow = 0
        elif diff == -1:
            result.append('1')
            borrow = 1
        else:  # diff == -2
            result.append('0')
            borrow = 1

    # Retourner 0 si le résultat est vide (cas où les deux nombres sont opposés)
    result_str = ''.join(result[::-1]).lstrip('0')
    return result_str if result_str else '0'


def est_premier(n, iterations=30):
    """
    Vérifie si un nombre est premier en utilisant le test de Miller-Rabin.

    :param n: Entier à tester.
    :param iterations: Nombre d'itérations du test de Miller-Rabin.
    :return: True si n est probablement premier, False sinon.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Écriture de n-1 sous la forme d * 2^s
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # Test de Miller-Rabin
    for _ in range(iterations):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)  # a^d % n
        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def nombre_premier_aleatoire(min_val=80, max_val=700):
    """
    Génère un nombre premier aléatoire entre min_val et max_val.

    :param min_val: Borne inférieure.
    :param max_val: Borne supérieure.
    :return: Un entier premier aléatoire.
    """
    while True:
        candidat = random.randint(min_val, max_val)
        if est_premier(candidat):
            return candidat


def nombrePremierMersenne(min_val, max_val):
    """
    Génère un nombre premier de Mersenne sous la forme d'un GrandNombre.

    :return: Un GrandNombre représentant un nombre premier de Mersenne.
    """
    while True:
        # Générer un n premier aléatoire
        n = nombre_premier_aleatoire(min_val, max_val)

        # Calculer 2^n - 1
        mersenne = (1 << n) - 1  # Décalage binaire équivalent à 2^n - 1

        # Vérifier si M_n est premier
        if est_premier(mersenne):
            # Convertir en GrandNombre et retourner
            return GrandNombre(mersenne)


def creationCleRSA(min_val=80, max_val=700):
    """
    Génère une paire de clés RSA en utilisant des nombres premiers de Mersenne.

    :return: Une paire de clés publiques (e, n) et privées (d, n), sous forme de tuples.
    """

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





