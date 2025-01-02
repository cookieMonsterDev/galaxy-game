from pygame import Rect, draw
from .board_button import BoardButton
from .config import CHESTNUT_BROWN_COLOR

items = [None, None, None, None, None, None, None, None, None]

class Board:
  def __init__(self, grid = items, turn = 1, left = 0, top = 0, width=252, height=252, gap_x = 6, gap_y = 6):
    self.__grid = grid
    self.__turn = turn
    self.__buttons = []
    self.__gap_x = gap_x
    self.__gap_y = gap_y
    self.__color = CHESTNUT_BROWN_COLOR
    self.__rect = Rect(left, top, width, height)
    self.__init_buttons()

  def __init_buttons(self):
    button_width = 80
    button_height = 80
    for column in range(3):
      for row in range(3):
        index = row * 3 + column
        button_top = row * (button_height + self.__gap_y)
        button_left = column * (button_width + self.__gap_x)
        button = BoardButton(left=button_left, top=button_top, state=1)
        self.__buttons.append(button)

  def __on_button_click(self, index, button):
    pass

  def draw(self, screen):
    draw.rect(screen, self.__color, self.__rect)
    for button in self.__buttons:
      button.draw(screen)





