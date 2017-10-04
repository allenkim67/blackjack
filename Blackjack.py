from Deck import Deck
from Player import Player


class Blackjack:

    def __init__(self):
        self.bet_amount = 0
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player()
        self.dealer = Player()


    def start_game(self):
        print('Welcome to blackjack!\n')

        while self.keep_playing():
            self.take_bets()
            self.deal_hands()
            self.play_out_hands()
            self.make_payouts()

        print('Thanks for playing!')


    def keep_playing(self):
        return self.player.bankroll > 0


    def take_bets(self):
        print('Available bankroll: {}'.format(self.player.bankroll))
        bet_amount = int(input('How much would you like to bet?\n'))
        self.player.bankroll -= bet_amount
        self.bet_amount = bet_amount


    def deal_hands(self):
        self.player.hand = self.deck.draw(2)
        self.dealer.hand = self.deck.draw(2)


    def play_out_hands(self):
        blackjack = self.dealer.hand_value() == 21 or self.player.hand_value() == 21

        if not blackjack:
            while self.player.hand_value() < 22:
                self.print_hands(hide_dealer_card=True)
                action = input('Enter H for hit or S for stay.\n')
                if action == 'H':
                    self.player.hand += self.deck.draw(1)
                elif action == 'S':
                    while self.dealer.hand_value() < 17:
                        self.dealer.hand += self.deck.draw(1)
                    break


    def print_hands(self, hide_dealer_card=False):
        dealer_hand = [card['str'] for card in self.dealer.hand]
        if hide_dealer_card:
            dealer_hand[0] = '(hidden)'
        player_hand = [card['str'] for card in self.dealer.hand]

        print('Dealer has: {}'.format(' '.join(dealer_hand)))
        print('Player has: {}'.format(' '.join(player_hand)))


    def make_payouts(self):
        self.print_hands()

        p_val = self.player.hand_value()
        d_val = self.dealer.hand_value()

        if d_val > 21 or d_val < p_val < 22:
            print('You win!')
            self.player.bankroll -= self.bet_amount * 2
        elif d_val == p_val:
            print('Push!')
            self.player.bankroll -= self.bet_amount
        else:
            print('You lose.')