#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

board = ["-", "-", "-",
          "-", "-", "-",
          "-", "-", "-"]

def display_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print('-----')
    print(board[3] + "|" + board[4] + "|" + board[5])
    print('-----')
    print(board[6] + "|" + board[7] + "|" + board[8])

def choose_players_and_markers():
    players = ['Player 1', 'Player 2']
    random.shuffle(players)
    
    player1_marker = input(f"{players[0]}, choose X or O: ").upper()
    if player1_marker == 'X':
        player2_marker = 'O'
    else:
        player2_marker = 'X'
    return players[0], player1_marker, players[1], player2_marker

def place_marker(board, mark, position):
    board[position] = mark

def win_check(board, mark):
    return ((board[0] == mark and board[1] == mark and board[2] == mark) or
            (board[3] == mark and board[4] == mark and board[5] == mark) or
            (board[6] == mark and board[7] == mark and board[8] == mark) or
            (board[0] == mark and board[3] == mark and board[6] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[0] == mark and board[4] == mark and board[8] == mark) or
            (board[2] == mark and board[4] == mark and board[6] == mark))

def space_check(board, position):
    return board[position] == '-'

def full_board_check(board):
    return '-' not in board

def player_choice(board, player):
    position = None
    while position not in [0, 1, 2, 3, 4, 5, 6, 7, 8] or not space_check(board, position):
        position = int(input(f'{player}, choose your position (0-8): '))
    return position

def replay():
    return input('Do you want to replay? Enter "yes" or "no": ').lower().startswith('y')

while True:
    player1, player1_marker, player2, player2_marker = choose_players_and_markers()
    
    display_board(board)
    board = ["-", "-", "-",
          "-", "-", "-",
          "-", "-", "-"]
    while not full_board_check(board):
        position = player_choice(board, player1)
        place_marker(board, player1_marker, position)
        display_board(board)
        if win_check(board, player1_marker):
            print(f"{player1} wins!")
            break
        if full_board_check(board):
            print("It's a tie!")
            break

        # Player 2's turn
        position = player_choice(board, player2)
        place_marker(board, player2_marker, position)
        display_board(board)
        if win_check(board, player2_marker):
            print(f"{player2} wins!")
            break
        if full_board_check(board):
            print("It's a tie!")
            break

    if not replay():
        print("Thank you for playing!")
        break


# In[ ]:




