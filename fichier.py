import grand_nombre
from grand_nombre import GrandNombre
import os

TAILLEMSG = 12


def sauvegarder_message(message: str, nom_fichier: str):
    if len(message) > TAILLEMSG:
        raise ValueError("Le message dépasse 12 octets (96 bits).")
    with open(nom_fichier, "w") as fichier:
        bits = ''.join(format(ord(c), '08b') for c in message)
        fichier.write(bits)
    print(f"Message sauvegardé dans {nom_fichier} sous forme binaire.")


def en_octet(message):
    longueur = len(message)
    reste = longueur % 8
    if reste != 0:
        message = '0' * (8 - reste) + message
    return message


def traduire_fichier(nom_fichier: str):
    try:
        with open(nom_fichier, "r") as fichier:
            contenu_binaire = fichier.read()
        contenu_binaire = en_octet(contenu_binaire)
        if contenu_binaire:
            # Diviser le contenu binaire en blocs de 8 bits (1 octet)
            message = ''.join(chr(int(contenu_binaire[i:i + 8], 2)) for i in range(0, len(contenu_binaire), 8))
            print(f"Contenu du fichier '{nom_fichier}' en texte : {message}")
        else:
            print(f"Le fichier '{nom_fichier}' est vide.")
    except FileNotFoundError:
        print(f"Le fichier '{nom_fichier}' est introuvable.")
    except ValueError:
        print(f"Erreur : Le contenu du fichier n'est pas un nombre binaire valide.")


def renvoyer_traduction(nom_fichier: str):
    try:
        with open(nom_fichier, "r") as fichier:
            contenu_binaire = fichier.read()
        contenu_binaire = en_octet(contenu_binaire)

        if contenu_binaire:
            message = ''.join(chr(int(contenu_binaire[i:i + 8], 2)) for i in range(0, len(contenu_binaire), 8))
            return message
        else:
            print(f"Le fichier '{nom_fichier}' est vide.")
    except FileNotFoundError:
        print(f"Le fichier '{nom_fichier}' est introuvable.")
    except ValueError:
        print(f"Erreur : Le contenu du fichier n'est pas un nombre binaire valide.")
    return None


def chiffrer_fichier_rsa_int(nom_fichier: str, nom_fichier_sortie: str, cle: int, module: int):
    try:
        with open(nom_fichier, "r") as fichier:
            message = fichier.read()
        if not message:
            print(f"Erreur : Le fichier '{nom_fichier}' est vide ou contient un message invalide.")
            return

        message_gn = grand_nombre.lire_binaire(message)
        cle_gn = GrandNombre(cle)
        module_gn = GrandNombre(module)

        # Chiffrement RSA
        message_chiffrer = message_gn.exponentielEtModulo(cle_gn, module_gn)
        if message_chiffrer is None:
            print("Erreur : le chiffrement a échoué.")
            return
        message_chiffrer = ''.join(message_chiffrer.binaire)

        with open(nom_fichier_sortie, "w") as sortie:
            sortie.write(message_chiffrer)
        print(f"Message chiffré sauvegardé dans {nom_fichier_sortie}.")
    except FileNotFoundError:
        print(f"Le fichier '{nom_fichier}' est introuvable.")
    except Exception as e:
        print(f"Erreur lors du chiffrement : {e}")


def chiffrer_fichier_rsa_grandNombre(nom_fichier: str, nom_fichier_sortie: str, cle: grand_nombre,
                                     module: grand_nombre):
    try:
        with open(nom_fichier, "r") as fichier:
            message = fichier.read()
        if not message:
            print(f"Erreur : Le fichier '{nom_fichier}' est vide ou contient un message invalide.")
            return


        message_gn = grand_nombre.lire_binaire(message)

        # Chiffrement RSA
        message_chiffrer = message_gn.exponentielEtModulo(cle, module)
        if message_chiffrer is None:
            print("Erreur : le chiffrement a échoué.")
            return
        message_chiffrer = ''.join(message_chiffrer.binaire)

        with open(nom_fichier_sortie, "w") as sortie:
            sortie.write(message_chiffrer)
        print(f"Message chiffré sauvegardé dans {nom_fichier_sortie}.")
    except FileNotFoundError:
        print(f"Le fichier '{nom_fichier}' est introuvable.")
    except Exception as e:
        print(f"Erreur lors du chiffrement : {e}")


def sauvegarder_long_message(message: str, nom_fichier: str):
    numero = 1
    for position in range(0, len(message), 12):
        bloc = message[position:position + 12]
        sauvegarder_message(bloc, nom_fichier + str(numero) + ".txt")
        numero += 1
    return numero


def chiffrer_long_message_int(prefixe_entre: str, suffixe_sortie: str, numero: int, cle: int, module: int):
    for i in range(1, numero):
        chiffrer_fichier_rsa_int(prefixe_entre + str(i) + ".txt", suffixe_sortie + str(i) + ".txt", cle, module)


def chiffrer_long_message_grand_nombre(prefixe_entre: str, suffixe_sortie: str, numero: int, cle: grand_nombre,
                                       module: grand_nombre):
    for i in range(1, numero):
        chiffrer_fichier_rsa_grandNombre(prefixe_entre + str(i) + ".txt", suffixe_sortie + str(i) + ".txt", cle, module)


def traduire_long_message(numero: int, nom_fichier: str):
    message = ''
    for i in range(1, numero):
        message += renvoyer_traduction(nom_fichier + str(i) + ".txt")
    print(f"\n------------------------------------------\n\nLe message est :\n{message}")


def supprimer_fichiers(nom_fichier, valeur):
    for i in range(1, valeur + 1):
        nomfichier = f"{nom_fichier}{i}.txt"
        if os.path.exists(nomfichier):
            try:
                os.remove(nomfichier)
            except Exception as e:
                print(f"Erreur lors de la suppression de {nomfichier}: {e}")
        else:
            print(f"Le fichier {nomfichier} n'existe pas.")
