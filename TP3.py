import random

hp = 20
defeated_monster_count = 0
monster_count = 0
combat_count = 0
victory_count = 0
defeat_count = 0


def total_monster_count():
    global monster_count
    monster_count += 1


def total_combat_count():
    global combat_count
    combat_count += 1



def defeat_conditions():
    global hp
    global defeat_count
    hp -= random_monster_strength
    defeat_count += 1

def victory_conditions():
    global hp
    global victory_count
    global defeated_monster_count
    hp += random_monster_strength
    victory_count += 1
    defeated_monster_count += 1


jeu = True

while jeu:
    random_monster_strength = random.randint(1, 5) + random.randint(1, 5)
    print(f"Vous tombez face avec un adversaire de difficulté : {random_monster_strength}")
    choix = int(input("Que voulez_vous faire?: "
                      "\n1- Combattre cet adversaire "
                      "\n2- Contourner cet adversaire et aller ouvrir une autre porte "
                      "\n3- Afficher les règles du jeu  "
                      "\n4- Quitter la partie "
                      "\nVotre option:"))
    if choix == 1:
        total_monster_count()
        total_combat_count()

        random_player_strength = random.randint(1, 2) + random.randint(1, 2)
        print(f"Adversaire : {monster_count}"
              f"\nForce de l'adversaire : {random_monster_strength}"
              f"\nNiveau de vie de l'usager : {hp}"
              f"\nCombat {combat_count} : {victory_count} victoires vs {defeat_count} defaites"
              f"\nlancer du de: {random_player_strength}")
        if random_monster_strength >= random_player_strength:
            print("Dernier combat = défaite ")
            defeat_conditions()
            print(f"Niveau de vie: {hp}")
            if hp > 0:
                jeu = True
            if hp <= 0:
                print(f"La partie est terminée. vous avez tué {defeated_monster_count} monstres")
                jeu = False

        elif random_monster_strength < random_player_strength:
            print("Dernier combat = victoire")
            victory_conditions()
            print(f"Niveau de vie: {hp}")
            jeu = True



    elif choix == 2:
        print("choix 2")

    elif choix == 3:
        print("Pour réussir un combat, il faut que la valeur du dé lancé soit"
              "\nsupérieure à la force de l'adversaire. Dans ce cas, le niveau"
              "\nde vie de l'usager est augmenté de la force de l'adversaire."
              "\nde lune défaite a lieu lorsque la valeur du dé lancé par l'usager"
              "\nest inférieure ou égale à la force de l'adversaire. Dans ce cas,"
              "\n")


    elif choix == 4:
        print("Merci et au revoir...")
        jeu = False
