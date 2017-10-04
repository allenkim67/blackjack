class Blackjack:

    def __init__(self):
        self.player_bankroll = 1000


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
        pass


    def deal_hands(self):
        pass


    def play_out_hands(self):
        pass


    def make_payouts(self):
        pass