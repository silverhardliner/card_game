from deck import Deck
from card import Card
from card_type_utils import CardTypeUtils as ctu
from player import Player

class Game:

    def __init__(self, ctu_v: ctu, settings = "normal") -> None:
        
        #Some rules
        stop_num = "A"
        self._stop_cards = [Card(s, stop_num, ctu_v) for s in ctu_v.card_suits]
        #self._cards = [Card(s, n, ct) for s in suits for n in numbers]
        
        draw_two_num = 7
        self._draw_two_cards = [Card(s, draw_two_num, ctu_v) for s in ctu_v.card_suits]

        self._start_num_cards = 4

        
        self.show_game_title()
        self._ctu_v = ctu_v
        self._winner = -1
        self._act_player_index = 0

        if settings == "fast":
            self.get_players_fast()
        else:
            self.get_players()
        
        self.create_decks()
        self.give_cards_to_players()

        self.play_game()

        
    def show_game_title(self) -> None:
        """Prints the game title at the start of the game."""
        title = "Welcome to my card game. Developed by Bc. Matej Kopecky.\n"
        print(title)

    def get_players(self) -> None:
        """Gets number of players, their names and ages."""
        self._players = []
        msg = "How many players will play?\n"
        print(msg)
        player_num = int(input("Number of players: "))

        for i in range(player_num):
            name = str(input(f"Player {i+1} name: "))
            age = int(input(f"Player {i+1} age: "))
            player = Player(name, age, self._ctu_v)
            self._players.append(player)

    def get_players_fast(self):
        """Get default players without user input."""
        p1 = Player("Matej", 23, self._ctu_v)
        p2 = Player("Jakub", 20, self._ctu_v)
        p3 = Player("Jirka", 22, self._ctu_v)
        p4 = Player("Honza", 22, self._ctu_v)
        self._players = [p1, p2, p3, p4]

    @property
    def players(self) -> list:
        """Returns the list of players."""
        return self._players
    
    def create_decks(self) -> None:
        """Creates the decks for the game."""
        self._draw_deck = Deck(self._ctu_v, name="Draw deck")
        self._play_deck = Deck(self._ctu_v, deck_type="empty", rotation="face", name="Play deck")
        first_card = self._draw_deck.draw_card()
        self._play_deck.add_card(first_card)

    def give_cards_to_players(self) -> None:
        """Gives cards to players."""
        n_cards = self._start_num_cards
        for i in range(n_cards):
            for j in range(len(self._players)):
                self._players[j].draw_card(self._draw_deck)

    def get_youngest_player_index(self) -> int:
        """Returns the youngest player."""
        youngest_player_index = -1
        age = 100
        for i in range(len(self.players)):
            if self.players[i].age < age:
                age = self.players[i].age
                youngest_player_index = i
        return youngest_player_index
    
    def check_game_end(self) -> int:
        """Checks if there is a winner."""
        for i in range(len(self.players)):
            if len(self.players[i].cards_in_hand) == 0:
                self._winner = i
                break

    def print_winner(self) -> None:
        """Prints winner name after the game is finished."""
        win = self.players[self._winner]
        msg = f"The winner is {win.name}. Congratulations!"
        print(msg)

    def check_player_draw(self, player: Player, deck: Deck) -> bool:
        """Checks if a player needs to draw or can play the card to the deck."""
        top_card = deck.look_at_top_card()
        able_to_play = False
        for card in player.cards_in_hand:
            if card.suit == top_card.suit or card.number == top_card.number:
                able_to_play = True
                break
        
        if able_to_play == False:
            player.draw_card(self._draw_deck)
            msg = f"Player {player.name} draws a card.\n"
            print(msg)

        return able_to_play

    def handle_card(self, player: Player, card: Card, deck: Deck) -> bool:
        """Handles the played card."""
        played_success = False
        top_card = deck.look_at_top_card()
        if card.suit == top_card.suit or card.number == top_card.number:
            player.cards_in_hand.remove(card)
            deck.add_card(card)
            played_success = True
        else:
            print(f"You cannot play this card, choose another!")
        return played_success
    
    def card_functions(self, card: Card) -> None:
        """Handles card functions."""

        # Stun card
        if card in self._stop_cards:
            api = self.next_player()
            print(f"Player {self.players[api].name} is stunned.\n")
        
        # Draw two cards
        elif card in self._draw_two_cards:
            api = self.next_player()
            for _ in range(2):
                self.players[api].draw_card(self._draw_deck)
            print(f"Player {self.players[api].name} draws two cards.\n")

    def next_player(self) -> int:
        self._act_player_index = (self._act_player_index+1) % len(self.players)
        return self._act_player_index
    
    def player_draws_card(self, player: Player):
        player.draw_card(self._draw_deck)
        print(f"Player {player.name} draws a card.\n")

    def play_game(self) -> None:
        """Main game loop."""
        self._act_player_index = self.get_youngest_player_index()

        while(True):
            act_player = self.players[self._act_player_index]
            print(f"Player {act_player.name} turn.")
            
            if self.check_player_draw(act_player, self._play_deck):
                
                play_success = False
                while(not play_success):
                    played_card = act_player.play_card(self._play_deck)

                    # Draw a card
                    if played_card == self._ctu_v.draw_button:
                        self.player_draws_card(act_player)
                        play_success = True
                    else:
                        print(played_card)
                        print()
                        self.card_functions(played_card)
                        play_success = self.handle_card(act_player, played_card, self._play_deck)

            self.check_game_end()
            self.next_player()

            if self._winner != -1:
                self.print_winner()
                break





if __name__ == "__main__":
    ctu_v = ctu()
    my_game = Game(ctu_v, settings="fast")