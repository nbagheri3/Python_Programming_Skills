import random

def generate_deck():
    suits = ["Spade", "Heart", "Diamond", "Club"]
    cards = ["Ace", "Jack", "Queen", "King"]
    cards.extend(map(str, range(2, 11)))
    complete_deck = [(suit, card) for suit in suits for card in cards]
    return complete_deck

def write_decks_to_file(num_decks, deck_size, output_file):
    random.seed(32)
    card_dict = {suit: [0, 0] for suit in suits}
    for i in range(num_decks):
        deck_cards = random.sample(complete_deck, deck_size)
        random.shuffle(deck_cards)
        for card in deck_cards:
            output_file.write("Deck-{}:{}:{}\n".format(i, card[0], card[1]))
            if card[1] in ["Ace", "Jack", "Queen", "King"]:
                continue
            else:
                card_dict[card[0]][0] += int(card[1])
                card_dict[card[0]][1] += 1

    return card_dict

def main(num_decks, deck_size, output_file_path):
    with open(output_file_path, "w") as output_file:
        card_dict = write_decks_to_file(num_decks, deck_size, output_file)

    for suit in suits:
        print('{}:{}:{}'.format(suit, card_dict[suit][0], card_dict[suit][1]))

if __name__ == "__main__":
    num_decks = int(input("Number of decks to generate: "))
    deck_size = int(input("Number of cards in each deck: "))
    output_file_path = input("Output file path: ")
    suits = ["Spade", "Heart", "Diamond", "Club"]
    complete_deck = generate_deck()
    main(num_decks, deck_size, output_file_path)
