import random
import os
import time

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
WIN_THE_MATCH = 3
WINNING_LINES = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],
    [1, 4, 7], [2, 5, 8], [3, 6, 9],
    [1, 5, 9], [3, 5, 7]
]
# FIRST_TO_GO = None

def display_intro():
    prompt('Welcome to Tic-Tac-Toe! First to 3 wins!')
    time.sleep(2)
    prompt('The board is laid out as follows')
    print('')
    print('     |     |')
    print(f'  1  |  2  |  3  ')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  4  |  5  |  6  ')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  7  |  8  |  9  ')
    print('     |     |')
    print('')
    # who_goes_first()
    time.sleep(5)
    prompt('Good luck!')

# def who_goes_first():
#     prompt('Who do you want to make the first move? player, computer, or choose')
#     FIRST_TO_GO = input().strip().strip(',').lower()
     

def display_board(board):
    os.system('clear')

    prompt(f'You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.')
    print('')
    print('     |     |')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}  ')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}  ')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}  ')
    print('     |     |')
    print('')


def initialize_board():
    return {number: INITIAL_MARKER for number in range(1,10)}


def initialize_scoreboard():
    return {'Player': 0, 'Computer': 0}


def prompt(message):
    print(f'==> {message}')


def display_scoreboard(scoreboard):
    prompt(f"Player: {scoreboard['Player']}   Computer: {scoreboard['Computer']}")


def update_scoreboard(winner, scoreboard):
    if winner == 'Player':
        scoreboard['Player'] += 1
    elif winner == 'Computer':
        scoreboard['Computer'] += 1
    else:
        pass


def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]


def join_or(sequence, delimiter=', ', word='or'):
    match len(sequence):
        case 0:
            return ''
        case 1:
            return str(sequence[0])
        case 2:
            return f"{(sequence[0])} {word} {str(sequence[1])}"
    sequence = [str(item) for item in sequence]
    return f"{delimiter.join(sequence[0:-1])}{delimiter}{word} {sequence[-1]}"


def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Please choose a number out of ({join_or(valid_choices)})")
        square = input().strip()
        if square in valid_choices:
            break
        prompt("Sorry, that's not a valid choice")

    board[int(square)] = HUMAN_MARKER


def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    square = None

    for line in WINNING_LINES:
        square = detect_offensive_square(line, board)
        if square:
            break

    if not square:
        for line in WINNING_LINES:
            square = detect_at_risk_square(line, board)
            if square:
                break
    
    if not square:
        square = pick_square_five(board)

    if not square:
        square = random.choice(empty_squares(board))

    board[square] = COMPUTER_MARKER


def detect_offensive_square(line, board):
    computer_squares_in_line = [board[square] for square in line]

    if computer_squares_in_line.count(COMPUTER_MARKER) == 2:
        for square in line:
            if board[square] == INITIAL_MARKER:
                return square
    return None


def detect_at_risk_square(line, board):
    marked_squares_in_line = [board[square] for square in line]

    if marked_squares_in_line.count(HUMAN_MARKER) == 2:
        for square in line:
            if board[square] == INITIAL_MARKER:
                return square
    return None


def pick_square_five(board):
    return 5 if board[5] == INITIAL_MARKER else None


def board_full(board):
    return len(empty_squares(board)) == 0


def someone_won(board):
    return bool(detect_winner(board))


def detect_winner(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
                and board[sq2] == HUMAN_MARKER
                and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
                and board[sq2] == COMPUTER_MARKER
                and board[sq3] == COMPUTER_MARKER):
            return 'Computer'
    return None


def play_tic_tac_toe():
    while True:
        display_intro()
        board = initialize_board()
        scoreboard = initialize_scoreboard()

        while scoreboard['Computer'] < WIN_THE_MATCH and scoreboard['Player'] < WIN_THE_MATCH:
            board = initialize_board()
            while True:
                display_board(board)
                display_scoreboard(scoreboard)

                player_chooses_square(board)
                if someone_won(board) or board_full(board):
                    break
                
                computer_chooses_square(board)
                if someone_won(board) or board_full(board):
                    break

            display_board(board)
            if someone_won(board):
                prompt(f'{detect_winner(board)} won!')
            else:
                prompt("It's a tie!")
            time.sleep(2)

            update_scoreboard(detect_winner(board), scoreboard)
            display_scoreboard(scoreboard)

        prompt(f'{detect_winner(board)} is the ultimate tic-tac-toe champion!')
        prompt('Play again? (Y/N)')
        answer = input().strip().lower()
        if answer[0] != 'y':
            break
    prompt("Thanks for playing!")


play_tic_tac_toe()

###Trying to figure out the setting to have the computer go first
#improve play again handling
#improve game loop
