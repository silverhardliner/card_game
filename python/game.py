from deck import Deck
from card import Card
from card_type_utils import CardTypeUtils as ctu
from player import Player

class Game:

    def __init__(self, card_type: ctu) -> None:
        self.show_game_title()
        self.players = self.get_players()

    def show_game_title(self) -> None:
        title = "Welcome to my card game. Developed by Bc. Matej Kopecky.\n"
        print(title)

    def get_players(self) -> list:
        gct = ctu()
        players = []
        msg = "How many players will play?\n"
        print(msg)
        player_num = int(input("Number of players: "))

        for i in range(player_num):
            name = str(input(f"Player {i+1} name: "))
            age = int(input(f"Player {i+1} age: "))
            player = Player(name, age, gct)
            players.append(player)

        return players


if __name__ == "__main__":
    gct = ctu()
    my_game = Game(gct)
    print(my_game.players[0])