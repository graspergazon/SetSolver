import itertools
import Card

cards = Card.SetDeck().getRandomCards(12)

def get_third_card(card_one, card_two):
    new_color = ""
    new_number = 0
    new_symbol = ""
    new_shading = ""
    if card_one.color == card_two.color:
        new_color = card_one.color
    else:
        new_color = list(set(Card.SetDeck().colors) - set([card_one.color, card_two.color]))[0]
    if card_one.number == card_two.number:
        new_number = card_one.number
    else:
        new_number = list(set(Card.SetDeck().numbers) - set([card_one.number, card_two.number]))[0]
    if card_one.symbol == card_two.symbol:
        new_symbol = card_one.symbol
    else:
        new_symbol = list(set(Card.SetDeck().symbols) - set([card_one.symbol, card_two.symbol]))[0]
    if card_one.shading == card_two.shading:
        new_shading = card_one.shading
    else:
        new_shading = list(set(Card.SetDeck().shadings) - set([card_one.shading, card_two.shading]))[0]
    return Card.Card(new_color, new_number, new_symbol, new_shading)

c = list(itertools.combinations(cards, 2))
for i in c:
    third_card = get_third_card(i[0],i[1])
    if third_card in cards:
        print("Yeah, there's a SET:")
        print(i[0])
        print(i[1])
        print(third_card)
        print("\n")
