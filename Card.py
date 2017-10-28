class Card(object):
    """ Object representing an card from a card set """
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def get_color(self):
        """
        Returns the color of the card
        :return: color of the card (int)
        """
        return self.color

    def get_value(self):
        """
        Returns the value of the card
        :return: value of the card (int)
        """
        if self.value > 10:
            return 10
        else:
            return self.value

    def set_value(self, value):
        """
        Set the value of the card
        :param value: value of the card (int)
        """
        self.value = value

    def get_formatted_name(self):
        """
        Returns the formatted name of a card
        :return: formatted name of the card (str)
        """
        return formatted_name(self.value, self.color)


def formatted_name(value, color):
    """
    Returns the formatted name of a card
    :param value: value of the card (int)
    :param color: value of the card (int)
    :return: formatted name of the card (str)
    """

    names = ['As', 'Valet', 'Dame', 'Roi']
    colors = ['Coeur', 'Carreaux', 'Trèfle', 'Pique']

    name = ''
    if 14 >= value > 10 or value == 1:
        name += names[0] if value == 1 else names[value - 10]
    else:
        name += str(value)

    name += ' de '

    if 0 <= color < 4:
        name += colors[color]

    return name
