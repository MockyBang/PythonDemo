# -*- coding: utf-8 -*
import collections
from random import choice

# 用 colections.nametuple 构建一个简单类来表示一张纸牌
# nametuple 用以构建只有少数属性但是没有方法的对象，比如数据库条目
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds club hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, club=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    deck = FrenchDeck()
    # print(deck._cards)
    print(len(deck))
    print(deck[0], deck[-1])
    print(choice(deck))
    print(choice(deck))
    print(choice(deck))
    print(deck[:3])
    print(deck[12::13])
    print('*' * 50)
    print('正向迭代')
    for card in deck:
        print(card)
    print('*' * 50)
    print('反向迭代')
    for card in reversed(deck):
        print(card)
    print('*' * 50)
    print(Card('Q', 'hearts') in deck)
    print(Card('7', 'beasts') in deck)
    print('*' * 50)
    print('根据点数大小排序')
    for card in sorted(deck, key=spades_high):
        print(card)
