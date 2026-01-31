"""
Tic-Tac-Toe game with optional AI opponent (Minimax algorithm).

Features:
- Two-player local mode (Player vs Player)
- Player vs Computer mode with an unbeatable Minimax AI
- Clear, well-documented functions and in-line comments

Usage:
Run the script and follow the on-screen prompts to choose mode and play.
"""

from typing import List, Optional, Tuple
import math

# Board positions are indexed 0..8 as follows:
#  0 | 1 | 2
#  ---------
#  3 | 4 | 5
#  ---------
#  6 | 7 | 8


def display_board(board: List[str]) -> None:
    """Prints the current board to the console in a human-friendly format."""
    rows = [board[i:i + 3] for i in range(0, 9, 3)]
    line = "-----------"
    for i, row in enumerate(rows):
        print(" {} | {} | {} ".format(*row))
        if i < 2:
            print(line)


def empty_positions(board: List[str]) -> List[int]:
    """Returns a list of indices that are not yet taken on the board."""
    return [i for i, v in enumerate(board) if v == " "]


def check_winner(board: List[str]) -> Optional[str]:
    """Checks the board for a winner.

    Returns:
        'X' or 'O' if that player has won, 'D' for draw, or None if the game is still ongoing.
    """
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]

    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "D"  # Draw

    return None  # Game still ongoing


def make_move(board: List[str], index: int, player: str) -> bool:
    """Attempts to make a move for `player` at `index`.

    Returns True if the move was successful, False if the position is already taken.
    """
    if board[index] == " ":
        board[index] = player
        return True
    return False


def minimax(board: List[str], depth: int, maximizing: bool, player: str, opponent: str) -> Tuple[int, Optional[int]]:
    """Minimax algorithm to compute the best score and move for the current player.

    Args:
        board: Current board state.
        depth: Remaining depth (not strictly necessary for tic-tac-toe, but helps clarity).
        maximizing: True if the current layer aims to maximize the `player`'s score.
        player: The symbol for the AI ('X' or 'O').
        opponent: The other player's symbol.

    Returns:
        A tuple (best_score, best_move_index).
    """
    winner = check_winner(board)
    if winner == player:
        return 1, None
    elif winner == opponent:
        return -1, None
    elif winner == "D":
        return 0, None

    best_move: Optional[int] = None

    if maximizing:
        best_score = -math.inf
        for idx in empty_positions(board):
            board[idx] = player
            score, _ = minimax(board, depth - 1, False, player, opponent)
            board[idx] = " "
            # Prefer faster wins: subtract depth to pick quicker wins at higher scores
            if score > best_score or (score == best_score and best_move is None):
                best_score = score
                best_move = idx
        return best_score, best_move

    else:
        best_score = math.inf
        for idx in empty_positions(board):
            board[idx] = opponent
            score, _ = minimax(board, depth - 1, True, player, opponent)
            board[idx] = " "
            if score < best_score or (score == best_score and best_move is None):
                best_score = score
                best_move = idx
        return best_score, best_move


def ai_move(board: List[str], ai_player: str, human_player: str) -> int:
    """Computes and performs the AI move using Minimax. Returns the index chosen."""
    _, move = minimax(board, depth=9, maximizing=True, player=ai_player, opponent=human_player)
    if move is None:
        # No move returned (shouldn't happen unless board is full)
        raise RuntimeError("AI could not determine a move")
    board[move] = ai_player
    return move


def player_input(board: List[str], player: str) -> int:
    """Prompts the user for a move until a valid choice is made and returns the chosen index."""
    valid = False
    choice = -1
    while not valid:
        try:
            raw = input(f"Player {player}, enter your move (1-9): ")
            choice = int(raw.strip()) - 1
            if choice not in range(9):
                print("Invalid input: choose a number from 1 to 9.")
                continue
            if board[choice] != " ":
                print("That position is already taken. Choose another one.")
                continue
            valid = True
        except ValueError:
            print("Please enter a valid integer between 1 and 9.")
    return choice


def play_game(vs_computer: bool = True) -> None:
    """Main game loop. Set `vs_computer` to False to play two-player local mode."""
    board: List[str] = [" "] * 9

    # Choose who is X and who plays first
    human_player = "X"
    ai_player = "O"

    if vs_computer:
        # Ask whether human wants to go first
        while True:
            first = input("Do you want to go first? (y/n): ").strip().lower()
            if first in ("y", "yes"):
                human_player = "X"
                ai_player = "O"
                break
            elif first in ("n", "no"):
                human_player = "O"
                ai_player = "X"
                break
            else:
                print("Please answer 'y' or 'n'.")

    current_player = "X"
    game_over = False

    print("\nStarting Tic-Tac-Toe!")
    display_board([str(i + 1) if v == " " else v for i, v in enumerate(board)])

    while not game_over:
        print("\nCurrent board:")
        display_board(board)

        if vs_computer and current_player == ai_player:
            # AI's turn
            move = ai_move(board, ai_player, human_player)
            print(f"\nComputer ({ai_player}) plays position {move + 1}.")
        else:
            # Human's turn (either human vs human or human vs AI)
            move = player_input(board, current_player)
            make_move(board, move, current_player)

        result = check_winner(board)
        if result == "X" or result == "O":
            print("\nFinal board:")
            display_board(board)
            print(f"\nPlayer {result} wins! 🎉")
            game_over = True
        elif result == "D":
            print("\nFinal board:")
            display_board(board)
            print("\nIt's a draw! 🤝")
            game_over = True
        else:
            # Switch turns
            current_player = "O" if current_player == "X" else "X"

    print("\nThanks for playing!")


def main() -> None:
    """Entrypoint for the program. Allows the user to pick a mode and play multiple rounds."""
    print("Welcome to Tic-Tac-Toe (with optional AI)\n")

    while True:
        mode = ""
        while mode not in ("1", "2"):
            print("Choose mode:")
            print("1) Player vs Computer (AI)")
            print("2) Player vs Player (local)")
            mode = input("Enter 1 or 2: ").strip()

        vs_computer = (mode == "1")
        play_game(vs_computer=vs_computer)

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
