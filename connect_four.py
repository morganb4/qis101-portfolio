#!/usr/bin/env python3
"""connect_four.py"""

# Code adapted from @dbiersach, connect_four.py:
# https://github.com/dbiersach/qis101/blob/0aa4537a02ac7f71d62ce6bbaf54e1e3175a5d51/labs/Session%2005%20-%20Algorithmic%20Efficiency/connect_four.py


def win_sequence(board: list[list[int]], row: int, col: int) -> bool:
    """Checks for winning sequence of 4 checkers in each direction at given location"""
    # Check diagonal on upper right
    if (
        row > 2
        and col < 4
        and (
            board[row][col] == board[row - 1][col + 1]
            and board[row][col] == board[row - 2][col + 2]
            and board[row][col] == board[row - 3][col + 3]
        )
    ):
        return True
    # Check diagonal on upper left
    if (
        row > 2
        and col > 2
        and (
            board[row][col] == board[row - 1][col - 1]
            and board[row][col] == board[row - 2][col - 2]
            and board[row][col] == board[row - 3][col - 3]
        )
    ):
        return True
    # Check diagonal on lower right
    if (
        row < 3
        and col < 4
        and (
            board[row][col] == board[row + 1][col + 1]
            and board[row][col] == board[row + 2][col + 2]
            and board[row][col] == board[row + 3][col + 3]
        )
    ):
        return True
    # Check diagonal on lower left
    if (
        row < 3
        and col > 2
        and (
            board[row][col] == board[row + 1][col - 1]
            and board[row][col] == board[row + 2][col - 2]
            and board[row][col] == board[row + 3][col - 3]
        )
    ):
        return True
    # Check vertically up
    if row > 2 and (
        board[row][col] == board[row - 1][col]
        and board[row][col] == board[row - 2][col]
        and board[row][col] == board[row - 3][col]
    ):
        return True
    # Check vertically down
    if row < 3 and (
        board[row][col] == board[row + 1][col]
        and board[row][col] == board[row + 2][col]
        and board[row][col] == board[row + 3][col]
    ):
        return True
    # Check horizontally to left
    if col > 2 and (
        board[row][col] == board[row][col - 1]
        and board[row][col] == board[row][col - 2]
        and board[row][col] == board[row][col - 3]
    ):
        return True
    # Check horizontally to the right
    if col < 4 and (
        board[row][col] == board[row][col + 1]
        and board[row][col] == board[row][col + 2]
        and board[row][col] == board[row][col + 3]
    ):
        return True
    # Returns false if no winning sequences found at given position
    return False


def determine_winner(board: list[list[int]]) -> int:
    """Traverses each element of board to find winner sequence using helper function"""
    for list_num in range(len(board)):  # Traverses each list of the board
        for i in range(len(board[list_num])):  # Traverses each slot on the board
            # Calls win_sequence to check for winning sequence at given location
            if win_sequence(board, list_num, i) and board[list_num][i] != 0:
                # Returns player number for winning sequence
                return board[list_num][i]
    return 0  # Returns 0 if no winner found


def print_winner(board: list[list[int]]) -> None:
    """Prints the winner for a given board using helper functions"""
    print(*board, sep="\n")
    print("The winner is...")
    # Calls the determine_winner function
    winner: int = determine_winner(board)
    if winner == 0:
        print("There is no winner yet!")
    else:
        print(f"The winner is Player {winner}.")


def main() -> None:
    board1: list[list[int]] = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 2, 2, 1, 1, 0, 0],
        [0, 2, 1, 2, 2, 0, 1],
        [2, 1, 1, 1, 2, 0, 2],
    ]
    print_winner(board1)  # Displays the winner for board 1

    board2: list[list[int]] = [
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 1, 0],
        [0, 1, 1, 2, 2, 2, 0],
        [2, 2, 1, 1, 1, 2, 0],
    ]
    print_winner(board2)  # Displays the winner for board 2

    board3: list[list[int]] = [
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 2, 2, 0],
        [0, 1, 2, 1, 2, 2, 0],
        [0, 2, 2, 2, 1, 1, 0],
        [0, 1, 1, 2, 1, 2, 0],
    ]
    print_winner(board3)  # Displays the winner for board 3


if __name__ == "__main__":
    main()
