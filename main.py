# Connect4

import numpy as np
import pygame
import sys
import math

# Rectangle Color:
BLUE = (0, 0, 255)
# Circle Color:
BLACK = (0, 0, 0)

# Player Colors:
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Dimensions of the board, goal of game
ROW_COUNT = 6
COLUMN_COUNT = 7
PIECES = ROW_COUNT - 2

# Differeniate between player 1 and player 2
turn = 0

# For negative diagonals:
neg_bound = int(ROW_COUNT - 3)

# Create a matrix to represent the board
def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

# Process:

# Drop the piece at the given location
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Check if the top row of that column hasn't been filled
def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

#Find the first instance of empty space
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r
# Take our board and reflect it across the x-axis
def print_board(board):
    print(np.flip(board, 0))

# Check for a 4 of a kind: Horizontal, Vertical, Positive and Negative diagonals
def winning_move(board, piece):
    pieces = []  # Keep track of the pieces
    # Check all the horizontal locations: Change column, row constant
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT):
            # Check for a piece, check the length of the list
            if board[r][c] == piece:
                pieces.append(piece)
                if (moves := len(pieces)) == PIECES:
                    return True
            else:
                # Reset the process, continue through every column
                pieces.clear()

    # Check all the vertical locations; for every column, check every row
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == piece:
                pieces.append(piece)
                # Check if we have a four of a kind
                if (moves := len(pieces)) == PIECES:
                    return True
            else:
                pieces.clear()

    # Check all positively sloped diagonals:
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT):
            # Check on row status, once it passes, then we stop the process
            if r < ROW_COUNT:
                if board[r][c] == piece:
                    pieces.append(piece)
                    r += 1
                    if (moves := len(pieces)) == PIECES:
                        return True
                else:
                    pieces.clear()

    # Check all negatively sloped diagonals
    for r in range(neg_bound, ROW_COUNT):
        for c in range(COLUMN_COUNT):
            # Check on row status
            if r >= 0:
                if board[r][c] == piece:
                    pieces.append(piece)
                    r -= 1
                    if (moves := len(pieces)) == PIECES:
                        return True
                else:
                    pieces.clear()

# Draw the Graphics
def draw_board(board):
    # Set up the board: Create the blue rectangles, then put a black circle in center
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            # Rectangle Size and Position
            position = c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE
            rect_size = SQUARESIZE, SQUARESIZE

            # Circle Position
            circle_x = int(c * SQUARESIZE + SQUARESIZE / 2)
            circle_y = int(r * SQUARESIZE + SQUARESIZE + HALFWAY)

            # Draw the Setup
            pygame.draw.rect(screen, BLUE, (position, rect_size))
            pygame.draw.circle(screen, BLACK, (circle_x, circle_y), RADIUS)

    # Overide the Black Circles When A Piece is Dropped
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):

            # Pieces: Bottom, Up Pattern
            piece_x = int(c * SQUARESIZE + SQUARESIZE / 2)
            piece_y = (height - (r * SQUARESIZE)) - HALFWAY
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (piece_x, piece_y), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (piece_x, piece_y), RADIUS)

    pygame.display.update()

# Create the board
board = create_board()

# Initialize pygame
pygame.init()

# Screen Setup
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)

# Board Setup
RADIUS = int((SQUARESIZE/2) - 5)
HALFWAY = SQUARESIZE/2

# Program at first instance
screen = pygame.display.set_mode(size)
title = pygame.display.set_caption("Connect 4")
caption = pygame.image.load("connect 4 icon.png")
icon = pygame.display.set_icon(caption)
draw_board(board)
pygame.display.update()

# Specify a font when we win the game
myfont = pygame.font.SysFont("monospace", 75)
# Mouse Motion: Pass in circles

# Create the Game Loop
running = True
while running:

    # Event Loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            posx = event.pos[0]

            # Check for border collisions(before the cirle implementation)
            if posx <= 45:
                posx = 45
            elif posx >= width - 45:
                posx = width - 45

            # Implement the circle by their turn, movement affected by my mouse
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, HALFWAY), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, HALFWAY), RADIUS)


            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Prevents the tile from being implemented
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            # Ask for player 1 Input:
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
            # Piece Implementing process: Check for a valid location, get the row, then put the piece
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        label = myfont.render("Player 1 wins!!", 1, RED)
                        screen.blit(label, (20, 10))
                        running = False
    # Ask for player 2 Input
            else:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
        # Piece Implementing process: Check for a valid location, get the row, then put the piece
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        label = myfont.render("Player 2 wins!!", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        running = False

            # Redraw the Graphics
            draw_board(board)

        # Continously alternating the turns
            turn += 1
            turn = turn % 2

        if not running:
            pygame.time.wait(3000)




