from enum import Enum
from config import WINNING_COMBINATIONS

DEFAULT_BOARD = [0] * 9

class Players(Enum):
    PLAYER_X = 1
    PLAYER_O = 2


class Game:
    def __init__(
        self,
        board=DEFAULT_BOARD.copy(),
        turn=Players.PLAYER_X.value,
        score_x=0,
        score_o=0,
        player_won=None,
        move_count=0,
    ):
        self.turn = turn
        self.board = board
        self.is_full = False
        self.score_x = score_x
        self.score_o = score_o
        self.move_count = move_count
        self.player_won = player_won

    def __check_win(self):
        for item in WINNING_COMBINATIONS:
            board_item_1 = self.board[item[0]]
            board_item_2 = self.board[item[1]]
            board_item_3 = self.board[item[2]]

            if board_item_1 == board_item_2 == board_item_3 and board_item_1 != 0:
                return (True, board_item_1)

        return (False, 0)

    def move(self, index):
        if self.board[index] != 0:
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

        self.is_full = 0 not in self.board
        if self.is_full:
            return

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

        self.player_won = None

    def rest_game(self):
        self.score_x = 0
        self.score_o = 0
        self.move_count = 0
        self.player_won = None
        self.board = DEFAULT_BOARD.copy()
