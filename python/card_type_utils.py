class CardTypeUtils:

    def __init__(self, card_type="standart") -> None:
        """CardTypeUtils is a class with settings of cards. The only default setting implemented is named standart."""
        if card_type == "standart":
            letter_numbers = ["J", "Q", "K", "A"]
            self._card_type = card_type
            self._card_numbers = [str(n)
                                  for n in range(2, 11)] + letter_numbers
            self._letter_numbers = letter_numbers
            self._card_suits = ["hearts", "clubs", "diamonds", "spades"]
            self._card_suits_letter = [suit[0] for suit in self._card_suits]

            self._draw_button = "x"

    def __repr__(self) -> str:
        """Prints card settings."""
        card_set = "CARD SETTINGS:\n"
        title = "Card type: " + self._card_type + "\n"
        numbers = "Card numbers:\n" + ", ".join(self._card_numbers) + "\n"
        suits = "Card suits:\n" + ", ".join(self._card_suits) + "\n"
        ret = card_set + title + numbers + suits
        return ret

    @property
    def card_numbers(self) -> list:
        """Returns card numbers."""
        return self._card_numbers

    @property
    def card_suits(self) -> list:
        """Returns card suits."""
        return self._card_suits

    @property
    def letter_numbers(self) -> list:
        """Returns card letter numbers."""
        return self._letter_numbers
    
    @property
    def start_num_cards(self) -> int:
        """Return the starting number of cards."""
        return self._start_num_cards
    
    @property
    def draw_button(self) -> str:
        """Return the char for drawing a card."""
        return self._draw_button

    def suit_check(self, suit: str, raise_ex=True) -> bool:
        """Checks if input suit is valid suit. Returns bool."""
        ret = False
        if suit in self._card_suits:
            ret = True
        else:
            msg = "That is not a suit!"
            if raise_ex:
                raise Exception(msg)
            # print(msg)
        return ret

    def number_check(self, number, raise_ex=True) -> bool:
        """Checks if input number is valid card number. Returns bool."""
        ret = False
        number = str(number).capitalize()
        if number.isalpha() and number in self._letter_numbers:
            ret = True
        elif number.isnumeric() and 2 <= int(number) <= 10:
            ret = True
        else:
            msg = "That is not a card number!"
            if raise_ex:
                raise Exception(msg)
            # print(msg)
        return ret

    def user_card_input(self, str_in: str):
        """
        The user has two options as input. First is full name of the card with "of" in the middle (3 of clubs/clubs of 3).
        Second is just number and first letter of the suit (3c/c3).
        """
        number = None
        suit = None
        str_in_len = len(str_in)

        if str_in_len == 1:
            if str_in == self._draw_button:
                suit = str_in
        elif str_in_len == 2:
            list_in = list(str_in)
            for i in list_in:
                if self.number_check(i, False):
                    number = i
                else:
                    suit = self.letter_to_suit(i)

        elif str_in_len == 3:
            searched_str = "10"
            ten = str_in.find(searched_str)
            if ten != -1:
                number = searched_str
                rest = str_in[:ten] + str_in[ten+len(searched_str):]
                suit = self.letter_to_suit(rest)

        else:
            splitted = str_in.split(" of ")
            for i in splitted:
                if self.number_check(i, False):
                    number = i
                elif self.suit_check(i, False):
                    suit = i

        return (suit, number)

    def letter_to_suit(self, letter: str) -> str:
        """Converts starting letter of suit to valid suit. If the input is not starting letter of suit returns None."""
        suit = None
        csl = self._card_suits_letter
        for i in range(len(csl)):
            if letter.lower() == csl[i]:
                suit = self._card_suits[i]
        return suit


if __name__ == "__main__":
    ctu = CardTypeUtils()
    print(ctu)
    card_input = "h2"
    print(ctu.user_card_input(card_input))
