class Player:

    def __init__(self):
        self.bankroll = 1000
        self.hand = []


    def hand_value(self):
        hand_sum = 0
        card_values = sorted([card['n_value'] for card in self.hand])

        for card_value in card_values:
            if card_value == 11 and hand_sum + card_value > 21:
                hand_sum += 1
            else:
                hand_sum += card_value

        return hand_sum