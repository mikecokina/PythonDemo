"""
This program should deal a game of Poker but has a bug. Explain and fix it by adding one very short line of code
anywhere, also explain both list comprehensions.

number represents unicode playing cards symbols
for visual representation of problem, see img.jpg
"""
import random

PLAYERS = 4
CARD_COLORS = [chr(127153), chr(127137), chr(127169), chr(127185)]
CARD_RANKS = 127166 - 127153 + 1

deck = [chr(ord(color) + rank) for color in CARD_COLORS for rank in range(CARD_RANKS)]
random.shuffle(deck)
hands = [''.join(card for _, card in zip(range(5), deck)) for _ in range(PLAYERS)]

pile = ''.join(deck)
