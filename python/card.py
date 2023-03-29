from card_type_utils import CardTypeUtils as ctu


class Card:
    """
    The Card class represents a single playing card and is initialised by passing a suit, a number and card type struct.
    """

    def __init__(self, suit: str, number: str, card_type: ctu) -> None:
        """
        Init function of card. Card takes suit, number and card type. 
        Card type is different class with card settings.
        """
        self._numbers = card_type.card_numbers
        self._letter_numbers = card_type.letter_numbers
        self._suits = card_type.card_suits

        # Card types methods
        self._suit_check = card_type.suit_check
        self._number_check = card_type.number_check

        if self._suit_check(suit):
            self._suit = suit
        if self._number_check(number):
            self._number = str(number).capitalize()
        # if self.game_check(game):
            # self._game = game
        # self._value = self.card_value()

    def __repr__(self) -> str:
        """
        Prints number and suit of the card.
        """
        return str(self._number) + " of " + self._suit
        # return str(self._number) + " of " + self._suit + ", game: " + self._game + ", value: " + str(self._value)

    def __eq__(self, other) -> bool:
        """
        Compares two cards with each other.
        """
        ret = None
        if not isinstance(other, Card):
            ret = NotImplemented
        else:
            ret = self._suit == other.suit and self._number == other.number
        return ret

    def to_string(self) -> str:
        """
        Returns name of the card with "of" in between.
        """
        ret = str(self._number) + " of " + self._suit
        return ret

    # SUIT
    @property
    def suit(self) -> str:
        """Returns suit of card."""
        return self._suit

    @suit.setter
    def suit(self, suit: str) -> None:
        """Sets suit of card."""
        if self._suit_check(suit):
            self._suit = suit

    @property
    def suits(self) -> list:
        """Returns all card suits."""
        return self._suits

    # NUMBER

    @property
    def number(self) -> str:
        """Returns card number."""
        return self._number

    @number.setter
    def number(self, number: str) -> None:
        """Sets card number."""
        if self._number_check(number):
            self._number = str(number)

    @property
    def numbers(self) -> list:
        """Returns all card numbers."""
        return self._numbers

    # GAME
    # @property
    # def game(self) -> str:
    #     return self._game

    # @game.setter
    # def game(self, game: str) -> None:
    #     if self.game_check(game):
    #         self._game = str(game)
    #         self._value = self.card_value()

    # def game_check(self, game) -> bool:
    #     ret = False
    #     if game in self._game_types:
    #         ret = True
    #     else:
    #         raise Exception("That is not a valid game!")
    #     return ret

    # VALUE
    # @property
    # def value(self) -> int:
    #     return self._value

    # def card_value(self) -> int:
    #     ret = None
    #     card_base = 11
    #     if self._game == "standart" and self._number in self._letter_numbers:
    #         ret = 10
    #     elif self._game == "ordered" and self._number in self._letter_numbers:
    #         index = self._letter_numbers.index(self._number)
    #         ret = index + card_base
    #     else:
    #         ret = self._number
    #     return ret


if __name__ == "__main__":
    game_type = ctu()
    new_card = Card("spades", 2, game_type)
    card2 = Card("spades", "2", game_type)
    print(new_card == card2)
