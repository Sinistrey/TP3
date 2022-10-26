import random

hp = 20
monster_count = 0
combat_count = 0
victory_count = 0
defeat_count = 0


def combat_status():
    if random_monster_strength > random_player_strength:
        "defaite"
    elif random_monster_strength < random_player_strength:
        "victoire"




def total_monster_count():
    global monster_count
    monster_count += 1


def minus_hp():
    global hp
    hp -= random_monster_strength


def add_hp():
    global hp
    hp += random_monster_strength


jeu = True

while jeu:
    random_monster_strength = random.randint(1, 5)
    print(f"Vous tombez face avec un adversaire de difficulté : {random_monster_strength}")
    choix = int(input("Que voulez_vous faire?: "
                      "\n1- Combattre cet adversaire "
                      "\n2- Contourner cet adversaire et aller ouvrir une autre porte "
                      "\n3- Afficher les règles du jeu  "
                      "\n4- Quitter la partie "
                      "\nVotre option:"))
    if choix == 1:
        total_monster_count()
        random_player_strength = random.randint(1, 6)
        print(f"Adversaire : {monster_count}"
              f"\nForce de l'adversaire : {random_monster_strength}"
              f"\nNiveau de vie de l'usager : {hp}"
              f"\nCombat {combat_count} : {victory_count} victoires vs {defeat_count} defaites")

        print(f"lancer du de: {random_player_strength}"
              f"\nDernier combat = {combat_status}")



    elif choix == 2:
        print("choix 2")

    elif choix == 3:
        print("choix 3")

    elif choix == 4:
        jeu = False
