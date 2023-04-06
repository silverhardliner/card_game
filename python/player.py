from deck import Deck
from card import Card
from card_type_utils import CardTypeUtils as ctu


class Player:

    def __init__(self, name: str, age: int, card_type: ctu) -> None:
        """The player class represents a game player and is initialised by parameters below:
        name: name of the player
        age: age of the player
        card_type: card type settings
        """
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
        """Prints player name with his cards."""
        card_str = self.card_string()
        title = "PLAYER:\n"
        return f"{self._name} {self._age} with cards:\n {card_str}"#title + self._name +  + " with cards:\n" + card_str

    @property
    def name(self) -> str:
        """Returns players name."""
        return self._name

    @property
    def age(self) -> int:
        """Returns player's age."""
        return self._age
    
    @property
    def cards_in_hand(self) -> list:
        """Returns players cards in hand."""
        return self._cards_in_hand

    def card_string(self) -> str:
        """Creates a string of player's cards."""
        card_str = ', '.join(one_card.to_string()
                             for one_card in self._cards_in_hand)
        return card_str

    def draw_card(self, deck: Deck) -> None:
        """Draws a card from deck."""
        new_card = deck.draw_card()
        self._cards_in_hand.append(new_card)

    def play_card(self, target_deck: Deck) -> Card:
        """Takes input from user as player, handles the input and play the card to the target deck."""
        cond = True
        while cond:
            print(f"Top card: {target_deck.look_at_top_card()}")
            print("Choose a card!\n" + self.card_string())
            input_card = str(input("Card: "))
            suit, number = self._user_card_input(input_card)
            if suit and number:
                played_card = Card(suit, number, self._card_type)
                print(played_card)
                print()

                c1 = self.handle_card(played_card, target_deck)
                c2 = played_card in self._cards_in_hand

                if c1 and c2:
                    cond = False
            else:
                print("This card is not in your hand, choose another!")

        self._cards_in_hand.remove(played_card)
        return played_card
    
    def handle_card(self, card: Card, deck: Deck) -> bool:
        """Handles the played card."""
        played_success = False
        top_card = deck.look_at_top_card()
        if card.suit == top_card.suit or card.number == top_card.number:
            deck.add_card(card)
            played_success = True
        else:
            print(f"You cannot play this card, choose another!")
        return played_success


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
