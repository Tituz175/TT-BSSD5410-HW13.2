def card_details(num):
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 0] + ["J", "Q", "K", "A"]
    cards_length = len(cards)
    clubs = ["C", "D", "H", "S"]
    card_position = num % cards_length
    card_class = num // cards_length
    card_detail = str(cards[card_position]) + clubs[card_class]
    return card_detail
