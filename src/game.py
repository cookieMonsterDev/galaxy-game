import copy
from enum import Enum

from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.gridlayout import GridLayout

from src.colors import MAIN_TEXT_COLOR, BACKGROUND_COLOR 
from .buttons import KeypadButton, BoardButton

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

DEFAULT_BOARD = [None] * 9

# class PlayerName(Enum):
#   X = "X"
#   O = "O"

# class Game:
#   def __init__(self):
#     self.round = 0
#     self.player_x_score = 0
#     self.player_o_score = 0
#     self.first_turn = None
#     self.player_turn = None
#     self.player_won = None
#     self.is_ended = False
#     self.is_blocked = False
#     self.field = copy.deepcopy(DEFAULT_FIELD)

#   def choose_player(self, player: PlayerName) -> None:
#     self.first_turn = player
#     self.player_turn = player
#     self.is_blocked = False

#   def reset_round(self) -> None:
#     self.field = copy.deepcopy(DEFAULT_FIELD)
#     self.player_turn = self.first_turn
#     self.player_won = None
#     self.is_ended = False
#     self.is_blocked = False

#   def new_round(self) -> None:
#     self.round += 1
#     self.reset_round()

#   def reset_game(self) -> None:
#     print('reset')
#     self.__init__()

#   def move(self, slot: int) -> None:
#     if self.field[slot] is not None or self.is_blocked:
#       return

#     self.field[slot] = self.player_turn

#     for combination in WINNING_COMBINATIONS:
#       if all(self.field[index] == self.player_turn for index in combination):
#         self.player_won = self.player_turn
#         self.is_ended = True
#         self.is_blocked = True

#         if self.player_won == PlayerName.X.value:
#           self.player_x_score += 1
#           self.player_turn = PlayerName.O.value
#         else:
#           self.player_o_score += 1
#           self.player_turn = PlayerName.X.value
#         return

#     if self.player_turn == PlayerName.X.value:
#         self.player_turn = PlayerName.O.value
#     else:
#         self.player_turn = PlayerName.X.value



class Game(BoxLayout):
  def __init__(self, **kwargs):
    super(Game, self).__init__(**kwargs)
    self.padding = 20
    self.orientation = 'vertical'
    self.bind(pos=self.update_canvas, size=self.update_canvas)


  def update_game_canvas(self, *args):
    self.canvas.before.clear()
    with self.canvas.before:
      Color(*BACKGROUND_COLOR)
      Rectangle(pos=self.pos, size=self.size)


  def render_board(self):
    board = GridLayout(cols=3, spacing=4, size_hint_y=0.7)

    with board.canvas.before:
      Color(*MAIN_TEXT_COLOR)
      Rectangle(
        pos=(board.pos[0] + 2, board.pos[1] + 2),
        size=(board.width - 4, board.height - 4) 
      )
    
    for item in self.board:
      button = BoardButton(text=item if item != None else "")
      board.add_widget(button)

    self.add_widget(board)


  def update_board_canvas(self, board, *args):
    board.canvas.before.clear()

    with board.canvas.before:
        Color(*MAIN_TEXT_COLOR)
        Rectangle(
          pos=(board.x + 2, board.y + 2), 
          size=(board.width - 4, board.height - 4) 
        )

  def render_keypad(self):
    keypad = BoxLayout(spacing=20, size_hint_y=0.1, padding=(0, 30, 0, 0))

    left_button = KeypadButton(text="Reset Game")
    right_button = KeypadButton(text="Reset Round")

    keypad.add_widget(left_button)
    keypad.add_widget(right_button)

    self.add_widget(keypad)
