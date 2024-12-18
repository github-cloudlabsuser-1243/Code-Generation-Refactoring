# Intentionally flawed Python program

# importing modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
if len(deck) >= 5:
    print("You got:")
    for i in range(5):
        print(deck[i][0], "of", deck[i][1])
else:
    print("Not enough cards in the deck to draw five cards.")
