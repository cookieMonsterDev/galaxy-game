from enum import Enum
from config import WINNING_COMBINATIONS

DEFAULT_BOARD = [None] * 9


class Players(Enum):
    PLAYER_X = "X"
    PLAYER_O = "O"


class Game:
    def __init__(
        self,
        board=DEFAULT_BOARD.copy(),
        turn=Players.PLAYER_X.value,
        score_x=0,
        score_o=0,
        player_won=None,
        move_count=0,
        win_line=None,
    ):

        self.turn = turn
        self.board = board
        self.is_full = False
        self.score_x = score_x
        self.score_o = score_o
        self.win_line = win_line
        self.move_count = move_count
        self.player_won = player_won

    def __check_win(self):
        for index, item in enumerate(WINNING_COMBINATIONS):
            board_item_1 = self.board[item[0]]
            board_item_2 = self.board[item[1]]
            board_item_3 = self.board[item[2]]

            if board_item_1 == board_item_2 == board_item_3 and board_item_1 != None:
                self.win_line = index
                return (True, board_item_1)

        return (False, None)

    def move(self, index):
        if self.player_won:
            return

        if self.board[index] != None:
            return

        self.board[index] = self.turn
        self.move_count += 1

        self.turn = (
            Players.PLAYER_X.value
            if self.turn == Players.PLAYER_O.value
            else Players.PLAYER_O.value
        )

        if self.move_count < 5:
            return

        self.is_full = None not in self.board

        (isWin, player) = self.__check_win()

        if isWin:
            if player == Players.PLAYER_X.value:
                self.score_x += 1
                self.player_won = Players.PLAYER_X.value

            if player == Players.PLAYER_O.value:
                self.score_o += 1
                self.player_won = Players.PLAYER_O.value

    def new_round(self):
        self.move_count = 0
        self.board = DEFAULT_BOARD.copy()

        if self.player_won == Players.PLAYER_X.value:
            self.turn = Players.PLAYER_O.value

        if self.player_won == Players.PLAYER_O.value:
            self.turn = Players.PLAYER_X.value

        self.win_line = None
        self.player_won = None

    def rest_game(self):
        self.score_x = 0
        self.score_o = 0
        self.move_count = 0
        self.win_line = None
        self.player_won = None
        self.board = DEFAULT_BOARD.copy()
