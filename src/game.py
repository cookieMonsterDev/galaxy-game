from enum import Enum

DEFAULT_GRID = [0] * 9
WINNING_COMBINATIONS = (
  (0, 1, 2),
  (3, 4, 5),
  (6, 7, 8),
  (0, 3, 6),
  (1, 4, 7),
  (2, 5, 8),
  (0, 4, 8),
  (2, 4, 6)
)

class Players(Enum):
  PLAYER_X = 1
  PLAYER_O = 2

class Game:
  def __init__(self, grid = DEFAULT_GRID.copy(), turn = Players.PLAYER_X, score_x = 0, score_o = 0, player_won = None, move_count = 0):
    self.grid = grid
    self.turn = turn
    self.is_full = False
    self.score_x = score_x
    self.score_o = score_o
    self.move_count = move_count
    self.player_won = player_won

  def __check_win(self):
    for item in WINNING_COMBINATIONS:
      grid_item_1 = self.grid[item[0]]
      grid_item_2 = self.grid[item[1]]
      grid_item_3 = self.grid[item[2]]
      if grid_item_1 == grid_item_2 == grid_item_3 and grid_item_1 != 0:
        return (True, grid_item_1)
    return (False, 0)

  def move(self, index):
    if self.grid[index] != 0:
      return
    self.grid[index] = self.turn
    self.move_count += 1
    if self.move_count < 5:
      return
    self.is_full = 0 not in self.grid
    if self.is_full:
      return
    (isWin, player) = self.__check_win()
    if isWin:
      if player == Players.PLAYER_X:
        self.score_x += 1
        self.player_won = Players.PLAYER_X
      if player == Players.PLAYER_O:
        self.score_o += 1
        self.player_won = Players.PLAYER_O
    
  def new_round(self):
    self.move_count = 0
    self.grid = DEFAULT_GRID.copy()
    if self.player_won == Players.PLAYER_X:
      self.turn = Players.PLAYER_O
    if self.player_won == Players.PLAYER_O:
      self.turn = Players.PLAYER_X
    self.player_won = None

  def rest_game(self):
    self.score_x = 0
    self.score_o = 0
    self.move_count = 0
    self.player_won = None
    self.grid = DEFAULT_GRID.copy()
