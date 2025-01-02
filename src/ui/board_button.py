from enum import Enum
from pygame import Rect, draw, mouse, MOUSEBUTTONDOWN
from config import PALE_GOLDENROD_COLOR, CHESTNUT_BROWN_COLOR

class ButtonState(Enum):
  EMPTY = 0
  CROSS = 1
  CIRCLE = 2

class BoardButton:
  def __init__(self, state=ButtonState.EMPTY, top=0, left=0, callback=None, width=100, height=100, backgroundColor=PALE_GOLDENROD_COLOR, textColor=CHESTNUT_BROWN_COLOR):
    self.state = state
    self.callback = callback
    self.textColor = textColor
    self.backgroundColor = backgroundColor
    self.rect = Rect(left, top, width, height)

  def __draw_circle(self, screen):
    center = self.rect.center
    radius = self.rect.width // 2.5
    draw.circle(screen, self.textColor, center, radius, width=6)

  def __draw_cross(self, screen):
    padding = 10
    x1, y1 = self.rect.topleft
    x2, y2 = self.rect.bottomright
    draw.line(screen, self.textColor, (x1 + padding, y1 + padding), (x2 - padding, y2 - padding), width=8)
    draw.line(screen, self.textColor, (x2 - padding, y1 + padding), (x1 + padding, y2 - padding), width=8)

  def draw(self, screen, top=0, left=0):
    self.rect.top = top
    self.rect.left = left
    draw.rect(screen, self.backgroundColor, self.rect)
    if self.state == ButtonState.CIRCLE:
      self.__draw_circle(screen)
    elif self.state == ButtonState.CROSS:
      self.__draw_cross(screen)

  def is_hovered(self):
    mouse_pos = mouse.get_pos()
    return self.rect.collidepoint(mouse_pos)

  def handle_event(self, event):
    if event.type == MOUSEBUTTONDOWN and self.is_hovered():
      self.callback()

 