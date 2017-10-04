from random import shuffle


class Deck:

    def __init__(self):
        self.cards = self.create_cards()


    def create_cards(self):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['C', 'D', 'H', 'S']
        return [{'value': v, 'suit': s} for v in values for s in suits]


    def draw(self, n):
        pass


    def shuffle(self):
        shuffle(self.cards)