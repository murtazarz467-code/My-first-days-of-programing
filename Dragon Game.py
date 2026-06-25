import random
import json


# =====================
# SAVE & LOAD
# =====================

def save_game(player):
    with open("save.json", "w") as file:
        json.dump(player, file)

    print("Game saved!")


def load_game():
    try:
        with open("save.json") as file:
            return json.load(file)
    except:
        return None


# =====================
# CHARACTER CREATION
# =====================

print("===== DRAGON RPG =====")
print("1. Warrior")
print("2. Mage")
print("3. Archer")

choice = input("Choose your class: ")

if choice == "1":
    player = {
        "class": "Warrior",
        "hp": 120,
        "max_hp": 120,
        "gold": 50,
        "xp": 0,
        "level": 1,
        "critical": 15,
        "potions": 2,
        "attack_scrolls": 1,
        "defense_scrolls": 1,
    }

elif choice == "2":
    player = {
        "class": "Mage",
        "hp": 90,
        "max_hp": 90,
        "gold": 50,
        "xp": 0,
        "level": 1,
        "critical": 10,
        "potions": 3,
        "attack_scrolls": 3,
        "defense_scrolls": 2,
    }

else:
    player = {
        "class": "Archer",
        "hp": 100,
        "max_hp": 100,
        "gold": 50,
        "xp": 0,
        "level": 1,
        "critical": 30,
        "potions": 2,
        "attack_scrolls": 2,
        "defense_scrolls": 1,
    }


# =====================
# MAIN GAME LOOP
# =====================

dragons = [
    ("Fire Dragon", 150),
    ("Ice Dragon", 180),
    ("Shadow Dragon", 250),
]

for dragon_name, dragon_max_hp in dragons:

    dragon_hp = dragon_max_hp

    print(f"\n🔥 A {dragon_name} appeared!")

    while player["hp"] > 0 and dragon_hp > 0:

        print("\n========================")
        print(f"Class: {player['class']}")
        print(f"Level: {player['level']}")
        print(f"XP: {player['xp']}")
        print(f"Gold: {player['gold']}")
        print(f"HP: {player['hp']}/{player['max_hp']}")
        print(f"{dragon_name}: {dragon_hp}")
        print("========================")

        print("\n1. Attack")
        print("2. Use Potion")
        print("3. Attack Scroll")
        print("4. Defense Scroll")
        print("5. Shop")
        print("6. Save")
        print("7. Run")

        action = input("Choose: ")

        defense = 0

        # =====================
        # ATTACK
        # =====================

        if action == "1":

            damage = random.randint(10, 20)

            if random.randint(1, 100) <= player["critical"]:
                damage *= 2
                print("🔥 CRITICAL HIT!")

            dragon_hp -= damage

            print(f"You dealt {damage} damage!")

        # =====================
        # HEAL
        # =====================

        elif action == "2":

            if player["potions"] > 0:

                heal = random.randint(20, 30)

                player["hp"] = min(
                    player["max_hp"],
                    player["hp"] + heal
                )

                player["potions"] -= 1

                print(f"You healed {heal} HP!")

            else:
                print("No potions left!")
                continue

        # =====================
        # ATTACK SCROLL
        # =====================

        elif action == "3":

            if player["attack_scrolls"] > 0:

                damage = random.randint(30, 50)

                dragon_hp -= damage

                player["attack_scrolls"] -= 1

                print(f"Magic attack dealt {damage} damage!")

            else:
                print("No attack scrolls!")
                continue

        # =====================
        # DEFENSE SCROLL
        # =====================

        elif action == "4":

            if player["defense_scrolls"] > 0:

                defense = random.randint(10, 20)

                player["defense_scrolls"] -= 1

                print(f"Defense increased by {defense}!")

            else:
                print("No defense scrolls!")
                continue

        # =====================
        # SHOP
        # =====================

        elif action == "5":

            while True:

                print("\n===== SHOP =====")
                print("1. Healing Potion (20 gold)")
                print("2. Attack Scroll (30 gold)")
                print("3. Defense Scroll (25 gold)")
                print("4. Exit")

                shop = input("Choose: ")

                if shop == "1":

                    if player["gold"] >= 20:
                        player["gold"] -= 20
                        player["potions"] += 1
                        print("Potion bought!")

                    else:
                        print("Not enough gold!")

                elif shop == "2":

                    if player["gold"] >= 30:
                        player["gold"] -= 30
                        player["attack_scrolls"] += 1
                        print("Attack Scroll bought!")

                    else:
                        print("Not enough gold!")

                elif shop == "3":

                    if player["gold"] >= 25:
                        player["gold"] -= 25
                        player["defense_scrolls"] += 1
                        print("Defense Scroll bought!")

                    else:
                        print("Not enough gold!")

                elif shop == "4":
                    break

            continue

        # =====================
        # SAVE
        # =====================

        elif action == "6":

            save_game(player)
            continue

        # =====================
        # RUN
        # =====================

        elif action == "7":

            chance = random.randint(1, 100)

            if chance <= 50:
                print("You escaped!")
                quit()

            else:
                print("Escape failed!")

        else:
            print("Invalid choice!")
            continue

        # =====================
        # DRAGON DEAD
        # =====================

        if dragon_hp <= 0:

            print(f"\n🏆 {dragon_name} defeated!")

            earned_gold = random.randint(30, 60)
            earned_xp = 100

            player["gold"] += earned_gold
            player["xp"] += earned_xp

            print(f"+{earned_gold} Gold")
            print(f"+{earned_xp} XP")

            if player["xp"] >= player["level"] * 100:

                player["xp"] = 0
                player["level"] += 1
                player["max_hp"] += 20
                player["hp"] = player["max_hp"]

                print("\n⭐ LEVEL UP!")
                print(f"Level: {player['level']}")

            break

        # =====================
        # DRAGON ATTACK
        # =====================

        dragon_damage = random.randint(10, 25)

        dragon_damage = max(0, dragon_damage - defense)

        player["hp"] -= dragon_damage

        print(f"{dragon_name} dealt {dragon_damage} damage!")

        if player["hp"] <= 0:

            print("\nYOU DIED!")
            quit()


print("\nCONGRATULATIONS!")
print("You defeated every dragon!")
print("THE END")