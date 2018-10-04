import collections
import random

Card = collections.namedtuple('Card', ['color', 'number', 'symbol', 'shading'])


class SetDeck:
    colors = 'red green purple'.split()
    numbers = [n for n in range(1, 4)]
    symbols = 'diamond squiggle oval'.split()
    shadings = 'solid striped open'.split()

    def __init__(self):
        self._cards = [Card(color, number, symbol, shading)
                       for color in self.colors
                       for number in self.numbers
                       for symbol in self.symbols
                       for shading in self.shadings]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def getRandomCards(self, number):
        return random.sample(list(self._cards),12)