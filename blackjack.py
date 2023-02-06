import random
from random import shuffle


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def card_value(self):
        if self.rank in "TJQK":
            return 10
        else:
            return " A23456789".index(self.rank)

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        res = 0
        aces = 0
        for card in self.cards:
            res += card.card_value()
            if card.get_rank() == "A":
                aces += 1
        if res + aces * 10 <= 21:
            res += aces * 10
        return res

    def __str__(self):
        def __str__(self):
            text = "%s's contains:\n" % self.name
            for card in self.cards:
                text += str(card) + " "
            text += "\nHand value: " + str(self.get_value())
            return text


class Desk:
    def __init__(self):
        ranks = "23456789TJQA"
        suits = "DCHS"
        self.cards = [Card(r,s) for r in ranks for s in suits]
        shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


def new_game():
    d = Desk()
    player_hand = Player("Player")
    dealer_hand = Player("Dealer")
    player_hand.add_card(d.deal_card())
    player_hand.add_card(d.deal_card())
    dealer_hand.add_card(d.deal_card())

    print (dealer_hand.get_value())
    print ("="*20)
    print (player_hand)

    in_game = True
    while player_hand.get_value() < 21:
        ans = input("Hit or stand? (h/s) ")
        if ans == "h":
            player_hand.add_card(d.deal_card())
        print(player_hand)
        if player_hand.get_value() > 21:
            print ("You lose")
            in_game = False
        else:
            print("You stand")
            break
        print("=" * 20)
        if in_game:
            while dealer_hand.get_value() < 17:
                dealer_hand.add_card(d.deal_card())
            print (dealer_hand)
            if dealer_hand.get_value() > 21:
                print ("Dealer lose")
                in_game = False

        if in_game:
            if player_hand.get_value() > dealer_hand.get_value():
                print ("Player win")
            else:
                print ("Dealer win")


new_game()



