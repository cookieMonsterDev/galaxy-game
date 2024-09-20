from enum import Enum
from typing import Union
import copy

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

DEFAULT_FIELD = [None] * 9

class Turn(Enum):
  X = "X"
  O = "O"

class Game:
  round: int
  player_x_score: int
  player_o_score: int 
  first_turn: Union[Turn, None]
  player_turn: Union[Turn, None]
  player_won: Union[Turn, None]
  is_ended: bool 
  is_blocked: bool
  field: list[Union[Turn, None]]

  def __init__(self):
    self.round = 0
    self.player1_score = 0
    self.player2_score = 0
    self.first_turn = None
    self.player_turn = None
    self.player_won = None
    self.is_ended = False 
    self.is_blocked = True
    self.field = copy.deepcopy(DEFAULT_FIELD)
  
  def get_state(self) -> dict:
    return {
      "round": self.round,
      "player_x_score": self.player_x_score,
      "player_o_score": self.player_o_score,
      "first_turn": self.first_turn,
      "player_turn":self.player_turn,
      "is_ended": self.is_ended,
      "is_blocked": self.is_blocked,
      "field":self.field,
    }
  
  def choose_player(self, player: Turn) -> None:
    self.first_turn = player
    self.player_turn = player
    self.is_blocked = False

  def reset_round(self) -> None:    
    self.field = DEFAULT_FIELD
    self.player_turn = self.first_turn
    self.player_won = None
    self.is_ended = False
    self.is_blocked = False

  def new_round(self) -> None:
    self.first_turn = self.player_turn
    self.field = DEFAULT_FIELD
    self.player_won = None
    self.is_ended = False
    self.is_blocked = False

  def reset_game(self) -> None:
    self.__init__()

  def move(self, slot: int) -> None:
    if self.field[slot] != None | self.is_blocked:
      return
    
    self.field[slot] = self.player_turn

    for combination in WINNING_COMBINATIONS:
      if self.field[combination[0]] == self.field[combination[1]] == self.field[combination[2]] != None:
        
        self.player_won = self.player_turn
        self.is_ended = True
        self.is_blocked = True

        if self.player_won == Turn.X:
          self.player_x_score += 1
          self.player_turn = Turn.O

        if self.player_won == Turn.O:
          self.player_o_score += 1
          self.player_turn = Turn.X

        return

    if self.player_turn == Turn.X:
      self.player_turn = Turn.O
  
    if self.player_turn == Turn.O:
      self.player_turn = Turn.X
