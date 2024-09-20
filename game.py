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
  __round: int
  __player_x_score: int
  __player_o_score: int 
  __first_turn: Union[Turn, None]
  __player_turn: Union[Turn, None]
  __player_won: Union[Turn, None]
  __is_ended: bool 
  __is_blocked: bool
  __field: list[Union[Turn, None]]

  def __init__(self):
    self.__round = 0
    self.__player_x_score = 0
    self.__player_o_score = 0
    self.__first_turn = None
    self.__player_turn = None
    self.__player_won = None
    self.__is_ended = False 
    self.__is_blocked = True
    self.__field = copy.deepcopy(DEFAULT_FIELD)
  
  def get_state(self) -> dict:
    return {
      "round": self.__round,
      "player_x_score": self.__player_x_score,
      "player_o_score": self.__player_o_score,
      "first_turn": self.__first_turn,
      "player_turn": self.__player_turn,
      "player_won": self.__player_won,
      "is_ended": self.__is_ended,
      "is_blocked": self.__is_blocked,
      "field": self.__field,
    }
  
  def choose_player(self, player: Turn) -> None:
    self.__first_turn = player
    self.__player_turn = player
    self.__is_blocked = False

  def reset_round(self) -> None:    
    self.__field = copy.deepcopy(DEFAULT_FIELD)
    self.__player_turn = self.__first_turn
    self.__player_won = None
    self.__is_ended = False
    self.__is_blocked = False

  def new_round(self) -> None:
    self.__round += 1
    self.reset_round()

  def reset_game(self) -> None:
    self.__init__()

  def move(self, slot: int) -> None:
    if self.__field[slot] != None | self.__is_blocked:
      return
    
    self.__field[slot] = self.__player_turn

    for combination in WINNING_COMBINATIONS:
      if self.__field[combination[0]] == self.__field[combination[1]] == self.__field[combination[2]] != None:
        
        self.__player_won = self.__player_turn
        self.__is_ended = True
        self.__is_blocked = True

        if self.__player_won == Turn.X:
          self.__player_x_score += 1
          self.__player_turn = Turn.O

        if self.__player_won == Turn.O:
          self.__player_o_score += 1
          self.__player_turn = Turn.X

        return

    if self.__player_turn == Turn.X:
      self.__player_turn = Turn.O
  
    if self.__player_turn == Turn.O:
      self.__player_turn = Turn.X
