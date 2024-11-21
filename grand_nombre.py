class GrandNombre:
    def __init__(self, nombre: int):
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
    def initialiser(cls, bit_string):
        if not isinstance(bit_string, str):
            raise ValueError("L'entrée doit être une chaîne de caractères.")

        if not all(bit in '01' for bit in bit_string):
            raise ValueError("La chaîne de caractères doit être composée uniquement de '0' et '1'.")

        instance = cls(0)
        instance.bits = list(bit_string)
        instance.longueur_bits = len(instance.bits)
        return instance

    def libererNombre(self):
        self.bits = None
        self.longueur_bits = 0

    def afficher(self):
        if self.bits is None:
            print("Le nombre est libéré")
        else:
            representation = ''.join(self.bits)
            print("Représentation binaire :", representation)

    def harmoniser(self, other):
        max_len = max(self.longueur_bits, other.longueur_bits)

        self.bits = list('0' * (max_len - len(self.bits)) + ''.join(self.bits))
        other.bits = list('0' * (max_len - len(other.bits)) + ''.join(other.bits))

        other.longueur_bits = max_len
        self.longueur_bits = max_len

    def enleverZeroGauche(self):
        while self.bits and self.bits[0] == '0':
            self.bits.pop(0)
        if not self.bits:
            self.bits = ['0']
        self.longueur_bits = len(self.bits)

    def comparer(self, other):
        if self.bits is None:
            raise ValueError("Le nombre a été libéré.")
        if isinstance(other, int):
            other = GrandNombre(other)
        elif not isinstance(other, GrandNombre):
            raise ValueError("L'objet à comparer doit être un entier ou une instance de GrandNombre.")

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

    def en_entier(self):
        entier = int(''.join(self.bits), 2)
        return entier

    def multiplier(self, other):
        if self.bits is None:
            raise ValueError("Le nombre est libéré")
        if isinstance(other, int):
            other = GrandNombre(other)
        elif not isinstance(other, GrandNombre):
            raise ValueError("L'objet à multiplier doit être un entier ou une instance de GrandNombre.")

        resultat = GrandNombre.initialiser0()
        self.harmoniser(other)

        for i in range(other.longueur_bits - 1, -1, -1):
            if other.bits[i] == '1':
                temp = GrandNombre(int(''.join(self.bits), 2))
                for _ in range(other.longueur_bits - 1 - i):
                    temp.multiplierPar2()
                resultat = resultat.additionner(temp)

        self.enleverZeroGauche()
        other.enleverZeroGauche()
        return resultat

    def puissance(self, exposant):
        if not isinstance(exposant, int) or exposant < 0:
            raise ValueError("L'exposant doit être un entier positif.")
        if self.bits is None and exposant == 0:
            raise ValueError("Le nombre est libéré.")

        resultat = GrandNombre.initialiser1()
        base = GrandNombre(int(''.join(self.bits), 2))

        while exposant > 0:
            if exposant % 2 == 1:
                resultat = resultat.multiplier(base)
            base = base.multiplier(base)
            exposant //= 2

        return resultat

    def soustraire(self, other):
        if self.bits is None:
            raise ValueError("Le nombre est libéré.")
        if isinstance(other, int):
            other = GrandNombre(other)
        if not isinstance(other, GrandNombre):
            raise ValueError("L'objet à soustraire doit être un entier ou une instance de GrandNombre.")
        if self.comparer(other) == -1:
            raise ValueError("La soustraction résulte en un nombre négatif, ce qui n'est pas supporté.")

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

    def decaler_gauche(self, shift):
        if shift < 0:
            raise ValueError("Le décalage doit être positif")
        return GrandNombre(int(''.join(self.bits) + '0' * shift, 2))

    def estPuissanceDeDeux(self):
        if self.en_entier() == 1:
            return True

        nombre = self.en_entier()
        while nombre % 2 == 0 and nombre > 1:
            nombre //= 2
        return nombre == 1

    def approximer(self):
        if self.bits is None:
            raise ValueError("Le nombre a été libéré")
        if self.estPuissanceDeDeux():
            return self

        result = GrandNombre(self.en_entier())
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
        if other.en_entier() == 0:
            raise ValueError("Le diviseur ne peut pas être zéro.")

        result = GrandNombre(self.en_entier())
        if result.comparer(other) == -1:
            return result
        while result.comparer(other) >= 0:
            shift = 0
            approximation = other.approximer()
            while approximation.longueur_bits < result.longueur_bits:
                shift += 1
                approximation = other.decaler_gauche(shift)

            retrait = other.decaler_gauche(shift)
            if result.comparer(retrait) == -1:
                retrait = other.decaler_gauche(shift - 1)

            result = result.soustraire(retrait)

        return result

    def exponentielEtModulo(self, exposant, module):
        if isinstance(exposant, int):
            exposant = GrandNombre(exposant)
        elif not isinstance(exposant, GrandNombre):
            raise ValueError("L'exposant doit être un entier ou une instance de GrandNombre.")
        if isinstance(module, int):
            module = GrandNombre(module)
        elif not isinstance(module, GrandNombre):
            raise ValueError("Le modulo doit être un entier ou une instance de GrandNombre.")

        resultat = GrandNombre.initialiser1()
        base = self.modulo(module)
        exposant_entier = exposant.en_entier()

        while exposant_entier > 0:
            if exposant_entier % 2 == 1:
                resultat = resultat.multiplier(base)
                resultat = resultat.modulo(module)
            base = base.multiplier(base)
            base = base.modulo(module)
            exposant_entier //= 2

        return resultat

    def pgcd(self, other):
        if isinstance(other, int):
            other = GrandNombre(other)
        elif not isinstance(other, GrandNombre):
            raise ValueError("Le pgcd doit etre faite entre un GrandNombre ou un int")
        if self.comparer(other) >= 0:
            return self.trouverPgcd(other)
        return other.trouverPgcd(self)

    def trouverPgcd(self, other):
        valeur_diviser = GrandNombre(self.en_entier())
        diviseur = GrandNombre(other.en_entier())
        reste = valeur_diviser.modulo(diviseur)

        while reste.en_entier() != 0:
            valeur_diviser = GrandNombre(diviseur.en_entier())
            diviseur = GrandNombre(reste.en_entier())
            reste = valeur_diviser.modulo(diviseur)
        return diviseur

    def premierEntreEux(self, other):
        if isinstance(other, int):
            other = GrandNombre(other)
        elif not isinstance(other, GrandNombre):
            raise ValueError("La comparaison doit etre faite entre un GrandNombre ou un int")

        if self.pgcd(other).en_entier() == 1:
            return True
        return False

    def calculer_quotient(self, other):
        if isinstance(other, int):
            other = GrandNombre(other)
        elif not isinstance(other, GrandNombre):
            raise ValueError("Le diviseur doit être un entier ou une instance de GrandNombre.")
        if self.comparer(other) == -1:
            return GrandNombre(0)

        quotient = 0
        cpt = 1
        reste = GrandNombre(self.en_entier())

        while reste.comparer(other) >= 0:
            diviseur = GrandNombre(other.en_entier())
            diviseur.multiplierPar2()
            while reste.comparer(diviseur) >= 0:
                cpt *= 2
                diviseur.multiplierPar2()
            diviseur.diviserPar2()
            cpt //= 2
            reste = reste.soustraire(diviseur)
            quotient += cpt

        return GrandNombre(quotient)







