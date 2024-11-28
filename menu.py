import rsa as rsa_simple
import time
from fichier import *
from grand_nombre import creationCleRSA
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


message = "Ceci est une phrase test qui à pour but d'être asser longue pour que le test soit cohérent."
nom_fichier = "texte"
nom_fichier_chiffre = "chiffrer"
nom_fichier_dechiffre = "dechiffrer"


def RsaMessage(cle, module, nom_fichier1, nom_fichier2, numero):
    chiffrer_long_message_int(nom_fichier1, nom_fichier2, numero, cle, module)

def supprimerFiles(numero):
    supprimer_fichiers(nom_fichier, numero-1)
    supprimer_fichiers(nom_fichier_chiffre, numero-1)
    supprimer_fichiers(nom_fichier_dechiffre, numero-1)


def lireFile(numero):
    traduire_long_message(numero, nom_fichier_dechiffre)
    print(f"\nEn sachant que le message originel est :\n{message}\n")


def MersenneMessage(cle, module, nom_fichier1, nom_fichier2, numero):
    chiffrer_long_message_grand_nombre(nom_fichier1, nom_fichier2, numero, cle, module)


def menu_principal():
    print("\n*** MENU PRINCIPAL ***")
    print("1. Générer une clé avec la bibliothèque RSA puis crypter/decrypter")
    print("2. Générer une clé avec les méthodes de l'énoncer puis crypter/decrypter")
    print("3. Tester la performance de génération de clés (RSA)")
    print("4. Tester la performance de génération de clés (Méthodes énoncer)")
    print("5. Tester la performance de cryptage/décryptage avec les grandNombres(Gen clé RSA)")
    print("6. Tester la performance de cryptage/décryptage avec les grandNombres(Gen clé Méthodes énoncer)")
    print("7. Calculer la taille moyenne de la clé (Méthodes énoncer)")
    print("8. Tester la performance de cryptage/décryptage avec la bibliotheque RSA")
    print("0. Quitter")
    choix = input("\nChoisissez une option : ")
    return choix


def option_1_generer_cle_rsa():
    taille = int(input("Entrez la taille des clés RSA à générer (en bits) : "))
    public_key, private_key = rsa_simple.newkeys(taille)
    numero = sauvegarder_long_message(message, nom_fichier)
    RsaMessage(public_key.e, public_key.n, nom_fichier, nom_fichier_chiffre, numero)
    RsaMessage(private_key.d, private_key.n, nom_fichier_chiffre, nom_fichier_dechiffre, numero)
    lireFile(numero)
    supprimerFiles(numero)
    return


def option_2_generer_cle_perso():
    taille_min = int(input("Entrez la taille minimale des nombres premiers : "))
    taille_max = int(input("Entrez la taille maximale des nombres premiers : "))
    public_key, private_key = creationCleRSA(taille_min, taille_max)
    numero = sauvegarder_long_message(message, nom_fichier)
    MersenneMessage(public_key[0], public_key[1], nom_fichier, nom_fichier_chiffre, numero)
    MersenneMessage(private_key[0], private_key[1], nom_fichier_chiffre, nom_fichier_dechiffre, numero)
    lireFile(numero)
    supprimerFiles(numero)
    return


def option_3_test_generation_rsa():
    repetitions = int(input("Entrez le nombre de répétitions : "))
    taille = int(input("Entrez la taille des clés RSA à générer (en bits) : "))
    temps_total = 0
    for _ in range(repetitions):
        debut = time.time()
        rsa_simple.newkeys(taille)
        temps_total += time.time() - debut
    temps_moyen = temps_total / repetitions
    print(f"\nTemps moyen pour générer une clé avec la bibliothèque RSA : {temps_moyen:.6f} secondes")


def option_4_test_generation_enoncer():
    repetitions = int(input("Entrez le nombre de répétitions : "))
    taille_min = int(input("Entrez la taille minimale des nombres premiers : "))
    taille_max = int(input("Entrez la taille maximale des nombres premiers : "))
    temps_total = 0
    for _ in range(repetitions):
        debut = time.time()
        creationCleRSA(taille_min, taille_max)
        temps_total += time.time() - debut
    temps_moyen = temps_total / repetitions
    print(f"\nTemps moyen pour générer une clé avec les fonctions : {temps_moyen:.6f} secondes")


