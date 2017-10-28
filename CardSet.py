from Card import Card
from random import shuffle, randint


class CardSet(object):
    def __init__(self):
        self.card_set = []
        for i in range(1, 14):
            for n in range(4):
                card = Card(i, n)
                self.card_set.append(card)

    def shuffle_set(self):
        """
        Shuffle the set of cards
        """
        shuffle(self.card_set)

    def pick_card(self, player=True):
        """
        Returns a random card from the set
        :return: a random card (Card)
        """
        if not self.is_empty():
            card = self.card_set[randint(0, len(self.card_set) - 1)]
            if card.value == 1 and player:
                card.set_value(choose_as_value())
            self.card_set.remove(card)
            return card
        else:
            return None

    def is_empty(self):
        """
        Returns whether or not a card set is empty
        :return: empty or not (bool)
        """

        return len(self.card_set) == 0


def check_cards_total_value(cards):
    """
    Returns the total value of your hand
    :param cards: list of the cards you already have (list)
    :return: the total value of your hand (int)
    """

    value = 0
    for card in cards:
        value += card.get_value()

    return value


def choose_as_value():
    """
    Choose the AS value
    :return: as value
    """

    chosen = False
    while not chosen:
        value = int(input("Vous avez pioché un AS. 1 ou 11 ?"))
        if value == 1 or value == 11:
            return value

