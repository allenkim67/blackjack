from random import shuffle


class Deck:

    def __init__(self):
        self.cards = self.create_cards()


    def create_cards(self):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['C', 'D', 'H', 'S']
        return [{'value': v,
                 'suit': s,
                 'n_value': self.n_value(v)} for v in values for s in suits]


    def n_value(self, v):
        if v in ['J', 'Q', 'K']:
            return 10
        elif v == 'A':
            return 11
        else:
            return int(v)


    def draw(self, n):
        drawn_cards = self.cards[-n:]
        self.cards = self.cards[:-n]
        return drawn_cards


    def shuffle(self):
        shuffle(self.cards)