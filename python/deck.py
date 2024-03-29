from card import Card
from card_type_utils import CardTypeUtils as ctu
import random


class Deck:

    def __init__(self, card_type: ctu, deck_type="shuffled", rotation="back", name="main") -> None:
        """The deck class represents a deck of cards and is initialised by parameters below:
        card_type: struct that holds info about cards
        deck_type: shuffled will shuffle the deck
        rotation: if the deck is face up or back up
        name: name of the deck
        """
        self._card_type = card_type
        self._card_numbers = card_type.card_numbers
        self._letter_numbers = card_type.letter_numbers
        self._card_suits = card_type.card_suits

        self._cards = []
        self._number_of_cards = 0
        self._name = name
        self._rotations = ["face", "back"]

        if self.check_rotation(rotation):
            self._deck_rotation = rotation
        if deck_type == "empty":
            pass
        else:
            self.populate()
            if deck_type == "shuffled":
                self.shuffle()

    def __repr__(self) -> str:
        """Prints deck name with the number of cards."""
        title = "DECK:\n"
        return title + self._name.capitalize() + " deck with " + str(self._number_of_cards) + " cards"

    def check_rotation(self, rotation: str) -> bool:
        """Checks if the rotation option input is correct."""
        ret = False
        if rotation in self._rotations:
            ret = True
        else:
            raise Exception("That is not deck rotation!")
        return ret

    def populate(self) -> None:
        """Populates deck woth cards."""
        suits = self._card_suits
        numbers = self._card_numbers
        ct = self._card_type
        self._cards = [Card(s, n, ct) for s in suits for n in numbers]
        self._number_of_cards = len(self._cards)

    def shuffle(self) -> None:
        """Shuffles cards in deck."""
        random.shuffle(self._cards)

    def print_cards(self) -> None:
        """Prints cards."""
        print(self._cards)

    def card_in_deck(self, searched_card: Card) -> bool:
        """Checks if a card is in deck."""
        ret = False
        if any(card == searched_card for card in self._cards):
            print('Card is in the ' + self._name + ' deck.')
            ret = True
        else:
            print('Card is not in the ' + self._name + ' deck.')
        return ret

    @property
    def number_of_cards(self) -> int:
        """Returns number of cards."""
        return self._number_of_cards

    def draw_card(self, position="top") -> Card:
        """Draws a card from specific position."""
        if self.number_of_cards > 0:
            card_index = self.get_index(position)
            new_card = self._cards.pop(card_index)
            self._number_of_cards -= 1
            return new_card
        else:
            print(self._name.capitalize() + "deck is empty.")
            return None

    def add_card(self, added_card: Card, position="top") -> None:
        """Adds a card to a specific position."""
        card_index = self.get_index(position)
        if card_index == -1:
            card_index = self._number_of_cards
        self._cards.insert(card_index, added_card)
        self._number_of_cards += 1

    def get_index(self, position) -> int:
        """Converts position input to list index for card drawing and adding."""
        card_index = 0
        if isinstance(position, int):
            card_index = position
        else:
            if position == "bottom":
                card_index = -1
            elif position == "random":
                card_index = random.randrange(self._number_of_cards)
        return card_index

    @property
    def deck_rotation(self) -> str:
        """Returns deck rotation."""
        return self._deck_rotation

    @deck_rotation.setter
    def deck_rotation(self, rotation: str) -> None:
        """Sets deck rotation."""
        if self.check_rotation(rotation):
            self._deck_rotation = rotation

    def look_at_top_card(self) -> Card:
        """Looks at the top deck card if the deck is rotated face up."""
        if self._deck_rotation == "face":
            return self._cards[0]
        else:
            print("Cannot see top card at the " + self._name + " deck.")
            return None

    @property
    def name(self) -> str:
        """Returns the name of the deck."""
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """Sets the name of the deck."""
        self._name = name

if __name__ == "__main__":
    gct = ctu()
    my_deck = Deck(gct)
    print(my_deck)
