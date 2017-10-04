from Deck import Deck


class Blackjack:

    def __init__(self):
        self.player_bankroll = 1000
        self.bet_amount = 0
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = []
        self.dealer_hand = []


    def start_game(self):
        print('Welcome to blackjack!\n')

        while self.keep_playing():
            self.take_bets()
            self.deal_hands()
            self.play_out_hands()
            self.make_payouts()

        print('Thanks for playing!')


    def keep_playing(self):
        return self.player_bankroll > 0


    def take_bets(self):
        print('Available bankroll: {}'.format(self.player_bankroll))
        bet_amount = int(input('How much would you like to bet?\n'))
        self.player_bankroll -= bet_amount
        self.bet_amount = bet_amount


    def deal_hands(self):
        self.player_hand = self.deck.draw(2)
        self.dealer_hand = self.deck.draw(2)


    def play_out_hands(self):
        pass


    def make_payouts(self):
        pass