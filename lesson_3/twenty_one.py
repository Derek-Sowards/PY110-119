import random
import os
import time

CARD_VALUES = [str(num) for num in range(2,11)] + ['J', 'Q', 'K', 'A']
SUITS = SUITS = ['♠', '♥', '♣', '♦']
TERM_SIZE = os.get_terminal_size()
HIT_OR_STAY = ['h', 's']


def say(message):
    print(f"==> {message}")

def wait(seconds):
    time.sleep(seconds)

def clear():
    os.system('clear')

def enter_to_continue():
    input('Press Enter to continue...\n')

def print_terminal_line():
    print("-" * TERM_SIZE.columns)

def display_instructions():
    clear()
    print('Welcome To 21!\n')
    print("Get as close to 21 as possible without going over.")
    print("Each player starts with 2 cards. One of the dealer's cards is hidden.")
    print("Options: 'Hit' to add cards to your total, 'Stay' to hold your total.")
    print("Going over 21 is a 'bust', resulting in an automatic loss.")
    print("Dealer hits until reaching 17 or higher.\n")
    print("Good luck\n")

def initialize_deck():
    init_deck = [f'{value}{suit}'
            for suit in SUITS
            for value in CARD_VALUES]
    random.shuffle(init_deck)
    return init_deck

def get_ascii_card(hand):
    cards = []
    for card in hand:
        card_display = []
        symbol = card[-1]
        num_list = [char for char in card if char not in SUITS]
        num1 = num_list[0]
        num2 = ' ' if len(num_list) != 2 else num_list[1]
        card_display.append("•---------•")
        card_display.append(f"| {num1}{num2}      |")
        card_display.append("|         |")
        card_display.append(f"|    {symbol}    |")
        card_display.append("|         |")
        card_display.append(f"|       {num1}{num2}|")
        card_display.append("•---------•")
        cards.append(card_display)
    return cards

def display_one_card(cards):
    for line in cards[0]:
        print(line)

def display_cards(cards):
    for pieces in zip(*(card for card in cards)):
        print('   '.join(pieces))

def get_two_from_deck(init_deck):
    return [init_deck.pop(), init_deck.pop()]

def first_total_for_dealer(cards):
    sum_val = 0

    value = cards[0][:-1]

    if value == "A":
        sum_val += 11
    elif value in ['J', 'Q', 'K']:
        sum_val += 10
    else:
        sum_val += int(value)
    return sum_val

def total(cards):
    sum_val = 0

    for card in cards:
        value = card[:-1]

        if value == "A":
            sum_val += 11
        elif value in ['J', 'Q', 'K']:
            sum_val += 10
        else:
            sum_val += int(value)

    # Correct for Aces
    for card in cards:
        value = card[:-1]
        if sum_val <= 21:
            break
        if value == "A":
            sum_val -= 10

    return sum_val

def busted(cards):
    return total(cards) > 21

def detect_result(dealer_cards, player_cards):
    player_total = total(player_cards)
    dealer_total = total(dealer_cards)

    if player_total > 21:
        return 'PLAYER_BUSTED'
    if dealer_total > 21:
        return 'DEALER_BUSTED'
    if dealer_total < player_total:
        return 'PLAYER'
    if dealer_total > player_total:
        return 'DEALER'
    return 'TIE'

def display_results(dealer_cards, player_cards):
    result = detect_result(dealer_cards, player_cards)

    match result:
        case 'PLAYER_BUSTED':
            say('You busted! Dealer wins!')
        case 'DEALER_BUSTED':
            say('Dealer busted! You win!')
        case 'PLAYER':
            say('You win!')
        case 'DEALER':
            say('Dealer wins!')
        case _:
            say("It's a tie!")

def play_again():
    while True:
        answer = input("Would you like to play again? y/n\n").strip().casefold()[0]
        if answer not in ['y', 'n']:
            say("Invalid input. Try again!")
            continue
        return answer == 'y'

def display_dealers_first_card(dealers_hand_init):
    clear()
    display_one_card(get_ascii_card(dealers_hand_init))
    print(f"Dealer's Total: {first_total_for_dealer(dealers_hand_init)}")

def display_all_cards(dealers_hand_init, players_hand_init):
    clear()
    display_cards(get_ascii_card(dealers_hand_init))
    print(f"Dealer's Total: {total(dealers_hand_init)}")
    print_terminal_line()
    display_cards(get_ascii_card(players_hand_init))
    print(f"Your Total: {total(players_hand_init)}")

def display_all_player_cards(players_hand_init):
    print_terminal_line()
    display_cards(get_ascii_card(players_hand_init))
    print(f"Your Total: {total(players_hand_init)}")

def get_players_answer():
    while True:
        answer = input("Would you like to hit or stay? (h/s)\n").strip().casefold()[0]
        if answer not in HIT_OR_STAY:
            say("Invalid input, must enter 'h' or 's'.")
            continue
        return answer

#Pre-Game

display_instructions()
enter_to_continue()

#Main Game Loop
#play 5 rounds. display how many rounds they won out of the 5. have a counter to count every iteration through game
#maybe change all of the play_agains() need to be swapped with (Press enter to continue to next rounds)
#Then have the play_again function at the very end of the 5 rounds.

while True:
    clear()
    wait(1)
    deck = initialize_deck()
    players_hand = get_two_from_deck(deck)
    dealers_hand = get_two_from_deck(deck)

    display_dealers_first_card(dealers_hand)
    display_all_player_cards(players_hand)

    #Player loop

    while True:
        players_answer = get_players_answer()

        if players_answer == 'h':
            players_hand.append(deck.pop())
            say("You chose to hit! ")
            wait(1)
            display_dealers_first_card(dealers_hand)
            display_all_player_cards(players_hand)

        if players_answer == 's' or busted(players_hand):
            break

    if busted(players_hand):
        display_results(dealers_hand, players_hand)
        wait(2)
        if play_again():
            continue
        break
    say(f"You stayed at {total(players_hand)}")
    wait(1)
    #Dealer loop

    say("Dealer's turn... ")
    wait(2)
    display_all_cards(dealers_hand, players_hand)
    wait(2)

    while total(dealers_hand) < 17:
        say("Dealer is deciding....")
        wait(2)
        clear()
        say("Dealer chooses to hit!")
        dealers_hand.append(deck.pop())
        display_all_cards(dealers_hand, players_hand)

    if busted(dealers_hand):
        display_results(dealers_hand, players_hand)
        wait(3)
        if play_again():
            continue
        break
    say(f"Dealer decides to stay at {total(dealers_hand)}")
    wait(1)

    #Both player and dealer stays
    display_results(dealers_hand, players_hand)

    if not play_again():
        break
say("Thanks for playing!")
