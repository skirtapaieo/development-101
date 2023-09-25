
import random
from typing import List

class Deck:
    suits = ["H", "D", "C", "S"]
    values = [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]

    def __init__(self):
        self.cards = []
        self.fill_deck()

    def fill_deck(self):
        for suit in Deck.suits:
            for value in Deck.values:
                card = value + suit
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n: int) -> List[str]:
        n = min(n, len(self.cards))  # Deal all remaining cards if less than n in the deck
        dealt_cards = self.cards[:n]
        self.cards = self.cards[n:]
        return dealt_cards

    def sort_by_suit(self):
        cards_by_suit = {"H": [], "D": [], "C": [], "S": []}

        for card in self.cards:
            suit = card[-1]
            cards_by_suit[suit].append(card)

        self.cards = (
            cards_by_suit["H"] +
            cards_by_suit["D"] +
            cards_by_suit["C"] +
            cards_by_suit["S"]
        )

    def contains(self, card: str) -> bool:
        return card in self.cards

    def copy(self) -> 'Deck':
        new_deck = Deck()
        new_deck.cards = self.cards[:]
        return new_deck

    def get_cards(self) -> List[str]:
        return self.cards[:]

    def __len__(self) -> int:
        return len(self.cards)

    def __str__(self) -> str:
        return ', '.join(self.cards)
