import sys


class TicTacToeGame:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Creates the empty board
        self.current_player = 'X'

    def to_move(self):  # Player/Computer move
        return self.current_player

    def actions(self):  # ok so we iterate thro the box and then pick out empty spots
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def result(self, action):
        new_game = TicTacToeGame()
        new_game.board = self.board.copy()
        new_game.board[action] = self.current_player
        new_game.current_player = 'O' if self.current_player == 'X' else 'X'
        return new_game

    def is_terminal(self):  # check if game
        return self.check_winner() is not None or ' ' not in self.board

    def utility(self, player):  # Minmax utility(as discussed in class)
        winner = self.check_winner()
        if winner == player:
            return 1
        elif winner is None:
            return 0
        else:
            return -1

    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                return self.board[a]
        return None


node_count = 0  # For the search tree


def minimax_search(game):  # This goes as per the psuedocode
    global node_count
    node_count = 0
    player = game.to_move()
    value, move = max_value(game, player)
    return move


def max_value(game, player):
    global node_count
    node_count += 1
    if game.is_terminal():
        return game.utility(player), None
    v = float('-inf')
    move = None
    for a in game.actions():
        v2, _ = min_value(game.result(a), player)
        if v2 > v:
            v, move = v2, a
    return v, move

def min_value(game, player):
    global node_count
    node_count += 1
    if game.is_terminal():
        return game.utility(player), None
    v = float('inf')
    move = None
    for a in game.actions():
        v2, _ = max_value(game.result(a), player)
        if v2 < v:
            v, move = v2, a
    return v, move


def alpha_beta_search(game):
    global node_count
    node_count = 0
    player = game.to_move()
    value, move = max_value_ab(game, float('-inf'), float('inf'), player)
    return move

def max_value_ab(game, alpha, beta, player):
    global node_count
    node_count += 1
    if game.is_terminal():
        return game.utility(player), None
    v = float('-inf')
    move = None
    for a in game.actions():
        v2, _ = min_value_ab(game.result(a), alpha, beta, player)
        if v2 > v:
            v, move = v2, a
            alpha = max(alpha, v)
        if v >= beta:
            return v, move
    return v, move


def min_value_ab(game, alpha, beta, player):
    global node_count
    node_count += 1
    if game.is_terminal():
        return game.utility(player), None
    v = float('inf')
    move = None
    for a in game.actions():
        v2, _ = max_value_ab(game.result(a), alpha, beta, player)
        if v2 < v:
            v, move = v2, a
            beta = min(beta, v)
        if v <= alpha:
            return v, move
    return v, move


def display_board(board):  # Display board
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")


def get_human_move(game):  # Player's turn
    while True:
        possible_moves = [i + 1 for i in game.actions()]
        print(
            f"{game.current_player}'s move. What is your move (possible moves at the moment are: {possible_moves} | enter 0 to exit the game)?")
        try:
            move = int(input())
            if move == 0:
                return None
            if move - 1 in game.actions():
                return move - 1
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number.")


def play_game(first, algo, mode):
    game = TicTacToeGame()
    game.current_player = first

    display_board(game.board)
    print("Initial empty board")

    while not game.is_terminal():
        if (mode == '1' and game.current_player == 'O') or mode == '2':
            # Computer's move
            if algo == '1':
                move = minimax_search(game)
            else:
                move = alpha_beta_search(game)
            print(f"{game.current_player}'s selected move: {move + 1}. Number of search tree nodes generated: {node_count}")
        else:
            move = get_human_move(game)
            if move is None:
                print("Game terminated by user.")
                return

        game = game.result(move)
        display_board(game.board)

    winner = game.check_winner()
    if winner:
        print(f"{winner} WON")
    else:
        print("TIE")


def main():  # Message to future me, use cmd to run(don't run on pycharm)
    if len(sys.argv) != 4:
        print("ERROR: Not enough/too many/illegal input arguments.")
        return

    algo, first, mode = sys.argv[1], sys.argv[2], sys.argv[3]

    if algo not in ['1', '2'] or first not in ['X', 'O'] or mode not in ['1', '2']:
        print("ERROR: Not enough/too many/illegal input arguments.")
        return

    print("Kuchibhotla, Pranav, A20511026 solution:")
    print(f"Algorithm: {'MiniMax' if algo == '1' else 'MiniMax with alpha-beta pruning'}")
    print(f"First: {first}")
    print(f"Mode: {'human versus computer' if mode == '1' else 'computer versus computer'}")

    play_game(first, algo, mode)


if __name__ == "__main__":
    main()


