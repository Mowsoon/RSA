import rsa

from fichier import *
from grand_nombre import creationCle

message = "Je ne suis pas interresser par le fait de te répondre Ganbold"
nom_fichier = "texte"
nom_fichier_chiffre = "chiffrer"
nom_fichier_dechiffre = "dechiffrer"

test = 2

if test == 1:
    public_key, private_key = rsa.newkeys(100)
    cle_publique = public_key.e
    module = public_key.n
    cle_privee = private_key.d
elif test == 2:
    public_key, private_key = creationCle()
    cle_publique = public_key[0]
    module = public_key[1]
    cle_privee = private_key[0]
else:
    raise ValueError("il faut choisir soit 1 soit 2")


"""
# Sauvegarder le message dans un fichier binaire
sauvegarder_message(message, nom_fichier)

# Chiffrer le fichier avec la clé publique
chiffrer_fichier_rsa_grand_nombre(nom_fichier, nom_fichier_chiffre, cle_publique, module)

# Déchiffrer le fichier chiffré avec la clé privée (ici, vous pouvez adapter pour un déchiffrement réel)
chiffrer_fichier_rsa_grand_nombre(nom_fichier_chiffre, nom_fichier_dechiffre, cle_privee, module)

# Lire et traduire le contenu déchiffré pour vérifier
traduire_fichier(nom_fichier_dechiffre)
"""

numero = sauvegarder_long_message(message, nom_fichier)

if test == 1:
    chiffrer_long_message_int(nom_fichier, nom_fichier_chiffre, numero, cle_publique, module)
    chiffrer_long_message_int(nom_fichier_chiffre, nom_fichier_dechiffre, numero, cle_privee, module)

else:
    chiffrer_long_message_grand_nombre(nom_fichier, nom_fichier_chiffre, numero, cle_publique, module)
    chiffrer_long_message_grand_nombre(nom_fichier_chiffre, nom_fichier_dechiffre, numero, cle_privee, module)

traduire_long_message(numero, nom_fichier_dechiffre)

supprimer_fichiers(nom_fichier, 6)
supprimer_fichiers(nom_fichier_chiffre, 6)
supprimer_fichiers(nom_fichier_dechiffre, 6)