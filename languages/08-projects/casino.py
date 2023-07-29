import random

# Blackjack game
def blackjack():
    print("\nWelcome to Blackjack!")

    player_money = 500
    while player_money > 0:
        bet_amount = int(input("How much would you like to bet? "))
        if 0 < bet_amount <= player_money:
            player_card = random.randint(1, 10)
            dealer_card = random.randint(1, 10)
            if player_card > dealer_card:
                print("You won!")
                player_money += bet_amount
            else:
                print("You lost.")
                player_money -= bet_amount
            print(f"You now have ${player_money}")
        else:
            print("Invalid bet amount.")

    print("You've run out of money. Leaving Blackjack.\n")

# Roulette game
def roulette():
    print("\nWelcome to Roulette!")

    player_money = 500
    while player_money > 0:
        bet_amount = int(input("How much would you like to bet? "))
        if 0 < bet_amount <= player_money:
            bet_number = int(input("What number would you like to bet on? (0-36, 00): "))
            result = random.randint(0, 36)
            if bet_number == result:
                print("You won!")
                player_money += bet_amount
            else:
                print("You lost.")
                player_money -= bet_amount
            print(f"You now have ${player_money}")
        else:
            print("Invalid bet amount.")

    print("You've run out of money. Leaving Roulette.\n")

# Slots game
def slots():
    print("\nWelcome to Slots!")

    player_money = 500
    while player_money > 0:
        bet_amount = int(input("How much would you like to bet? "))
        if 0 < bet_amount <= player_money:
            result = random.choice(['win', 'lose'])
            if result == 'win':
                print("You won!")
                player_money += bet_amount
            else:
                print("You lost.")
                player_money -= bet_amount
            print(f"You now have ${player_money}")
        else:
            print("Invalid bet amount.")

    print("You've run out of money. Leaving Slots.\n")

def play_casino():
    while True:
        print("Welcome to the Casino! Choose your game: (1) Blackjack, (2) Roulette, (3) Slots, (4) Quit")
        choice = int(input())
        if choice == 1:
            blackjack()
        elif choice == 2:
            roulette()
        elif choice == 3:
            slots()
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

play_casino()
