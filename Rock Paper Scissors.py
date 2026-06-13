import random

LEVELS = {
    1: {"start": 0,   "goal": 50,  "xp_win": 10, "xp_lose": 0},
    2: {"start": 50,  "goal": 100, "xp_win": 10, "xp_lose": -10},
    3: {"start": 100, "goal": 150, "xp_win": 10, "xp_lose": -25},
    4: {"start": 150, "goal": 200, "xp_win": 50, "xp_lose": -50},
    5: {"start": 200, "goal": 300, "xp_win": 50, "xp_lose": -200}
}

MAX_XP = 300

# Statistics
wins = 0
losses = 0
draws = 0


def get_level(xp):
    if xp >= 200:
        return 5
    elif xp >= 150:
        return 4
    elif xp >= 100:
        return 3
    elif xp >= 50:
        return 2
    return 1


def show_status(xp):
    level = get_level(xp)
    config = LEVELS[level]

    start = config["start"]
    goal = config["goal"]

    if level == 5 and xp >= MAX_XP:
        progress = 1
    else:
        progress = (xp - start) / (goal - start)

    bar_length = 20
    filled = int(progress * bar_length)

    bar = "█" * filled + "░" * (bar_length - filled)

    total_games = wins + losses + draws

    print("\n" + "═" * 40)
    print(f"Level : {level}/5")
    print(f"XP    : {xp}/{MAX_XP}")
    print(f"[{bar}]")

    if total_games > 0:
        win_rate = (wins / total_games) * 100
        print(f"\nGames Played : {total_games}")
        print(f"Wins         : {wins}")
        print(f"Losses       : {losses}")
        print(f"Draws        : {draws}")
        print(f"Win Rate     : {win_rate:.1f}%")

    print("═" * 40)


def determine_winner(user, computer):
    if user == computer:
        return "draw"

    if (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        return "win"

    return "lose"


def play_round(xp):
    global wins, losses, draws

    level = get_level(xp)
    config = LEVELS[level]

    print("\n" + "─" * 40)
    print(f"Level {level}")
    print(f"Win Reward : +{config['xp_win']} XP")
    print(f"Lose Penalty : {config['xp_lose']} XP")
    print("─" * 40)

    choices = ["rock", "paper", "scissors"]

    user = input(
        "Choose (rock / paper / scissors): "
    ).lower().strip()

    if user not in choices:
        print("Invalid choice!")
        return xp

    computer = random.choice(choices)

    print(f"\nComputer chose: {computer}")

    result = determine_winner(user, computer)

    if result == "draw":
        draws += 1
        print("🤝 Draw!")

    elif result == "win":
        wins += 1
        xp += config["xp_win"]
        print(f"✅ You Win! +{config['xp_win']} XP")

    else:
        losses += 1
        xp += config["xp_lose"]

        floor = config["start"]
        xp = max(xp, floor)

        print(f"❌ You Lose! {config['xp_lose']} XP")

    xp = min(xp, MAX_XP)

    return xp


# ===============================
# Main Program
# ===============================

xp = 0

print("═" * 45)
print("🎮 ROCK PAPER SCISSORS RPG")
print("═" * 45)

while True:

    level = get_level(xp)

    print("\nMenu")
    print("1. Play")
    print("2. Show Status")
    print("3. Reset Progress")
    print("4. Quit")

    choice = input("\nSelect option: ").strip()

    if choice == "1":

        old_level = level

        xp = play_round(xp)

        new_level = get_level(xp)

        if new_level > old_level:
            print(f"\n🎉 LEVEL UP!")
            print(f"You reached Level {new_level}!")

        if xp >= MAX_XP:
            print("\n🏆 CONGRATULATIONS!")
            print("You completed the game!")
            show_status(xp)
            break

    elif choice == "2":
        show_status(xp)

    elif choice == "3":

        xp = 0
        wins = 0
        losses = 0
        draws = 0

        print("\n🔄 Progress Reset!")

    elif choice == "4":
        print("\n👋 Goodbye!")
        break

    else:
        print("\n❌ Invalid option!")