from enum import Enum
from pygame import Rect, draw
from .config import PALE_GOLDENROD_COLOR, CHESTNUT_BROWN_COLOR

class ButtonState(Enum):
  EMPTY = 0
  CROSS = 1
  CIRCLE = 2

class BoardButton:
  def __init__(self, state=ButtonState.EMPTY, left=0, top=0, width=80, height=80, backgroundColor=PALE_GOLDENROD_COLOR, textColor=CHESTNUT_BROWN_COLOR):
    self.state = state
    self.__clicked = False
    self.textColor = textColor
    self.backgroundColor = backgroundColor
    self.__rect = Rect(left, top, width, height)

  def __draw_circle(self, screen):
    center = self.__rect.center
    radius = self.__rect.width // 2.5
    draw.circle(screen, self.textColor, center, radius, width=6)

  def __draw_cross(self, screen):
    padding = 10
    x1, y1 = self.__rect.topleft
    x2, y2 = self.__rect.bottomright
    draw.line(screen, self.textColor, (x1 + padding, y1 + padding), (x2 - padding, y2 - padding), width=8)
    draw.line(screen, self.textColor, (x2 - padding, y1 + padding), (x1 + padding, y2 - padding), width=8)

  def __is_clicked(self, mouse_pos, mouse_pressed):
    return self.__rect.collidepoint(mouse_pos) and mouse_pressed[0]

  def set_state(self, new_state: ButtonState):
    self.state = new_state

  def draw(self, screen):
    draw.rect(screen, self.backgroundColor, self.__rect)
    if self.state == ButtonState.CIRCLE:
      self.__draw_circle(screen)
    elif self.state == ButtonState.CROSS:
      self.__draw_cross(screen)

  def on_click(self, mouse_pos, mouse_pressed, callback):
    if self.__is_clicked(mouse_pos, mouse_pressed):
      if not self.__clicked:
        callback(self)
      self.__clicked = True
    else:
      self.__clicked = False

 