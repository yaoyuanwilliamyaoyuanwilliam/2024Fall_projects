# 2024 Fall Final Projects

Each project from this semester is a public fork linked from this repository.  This is just one of the many assignments students worked on for the course, but this is the *only* one they are permitted to publish openly.

## Project Name: Three-player Hexagonal Othello

Description: This project reimagines the classic game of Othello by introducing a third player and using a hexagonal board. While making many different changes to the game rules and initial state, the program presents what I believe is the best gaming experience and competitive form. The game emphasizes dynamic strategy, multiplayer interaction, and fair competition. Even though the new format adds complexity, the project still fully ensures smooth gameplay after performance optimization.

## Basic Rule:
Flipping rules: the same as Othello(Reversi) with 2 players if we treat the other two pieces as pieces of the same opponent. 
Adding rules: B - W - R one by one and if no place valid to add then skip, if skip 3 times in a row, it will end immediately.
Victory conditions: count the number of pieces, the one with most pieces win.

## Additional Rule:
At no time can either party be completely killed.

## Running Cost:
n: the length of on side of the board

board cells: O(n^2)
init_board: O(n^2)

is_valid_move: O(n)
make_move : O(n)
flip_pieces: O(n)

get_valid_moves : O(n^2)
play : O(n^2) / each turn
