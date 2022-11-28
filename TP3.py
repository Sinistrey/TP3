"""
Programme fait par Lily Qian
Groupe: 403
Description: Combat des monstres
"""
import random

hp = 20
defeated_monster_count = 0
monster_count = 0
combat_count = 0
victory_count = 0
defeat_count = 0
win_streak = 0


def defeat_conditions():
    """
    cette fonction sert a modifier les données au moment d'une défaite
    """
    global hp, defeat_count, win_streak
    hp -= random_monster_strength
    defeat_count += 1
    win_streak = 0


def victory_conditions():
    """
    cette fonction sert a modifier les données au moment d'une victoire
    """
    global hp, victory_count, defeated_monster_count, win_streak
    hp += random_monster_strength
    victory_count += 1
    win_streak += 1
    defeated_monster_count += 1
    print(f"Nombre de victoires consécutifs: {win_streak}")


def quit_game():
    global jeu
    print("Merci et au revoir...")
    jeu = False


jeu = True
is_boss = False
while jeu:
    if win_streak == 3 and (win_streak % 3 == 0):
        random_monster_strength = random.randint(8, 10) + random.randint(8, 10)
        is_boss = True
    else:
        random_monster_strength = random.randint(1, 5) + random.randint(1, 5)
        is_boss = False
    print(f"Vous tombez face avec un adversaire de difficulté : {random_monster_strength}\n")
    print("Que voulez_vous faire?:")
    print("1- Combattre cet adversaire ")
    print("2- Afficher les règles du jeu")
    print("3-Quitter la partie")
    if not is_boss:
        print("4- Contourner cet adversaire et aller ouvrir une autre porte ")
    print("Que voulez_vous faire?: ")
    choix = int(input("\nVotre option:"))

    if choix == 1:
        monster_count += 1
        combat_count += 1
        random_player_strength = random.randint(1, 6) + random.randint(1, 6)
        print(f"Adversaire : {monster_count}"
              f"\nForce de l'adversaire : {random_monster_strength}"
              f"\nNiveau de vie de l'usager : {hp}"
              f"\nCombat {combat_count} : {victory_count} victoires vs {defeat_count} défaites"
              f"\nlancer du dé: {random_player_strength}")
        if random_monster_strength >= random_player_strength:
            print("Dernier combat = défaite ")
            defeat_conditions()
            print(f"Niveau de vie: {hp}\n")
            win_streak = 0

        elif random_monster_strength < random_player_strength:
            print("Dernier combat = victoire")
            victory_conditions()
            print(f"Niveau de vie: {hp}\n")

    elif choix == 2:
        print("Pour réussir un combat, il faut que la valeur du dé lancé soit"
              "\nsupérieure à la force de l'adversaire. Dans ce cas, le niveau"
              "\nde vie de l'usager est augmenté de la force de l'adversaire."
              "\nde lune défaite a lieu lorsque la valeur du dé lancé par l'usager"
              "\nest inférieure ou égale à la force de l'adversaire. Dans ce cas,"
              "\nle niveau de vie de l'usager est diminué de la force de l'adversaire.")
        decision = str(input("Voulez-vous continuer le jeu? o/n\n"))
        if decision == "o":
            jeu = True
        elif decision == "n":
            quit_game()

    elif choix == 3:
        quit_game()

    elif choix == 4:
        win_streak = 0
        hp -= 1
        print("Vous avez perdu 1 vie."
              f"\nNiveau de vie: {hp}\n")

    if hp > 0:
        jeu = True
    elif hp <= 0:
        print(f"La partie est terminée. vous avez tué {defeated_monster_count} monstres")
        jeu = False