def option_5_test_cryptage_enoncer_generationRSA():
    taille = int(input("Entrez la taille des clés RSA à générer (en bits) : "))
    repetitions = int(input("Entrez le nombre de répétitions : "))
    numero = sauvegarder_long_message(message, nom_fichier)
    public_key, private_key = rsa_simple.newkeys(taille)
    temps_cryptage = 0
    temps_decryptage = 0
    for _ in range(repetitions):
        debut = time.time()
        RsaMessage(public_key.e, public_key.n, nom_fichier, nom_fichier_chiffre, numero)
        temps_cryptage += time.time() - debut

        debut = time.time()
        RsaMessage(private_key.d, private_key.n, nom_fichier_chiffre, nom_fichier_dechiffre, numero)
        temps_decryptage += time.time() - debut
    print(f"\nTemps moyen de cryptage : {temps_cryptage / repetitions:.6f} secondes")
    print(f"Temps moyen de décryptage : {temps_decryptage / repetitions:.6f} secondes")
    supprimerFiles(numero)


def option_6_test_cryptage_enoncer_generationMerise():
    taille_min = int(input("Entrez la taille minimale des nombres premiers : "))
    taille_max = int(input("Entrez la taille maximale des nombres premiers : "))
    repetitions = int(input("Entrez le nombre de répétitions : "))
    numero = sauvegarder_long_message(message, nom_fichier)
    public_key, private_key = creationCleRSA(taille_min, taille_max)
    cle_publique, module = public_key
    cle_privee = private_key[0]
    temps_cryptage = 0
    temps_decryptage = 0
    for _ in range(repetitions):
        debut = time.time()
        MersenneMessage(cle_publique, module, nom_fichier, nom_fichier_chiffre, numero)
        temps_cryptage += time.time() - debut

        debut = time.time()
        MersenneMessage(cle_privee, module, nom_fichier_chiffre, nom_fichier_dechiffre, numero)
        temps_decryptage += time.time() - debut
    print(f"\nTemps moyen de cryptage : {temps_cryptage / repetitions:.6f} secondes")
    print(f"Temps moyen de décryptage : {temps_decryptage / repetitions:.6f} secondes")
    supprimerFiles(numero)


def option_7_taille_moyenne_n():
    try:
        repetitions = int(input("Nombre de répétitions : "))
        taille_min = int(input("Entrez la taille minimale des nombres premiers : "))
        taille_max = int(input("Entrez la taille maximale des nombres premiers : "))

        if repetitions <= 0 or taille_min <= 0 or taille_max <= 0 or taille_min > taille_max:
            print("Les valeurs fournies sont invalides. Veuillez réessayer.")
            return

        total_taille_n = 0
        for i in range(repetitions):
            public_key, private_key = creationCleRSA(taille_min, taille_max)
            total_taille_n += len(public_key[1].binaire)

        taille_moyenne = total_taille_n / repetitions
        print(f"\nTaille moyenne de n sur {repetitions} répétitions : {taille_moyenne:.2f} bits")


    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")


def option_8_test_cryptage_rsa_generationRSA():
    taille = int(input("Entrez la taille des clés RSA à générer (en bits) : "))
    repetitions = int(input("Entrez le nombre de répétitions : "))

    # Génération des clés
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=taille,
    )
    public_key = private_key.public_key()

    # Découper le message en blocs de 12 octets
    def decouper_message(message, taille_bloc):
        return [message[i:i + taille_bloc] for i in range(0, len(message), taille_bloc)]

    blocs = decouper_message(message.encode(), 12)

    # Variables pour stocker les temps
    temps_cryptage = 0
    temps_decryptage = 0

    for _ in range(repetitions):
        message_chiffre = []
        message_dechiffre = b""

        for bloc in blocs:
            # Mesure du temps de cryptage
            debut = time.perf_counter()
            bloc_chiffre = public_key.encrypt(
                bloc,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            temps_cryptage += time.perf_counter() - debut
            message_chiffre.append(bloc_chiffre)

            # Mesure du temps de décryptage
            debut = time.perf_counter()
            bloc_dechiffre = private_key.decrypt(
                bloc_chiffre,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            temps_decryptage += time.perf_counter() - debut
            message_dechiffre += bloc_dechiffre

        # Vérification que le message décrypté correspond au message original
        assert message_dechiffre == message.encode(), "Le message décrypté ne correspond pas au message original !"

    # Calcul des temps moyens
    print(f"\nTemps moyen de cryptage : {temps_cryptage / repetitions:.6f} secondes")
    print(f"Temps moyen de décryptage : {temps_decryptage / repetitions:.6f} secondes")



