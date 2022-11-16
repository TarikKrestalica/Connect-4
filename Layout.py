[[0, 0, 0, 0, 0, 0, 0]
 [0, 0, 0, 0, 0, 0, 0]
 [0, 0, 0, 0, 0, 0, 0]
 [0, 0, 0, 0, 0, 0, 0]
 [0, 0, 0, 0, 0, 0, 0]
 [0, 0, 0, 0, 0, 0, 0]]

# Player Turn (Select Column 0, 1, 2, 3, 4, 5, 6):
    # We will have the user control where they implement the disks
    # Whatever number you select, that's where the piece will be implemented


#Players to choose a column from 0 to 6
# Ask for player 1 Input:
#if turn == 0:
    #col = int(input("Player 1, choose a column (0-6): "))

#Piece Implementing process: Check for a valid location, get the row, then put the piece
    #if is_valid_location(board, col):
        #row = get_next_open_row(board, col)
        #drop_piece(board, row, col, 1)

        # if winning_move(board, 1):
            # print("Player 1 Wins!!! Congrats!!!")
            # print(print_board(board))
            # running = False
            # break


# Ask for player 2 Input
# else:
    # col = int(input("Player 2, choose a column (0-6): "))

# Piece Implementing process: Check for a valid location, get the row, then put the piece
    # if is_valid_location(board, col):
        # row = get_next_open_row(board, col)
        # drop_piece(board, row, col, 2)

        # if winning_move(board, 2):
            # print("Player 2 Wins!!! Congrats!!!")
            # running = False

            # print(print_board(board))

# Continously alternating the turns
# turn += 1
# turn = turn % 2