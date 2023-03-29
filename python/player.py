from deck import Deck
from card import Card
from card_type_utils import CardTypeUtils as ctu


class Player:

    def __init__(self, name: str, age: int, card_type: ctu) -> None:
        self._cards_in_hand = []
        self._name = name
        self._age = age

        # Card types
        self._card_type = card_type
        self._card_numbers = card_type.card_numbers
        self._letter_numbers = card_type.letter_numbers
        self._card_suits = card_type.card_suits

        # Card types methods
        self._suit_check = card_type.suit_check
        self._number_check = card_type.number_check
        self._user_card_input = card_type.user_card_input

    def __repr__(self) -> str:
        card_str = self.card_string()
        return self._name + " with cards:\n" + card_str

    def card_string(self) -> str:
        card_str = ', '.join(one_card.to_string()
                             for one_card in self._cards_in_hand)
        return card_str

    def draw_card(self, deck: Deck) -> None:
        new_card = deck.draw_card()
        self._cards_in_hand.append(new_card)

    def play_card(self, target_deck: Deck) -> Card:
        cond = True
        while cond:
            print("Choose a card!\n" + self.card_string())
            input_card = str(input("Card: "))
            suit, number = self._user_card_input(input_card)
            if suit and number:
                played_card = Card(suit, number, self._card_type)
                print(played_card)
                if played_card in self._cards_in_hand:
                    cond = False
            else:
                print("This card is not in your hand, choose another!")

        target_deck.add_card(played_card)
        self._cards_in_hand.remove(played_card)
        return played_card


if __name__ == "__main__":
    game_card_type = ctu()

    draw_deck = Deck(game_card_type)
    play_deck = Deck(game_card_type, deck_type="empty",
                     rotation="face", name="play")

    my_player = Player("Matej", 23, game_card_type)
    for _ in range(5):
        my_player.draw_card(draw_deck)
    played_card = my_player.play_card(play_deck)
    print(my_player)
    print(play_deck.number_of_cards)
    play_deck.print_cards()
    draw_deck.card_in_deck(played_card)
    play_deck.card_in_deck(played_card)
