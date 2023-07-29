import random

# Representing a deck of cards
suits = ["\u2666", "\u2665", "\u2663", "\u2660"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return self.rank + self.suit

    def value(self):
        if self.rank in "JQK":
            return 10
        elif self.rank == "A":
            return 11
        else:
            return int(self.rank)

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self, *cards):
        self.cards = list(cards)

    def value(self):
        val = sum(card.value() for card in self.cards)
        aces = sum(card.rank == "A" for card in self.cards)
        while val > 21 and aces:
            val -= 10
            aces -= 1
        return val

    def add(self, card):
        self.cards.append(card)

    def __repr__(self):
        return ", ".join(map(str, self.cards))

def blackjack():
    player_money = 500

    while player_money > 0:
        print(f"\nYou are starting with ${player_money}. Would you like to play a hand?")
        play = input().lower()
        if play not in ["yes", "y"]:
            print(f"You left with ${player_money}. Goodbye.")
            break

        bet = -1
        while bet < 1 or bet > player_money:
            print("Place your bet: ")
            bet = float(input())
            if bet < 1:
                print("The minimum bet is $1.")
            elif bet > player_money:
                print("You do not have sufficient funds.")

        deck = Deck()
        player = Hand(deck.deal(), deck.deal())
        dealer = Hand(deck.deal(), deck.deal())

        print(f"You are dealt: {player}")
        print(f"The dealer is dealt: {dealer.cards[0]}, Unknown")

        while player.value() < 21:
            print("Would you like to hit or stay?")
            move = input().lower()
            if move in ['hit', 'h']:
                player.add(deck.deal())
                print(f"You are dealt: {player.cards[-1]}")
                print(f"You now have: {player}")
            else:
                break

        if player.value() > 21:
            player_money -= bet
            print(f"Your hand value is over 21, you lose ${bet} :(\n")
            continue

        print(f"The dealer has: {dealer}")
        while dealer.value() < 17:
            dealer.add(deck.deal())
            print(f"The dealer hits and is dealt: {dealer.cards[-1]}")
            print(f"The dealer has: {dealer}")

        if dealer.value() > 21:
            player_money += bet
            print(f"The dealer busts, you win ${bet} :)\n")
            continue
        elif dealer.value() > player.value():
            player_money -= bet
            print(f"The dealer wins, you lose ${bet} :(\n")
        elif dealer.value() < player.value():
            player_money += bet
            print(f"You win ${bet}!\n")
        else:
            print("You tie. Your bet has been returned.\n")

    if player_money == 0:
        print("You've run out of money. Please restart the program to try again. Goodbye.")

blackjack()
