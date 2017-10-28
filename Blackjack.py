from CardSet import CardSet, check_cards_total_value
from random import uniform


def check_more_card(cards):
    """
    Returns whether or not the computer should pick a new card
    :param cards: cards the computer already has (list)
    :return: pick a new one or not (bool)
    """

    probability = {
        15: 0.03,
        16: 0.025,
        17: 0.02,
        18: 0.015,
        19: 0.01,
        20: 0.005
    }

    total_value = check_cards_total_value(cards)
    if total_value >= 21:
        return False
    elif total_value < 15:
        return True
    else:
        random_probability = uniform(0, 1)
        if random_probability <= probability[total_value]:
            return True
        else:
            return False


def show_cards(cards):
    """
    Show the formatted name of the cards in a list
    :param cards: list of cards
    """
    for card in cards:
        print("\t", card.get_formatted_name())


print("Lancement de la partie...")
card_set = CardSet()

shuffle = True
while shuffle:
    p = input("Voulez-vous mélanger le paquet de cartes? (y/n) > ")
    if p is 'y':
        card_set.shuffle_set()
    else:
        shuffle = False

print("Paquet mélangé. Vous et l'ordinateur recevez 2 cartes.")

cards_player = [card_set.pick_card(), card_set.pick_card()]
cards_ia = [card_set.pick_card(False), card_set.pick_card(False)]

print("-----")
for card in cards_player:
    print(card.get_formatted_name())
print("-----")

pick_new_card = True
while pick_new_card:
    p = input("Voulez-vous piocher une nouvelle carte? (y/n) > ")
    if p is 'y':
        if card_set.is_empty():
            print('Le paquet de cartes est vide.')
            pick_new_card = False
        else:
            new_card = card_set.pick_card()
            cards_player.append(new_card)
            print("Vous avez pioché : {}".format(new_card.get_value()))

            if check_cards_total_value(cards_player) > 21:
                print("Vous avez dépassé 21, vous avez perdu!")
                pick_new_card = False
    else:
        pick_new_card = False

card_picked = 0
while check_more_card(cards_ia):
    if not card_set.is_empty():
        card_picked += 1
        new_card = card_set.pick_card(False)
        cards_ia.append(new_card)

        if check_cards_total_value(cards_ia) > 21:
            print("L'IA a dépassé 21, vous avez gagné!")

total_player = check_cards_total_value(cards_player)
total_ia = check_cards_total_value(cards_ia)
print("Vos points : {} - Les points de l'IA : {}".format(total_player, total_ia))
print("Cartes de l'IA:")
show_cards(cards_ia)
print("Vos cartes:")
show_cards(cards_player)

if total_player <= 21 and total_ia <= 21:
    if check_cards_total_value(cards_player) > check_cards_total_value(cards_ia):
        print("Vous avez gagné!")
    elif check_cards_total_value(cards_player) < check_cards_total_value(cards_ia):
        print("Vous avez perdu!")
    else:
        print("Egalité entre vous et l'ordinateur!")
