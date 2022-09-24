# 3 x 3 --- TicTacToe Human Vs Computer Game
import random


class Player:  # Base class

    def __init__(self, symbol):
        self.symbol = symbol


class HumanPlayer(Player):  # Defining Human player and its Move method
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move(self, game):
        avail_moves = game.get_available_moves()
        print('Available positions for you are: ', avail_moves)
        flag1 = True
        while flag1:
            our_move = int(input('Please Enter valid positions:-->'))
            if our_move in avail_moves:
                print('Your move: ', our_move)
                flag1 = False
            else:
                print('!!! Invalid Selection !!! ')

        return our_move


class RandomCompPlayer(Player):  # Defining Computer player and its Move method
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move(self, game):
        avail_moves = game.get_available_moves()
        rcp_move = random.choice(avail_moves)
        print('Comp move: ', rcp_move)
        return rcp_move


class TicTacToe1:  # Defining Game rules and board functions
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():  # Creating array to display game-board
        return [' ' for i in range(9)]

    def print_board(self):
        for j in range(len(self.board)):
            if j % 3 == 0:
                print('\n', '--------', '\n|', end='')
            print(self.board[j], '|', end='')
        print('\n --------\n')

    def get_available_moves(self):
        available_moves = [k for k in range(len(self.board)) if self.board[k] == ' ']
        return available_moves

    def assign_move(self, symbol, position):
        self.board[position] = symbol
        self.print_board()
        if self.winner(symbol):
            self.current_winner = symbol
            return True
        else:
            return False

    def winner(self, symbol):  # Winning condition for either player
        row_moves = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        col_moves = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
        dgl_moves = [[0, 4, 8], [2, 4, 6]]
        for row_set in row_moves:
            row_bool_list = [True if symbol == self.board[ele] else False for ele in row_set]
            if all(row_bool_list):
                return True
        for col_set in col_moves:
            col_bool_list = [True if symbol == self.board[ele] else False for ele in col_set]
            if all(col_bool_list):
                return True
        for dgl_set in dgl_moves:
            dgl_bool_list = [True if symbol == self.board[ele] else False for ele in dgl_set]
            if all(dgl_bool_list):
                return True
        return False

    def check_empty_box(self):
        if ' ' in self.board:
            return True
        else:
            return False


def play(game, x_player, o_player):  # Playing condition

    game.print_board()

    symbol = 'O'
    while game.check_empty_box():
        if symbol == 'O':
            move = o_player.get_move(game)
        else:
            move = x_player.get_move(game)

        if game.assign_move(symbol, move):
            if game.current_winner:
                if symbol == 'O':
                    print('Human player Wins!')
                else:
                    print('Computer Wins!')
                break

        if symbol == 'X':
            symbol = 'O'
        else:
            symbol = 'X'
    else:
        print("IT's a Tie !!")


x_player = RandomCompPlayer('X')
o_player = HumanPlayer('O')
t = TicTacToe1()
play(t, x_player, o_player)  # commencing play