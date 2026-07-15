import random

class Card:
    """
    Represents a single playing card with its suit and rank
    """
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    """
    Represents a standard 52-card playing deck.
    Handles the generation, shuffling and dealing of cards.
    """

    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        for c_suit in suits:
            for c_rank in ranks:
                new_card = Card(c_suit, c_rank)
                self.cards.append(new_card)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()


class Hand:
    """
    Represents a single unique Hand of cards for each player.
    Handles the addition of cards and the final calculation of the value of the hand.
    """

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        total = 0
        aces = 0
        for card in self.cards:
            if card.rank in ['Jack', 'Queen', 'King']:
                total += 10
            elif card.rank == 'Ace':
                total += 11
                aces+=1
            else:
                total += int(card.rank)

        # Corrects the value of the aces appropriately
        while (total > 21) and (aces > 0):
            total -= 10
            aces -= 1
        
        return total
    