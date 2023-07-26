#!/usr/bin/env python3
"""board_encoding.py"""


def decode_board(board_int: int) -> list[list[int]]:
    """Returns an array corresponding to board setup given encoded board int"""
    # Create empty list for sequence of ints on decoded board read L to R, top to bottom
    board_sequence: list[int] = []
    # Append reversed base-3 description of board_int to list (based on encoding scheme)
    while board_int > 0:
        board_sequence.append(board_int % 3)
        board_int = board_int // 3
    # Initialize a 2D array for the final board set-up (3x3 tic-tac-toe board)
    board_array: list[list[int]] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    # Replace elements of board_array with their values from board_sequence
    for i, x in enumerate(board_sequence):
        row: int = i // 3  # Move to new row after traversing 3 values of board_sequence
        # Add values of board_sequence to successive positions in board_array
        board_array[row][i - 3 * row] = x
    return board_array  # Return final board architecture


def print_board(board_num: int, board: list[list[int]]) -> None:
    """Prints decoded board on screen with integer values
    represented as letters X (1) and O (2)"""
    print(f"\nBoard {board_num + 1}\n")  # Prints board number
    # Traverses the board and prints an X or O depending on value at each position
    for list_num in range(len(board)):
        for i in board[list_num]:
            if i == 1:
                print("[X]", end="")
            elif i == 2:
                print("[O]", end="")
            else:
                print("[_]", end="")  # Prints blank space if value on board is 0
        print()  # Add new line after each list contained within board
    print()


def main() -> None:
    boards: list[int] = [2271, 1638, 12065]  # Creates a list of boards to decode
    # Prints each decoded board using print_board and decode_board functions
    for board_num, board in enumerate(boards):
        print_board(board_num, decode_board(board))


if __name__ == "__main__":
    main()
