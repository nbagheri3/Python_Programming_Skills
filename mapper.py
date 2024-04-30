#!/usr/bin/env python3
import sys

# Read input line by line
for line in sys.stdin:
    line = line.strip()
    # Split the line into deck_no, suit, and card variables
    deck_no, suit, card = line.split(":")
    # Define face cards
    face_cards = ["Ace", "Jack", "Queen", "King"]
    # If the card is a face card, skip it
    if card in face_cards:
        continue
    else:
        # Output the key, card value
        print("{}\t{}".format(suit, int(card)))
