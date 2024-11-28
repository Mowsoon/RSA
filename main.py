from menu import *

def main():
    while True:
        choix = menu_principal()
        if choix == "1":
            option_1_generer_cle_rsa()
        elif choix == "2":
            option_2_generer_cle_perso()
        elif choix == "3":
            option_3_test_generation_rsa()
        elif choix == "4":
            option_4_test_generation_enoncer()
        elif choix == "5":
            option_5_test_cryptage_enoncer_generationRSA()
        elif choix == "6":
            option_6_test_cryptage_enoncer_generationMerise()
        elif choix == "7":
            option_7_taille_moyenne_n()
        elif choix == "8":
            option_8_test_cryptage_rsa_generationRSA()
        elif choix == "0":
            print("Au revoir !")
            break
        else:
            print("Option invalide, veuillez réessayer.")
        input("\nAppuyez sur une Entrée pour continuer...")

if __name__ == "__main__":
    main()
