from deck import Deck
from card import Card
from card_type_utils import CardTypeUtils as ctu
from player import Player

class Game:

    def __init__(self, card_type: ctu) -> None:
        self.show_game_title()
        self._player_names, self._player_age = self.get_players()
        print(self._player_names)
        print(self._player_age)
        self.players = self.make_players()

    def show_game_title(self) -> None:
        title = "Welcome to my card game. Developed by Bc. Matej Kopecky.\n"
        print(title)

    def get_players(self) -> list:
        msg = "How many players will play?\n"
        print(msg)
        player_num = int(input("Number of players: "))
        print()

        player_names = []
        player_age = []
        for i in range(player_num):
            name = str(input(f"Player {i+1} name: "))
            player_names.append(name)
            age = int(input(f"Player {i+1} age: "))
            player_age.append(age)
            print()

        return player_names, player_age

    def make_players(self) -> list:
        gct = ctu()
        players = []

        for i in range(len(self._player_names)):
            name = self._player_names[i]
            age  = self._player_age[i]
            player = Player(name, age, gct)
            players.append(player)

        return players


if __name__ == "__main__":
    gct = ctu()
    my_game = Game(gct)
    print(my_game.players[0])