import random
class GrandNombre:
    def __init__(self, nombre: int):
        self.signe = 0 if nombre >= 0 else 1
        nombre = abs(nombre)
        self.longueur_bits = len(bin(nombre)) - 2
        self.bits = list(bin(nombre)[2:].zfill(self.longueur_bits))
        if len(self.bits) > self.longueur_bits:
            raise ValueError(f"Le nombre depasse la longueur : {self.longueur_bits}")

    @classmethod
    def initialiser0(cls):
        return cls(0)

    @classmethod
    def initialiser1(cls):
        return cls(1)

    @classmethod
    def initialiser(cls, bit_string, signe=0):
        if not isinstance(bit_string, str):
            raise ValueError("L'entrée doit être une chaîne de caractères.")

        if not all(bit in '01' for bit in bit_string):
            raise ValueError("La chaîne de caractères doit être composée uniquement de '0' et '1'.")

        instance = cls(0)
        instance.bits = list(bit_string)
        instance.longueur_bits = len(instance.bits)
        instance.signe = signe
        return instance

    @classmethod
    def instancier(cls, bits, signe):
        if not isinstance(bits, list) or not all(bit in ['0', '1'] for bit in bits):
            raise ValueError("Les bits doivent être une liste composée uniquement de '0' et '1'.")
        if signe not in [0, 1]:
            raise ValueError("Le signe doit être 0 (positif) ou 1 (négatif).")
        if len(bits) == 0:
            raise ValueError("La liste des bits ne peut pas être vide.")

        instance = cls(0)
        instance.bits = bits[:]  # Copie des bits pour éviter les références externes.
        instance.longueur_bits = len(bits)
        instance.signe = signe
        return instance

    def libererNombre(self):
        self.bits = None
        self.longueur_bits = 0
        self.signe = -1

    def en_entier(self):
        valeur = int(''.join(self.bits), 2)
        return -valeur if self.signe == 1 else valeur

    def afficher(self):
        if self.bits is None:
            raise ValueError("Le nombre est libere")
        else:
            signe = '-' if self.signe == 1 else ''
            representation = ''.join(self.bits)
            print(f"Représentation binaire :\n{signe}{representation}")

    def harmoniser(self, other):
        max_len = max(self.longueur_bits, other.longueur_bits)

        self.bits = ['0'] * (max_len - len(self.bits)) + self.bits
        other.bits = ['0'] * (max_len - len(other.bits)) + other.bits

        self.longueur_bits = other.longueur_bits = max_len

    def enleverZeroGauche(self):
        while self.bits and self.bits[0] == '0':
            self.bits.pop(0)
        if not self.bits:
            self.bits = ['0']
        self.longueur_bits = len(self.bits)

    def comparer(self, other):
        if self.signe == 0 and other.signe == 1:
            return 1
        elif self.signe == 1 and other.signe == 0:
            return -1
        elif self.signe == 0:
            return self.comparerValeursAbsolues(other)
        else:
            return self.comparerValeursAbsolues(other) * -1

    def comparerValeursAbsolues(self, other):
        self.harmoniser(other)
        for a, b in zip(self.bits, other.bits):
            if a > b:
                other.enleverZeroGauche()
                return 1
            elif a < b:
                self.enleverZeroGauche()
                return -1
        return 0

    def estPair(self):
        if self.bits is None:
            raise ValueError("Le nombre est libere")
        return self.bits[-1] == '0'

    def diviserPar2(self):
        if self.bits is None:
            raise ValueError("Le nombre est libere")
        if self.longueur_bits == 1:
            self.bits = '0'
        else:
            self.bits = self.bits[:-1]
        self.longueur_bits = len(self.bits)

    def reduireDe1(self):
        if self.bits is None:
            raise ValueError("Le nombre est libere")

        if self.longueur_bits == 1 and self.bits[0] == '0':
            self.signe = 1
            self.bits = ['1']

        elif self.signe == 0:
            carry = 1
            for i in range(self.longueur_bits - 1, -1, -1):
                if carry == 0:
                    break
                if self.bits[i] == '1':
                    self.bits[i] = '0'
                    carry = 0
                else:
                    self.bits[i] = '1'
            if carry == 1:
                self.bits = ['1'] * self.longueur_bits
            self.enleverZeroGauche()
        else:
            carry = 1
            for i in range(self.longueur_bits - 1, -1, -1):
                if carry == 0:
                    break
                if self.bits[i] == '0':
                    self.bits[i] = '1'
                    carry = 0
                else:
                    self.bits[i] = '0'
            if carry == 1:
                self.bits.insert(0, '1')
            self.enleverZeroGauche()

    def multiplierPar2(self):
        if self.bits is None:
            raise ValueError("Le nombre est libere")

        self.bits = self.bits + ['0']
        self.longueur_bits += 1

    def additionner(self, other):
        if self.bits is None:
            raise ValueError("Le nombre est libere")
        if isinstance(other, int):
            other = GrandNombre(other)
        elif not isinstance(other, GrandNombre):
            raise ValueError("L'objet à additionner doit être un entier ou une instance de GrandNombre.")

        if self.signe == other.signe:
            result = self.additionnerValeursAbsolue(other)
            result.signe = self.signe
        else:
            if self.comparerValeursAbsolues(other) >= 0:
                result = self.soustraireValeursAbsolue(other)
                result.signe = self.signe
            else:
                result = other.soustraireValeursAbsolue(self)
                result.signe = other.signe
        return result

    def additionnerValeursAbsolue(self, other):
        self.harmoniser(other)
        result_bits = ['0'] * (self.longueur_bits + 1)  #si debordement
        carry = 0

        for i in range(self.longueur_bits - 1, -1, -1):
            a_self = int(self.bits[i])
            b_other = int(other.bits[i])
            total = a_self + b_other + carry
            result_bits[i + 1] = str(total % 2)
            carry = total // 2

        if carry == 1:
            result_bits[0] = '1'

        #on tronque si debordement
        result_bits = result_bits[1:] if result_bits[0] == '0' else result_bits
        result = GrandNombre(int(''.join(result_bits), 2))
        self.enleverZeroGauche()
        other.enleverZeroGauche()
        return result

    def soustraireValeursAbsolue(self, other):
        self.harmoniser(other)
        result_bits = ['0'] * self.longueur_bits
        borrow = 0

        for i in range(self.longueur_bits - 1, -1, -1):
            a_self = int(self.bits[i])
            b_other = int(other.bits[i])

            # Soustraction avec emprunt
            if a_self < b_other + borrow:
                result_bits[i] = str((a_self + 2) - (b_other + borrow))
                borrow = 1
            else:
                result_bits[i] = str(a_self - b_other - borrow)
                borrow = 0

        result = GrandNombre(int(''.join(result_bits), 2))
        self.enleverZeroGauche()
        other.enleverZeroGauche()
        return result

    def multiplier(self, other):
        if self.bits is None:
            raise ValueError("Le nombre est libéré")
        if isinstance(other, int):
            other = GrandNombre(other)
        elif not isinstance(other, GrandNombre):
            raise ValueError("L'objet à multiplier doit être un entier ou une instance de GrandNombre.")

        resultat = GrandNombre.initialiser0()
        if self.signe == other.signe:
            signe = 0
        else:
            signe = 1

        self.harmoniser(other)
        for i in range(other.longueur_bits - 1, -1, -1):
            if other.bits[i] == '1':
                temp = GrandNombre(int(''.join(self.bits), 2))
                for _ in range(other.longueur_bits - 1 - i):
                    temp.multiplierPar2()
                resultat = resultat.additionner(temp)
        self.enleverZeroGauche()
        other.enleverZeroGauche()

        resultat.signe = signe
        return resultat

    def puissance(self, exposant):
        if self.bits is None:
            raise ValueError("Le nombre est libéré.")
        if isinstance(exposant, (GrandNombre, int)):
            exposant_entier = exposant.en_entier() if isinstance(exposant, GrandNombre) else exposant
            if exposant_entier < 0:
                raise ValueError("L'exposant doit être positif.")
        else:
            raise ValueError("L'exposant doit être un entier ou une instance de GrandNombre.")
        if self.signe == 1 and exposant_entier % 2 == 1:
            signe = 1
        else:
            signe = 0

        result = GrandNombre.initialiser1()
        base = GrandNombre.instancier(self.bits, self.signe)
        while exposant_entier > 0:
            if exposant_entier % 2 == 1:
                result = result.multiplier(base)
            base = base.multiplier(base)
            exposant_entier //= 2
        result.signe = signe
        return result

    def soustraire(self, other):
        if isinstance(other, int):
            other = GrandNombre(other)
        elif not isinstance(other, GrandNombre):
            raise ValueError("la soustraction se fait avec un int ou un grandNombre")
        reverse_other = GrandNombre.instancier(other.bits, 1 - other.signe)
        return self.additionner(reverse_other)

    def decalerGauche(self, shift):
        if shift < 0:
            raise ValueError("Le décalage doit être positif")
        return GrandNombre(int(''.join(self.bits) + '0' * shift, 2))

    def estPuissanceDeDeux(self):
        if self.bits is None:
            raise ValueError("Le nombre est libéré.")
        if self.signe == 1 or ''.join(self.bits) == '0':
            return False

        return self.bits.count('1') == 1

    def approximer(self):
        if self.bits is None:
            raise ValueError("Le nombre a été libéré")
        if self.estPuissanceDeDeux():
            return self
        if self.signe == 1:
            raise ValueError("Le nombre doit etre positif")

        result = GrandNombre.instancier(self.bits, self.signe)
        result.bits = '1' + '0' * result.longueur_bits
        result.longueur_bits = len(result.bits)
        return result

    def modulo(self, other):
        if self.bits is None:
            raise ValueError("Le nombre est libéré.")
        if isinstance(other, int):
            other = GrandNombre(other)
        elif not isinstance(other, GrandNombre):
            raise ValueError("Le diviseur doit être un entier ou une instance de GrandNombre.")
        if other.signe == 1 or other.bits == ['0']:
            raise ValueError("Le diviseur doit être un nombre positif supérieur à 0.")

        result = GrandNombre.instancier(self.bits, self.signe)
        if result.comparer(other) == -1:
            if result.signe == 1:
                while result.signe == 1:
                    result = result.additionner(other)
            return result

        while result.comparer(other) >= 0:
            shift = 0
            approximation = other.approximer()
            while approximation.longueur_bits < result.longueur_bits:
                shift += 1
                approximation = other.decalerGauche(shift)

            retrait = other.decalerGauche(shift)
            if result.comparer(retrait) == -1:
                retrait = other.decalerGauche(shift - 1)

            result = result.soustraire(retrait)

        return result

    def exponentielEtModulo(self, exposant, module):
        if isinstance(exposant, (GrandNombre, int)):
            exposant_entier = exposant.en_entier() if isinstance(exposant, GrandNombre) else exposant
            if exposant_entier < 0:
                raise ValueError("L'exposant doit être positif.")
        else:
            raise ValueError("L'exposant doit être un entier ou une instance de GrandNombre.")
        if isinstance(module, int):
            module = GrandNombre(module)
        elif not isinstance(module, GrandNombre):
            raise ValueError("Le modulo doit être un entier ou une instance de GrandNombre.")

        result = GrandNombre.initialiser1()
        base = self.modulo(module)
        while exposant_entier > 0:
            if exposant_entier % 2 == 1:
                result = result.multiplier(base)
                result = result.modulo(module)
            base = base.multiplier(base)
            base = base.modulo(module)
            exposant_entier //= 2
        return result

    def quotient(self, other):
        if self.bits is None:
            raise ValueError("Le nombre est libéré.")
        if isinstance(other, int):
            other = GrandNombre(other)
        elif not isinstance(other, GrandNombre):
            raise ValueError("Le diviseur doit être un entier ou une instance de GrandNombre.")

        signe = 0 if self.signe == other.signe else 1

        abs_self = GrandNombre.instancier(self.bits, 0)
        quotient = GrandNombre.initialiser0()

        current = GrandNombre.instancier(other.bits, 0)
        temp_quotient = GrandNombre(1)

        while abs_self.comparerValeursAbsolues(current) >= 0:
            while abs_self.comparer(current) >= 0:
                current.multiplierPar2()
                temp_quotient.multiplierPar2()

            current.diviserPar2()
            temp_quotient.diviserPar2()

            abs_self = abs_self.soustraire(current)
            quotient = quotient.additionner(temp_quotient)

            current = GrandNombre.instancier(other.bits, 0)
            temp_quotient = GrandNombre(1)

        quotient.signe = signe
        return quotient

    def pgcd(self, other):
        if isinstance(other, int):
            other = GrandNombre(other)
        elif not isinstance(other, GrandNombre):
            raise ValueError("Le pgcd doit etre faite entre un GrandNombre ou un int")

        abs_self = GrandNombre.instancier(self.bits, 0)
        abs_other = GrandNombre.instancier(other.bits, 0)

        if abs_self.comparer(abs_other) >= 0:
            return abs_self.trouverPgcd(abs_other)
        return abs_other.trouverPgcd(abs_self)

    def trouverPgcd(self, other):
        valeur_diviser = GrandNombre.instancier(self.bits, 0)
        diviseur = GrandNombre.instancier(other.bits, 0)
        reste = valeur_diviser.modulo(diviseur)

        while reste.bits != ['0']:
            valeur_diviser = GrandNombre.instancier(diviseur.bits, 0)
            diviseur = GrandNombre.instancier(reste.bits, 0)
            reste = valeur_diviser.modulo(diviseur)
        return diviseur

    def estPremierAvec(self, other):
        if isinstance(other, int):
            other = GrandNombre(other)
        elif not isinstance(other, GrandNombre):
            raise ValueError("La comparaison doit etre faite entre un GrandNombre ou un int")

        if self.pgcd(other).bits == ['1']:
            return True
        return False

    def inverserAvecModulo(self, other):
        if self.bits is None:
            raise ValueError("Le nombre à été libéré.")
        if isinstance(other, int):
            other = GrandNombre(other)
        elif not isinstance(other, GrandNombre):
            raise ValueError("Le calcul de l'inverse modulaire doit etre fait avec des int ou grandNombre")

        if not self.estPremierAvec(other):
            raise ValueError("Les nombres ne sont pas premiers entre eux, donc l'inverse modulaire n'existe pas.")

        x1, y1, r1 = GrandNombre(1), GrandNombre(0), GrandNombre.instancier(self.bits, self.signe)
        x2, y2, r2 = GrandNombre(0), GrandNombre(1), GrandNombre.instancier(other.bits, other.signe)

        while r2.comparerValeursAbsolues(GrandNombre(0)):
            q = r1.quotient(r2)

            temp = GrandNombre.instancier(x2.bits, x2.signe)
            x2 = x1.soustraire(q.multiplier(x2))
            x1 = GrandNombre.instancier(temp.bits, temp.signe)

            temp = GrandNombre.instancier(y2.bits, y2.signe)
            y2 = y1.soustraire(q.multiplier(y2))
            y1 = GrandNombre.instancier(temp.bits, temp.signe)

            r1 = GrandNombre.instancier(r2.bits, r2.signe)
            r2 = self.multiplier(x2).additionner(other.multiplier(y2))

        return x1.modulo(other)


def estPremier(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    limite = int(n ** 0.5) + 1
    for i in range(5, limite, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def testLucasLehmer(p):
    if p < 2:
        return False
    s = 4
    M_p = (1 << p) - 1
    for _ in range(p - 2):
        s = (s * s - 2) % M_p
    return s == 0


def nombrePremierMersenne():
    while True:
        n = random.randint(80, 700)
        if estPremier(n):
            if testLucasLehmer(n):
                return GrandNombre((1 << n) - 1)


def creationCle():
    p = nombrePremierMersenne()
    q = nombrePremierMersenne()
    n = p.multiplier(q)
    phi = p.soustraire(GrandNombre.initialiser1()).multiplier(q.soustraire(GrandNombre.initialiser1()))
    e = GrandNombre(65537)
    if not(phi.estPremierAvec(e)):
        for i in range(3, n.en_entier()):
            if phi.estPremierAvec(GrandNombre(i)):
                e = GrandNombre(i)
                break
    if e is None:
        raise ValueError("Aucun e n'est viable")
    d = e.inverserAvecModulo(phi)
    publique = (e, n)
    privee = (d, n)
    return publique, privee


