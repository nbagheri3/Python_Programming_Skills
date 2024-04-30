#!/usr/bin/env python3
import sys

# Initialize variables
current_suit = None
current_sum = 0
current_count = 0

# Loop through input received from standard input
for line in sys.stdin:
    # Split line into suit and card
    suit, card = line.strip().split()
    try:
        # Convert the card to an integer
        card = int(card)
    except ValueError:
        continue

    # Check if the current suit matches the suit on this line
    if current_suit != suit:
        # Print the previous suit's data (if there was one)
        if current_suit:
            print('{}:{}:{}'.format(current_suit, current_sum, current_count))

        # Reset the sum and count for the new suit
        current_count = 0
        current_suit = suit

    # Add the card value to the running sum and increment the count
    current_sum += card
    current_count += 1

# Print the data for the last suit (if there was one)
if current_suit:
    print('{}:{}:{}'.format(current_suit, current_sum, current_count))
