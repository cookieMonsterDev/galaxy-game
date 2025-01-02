from pygame import Rect, draw, mouse

class BoardButton:
  def __init__(self, left, top, width=50, height=50):
    self.__rect = Rect(left, top, width, height)
    self.__color = (0, 0, 0)
    self.__state = None
    self.__clicked = False 

  def draw(self, screen):
    draw.rect(screen, self.__color, self.__rect)
    if self.__state == 0:
      self.__draw_circle(screen)
    if self.__state == 1:
      self.__draw_cross(screen)

  def __draw_circle(self, screen):
    center = self.__rect.center
    radius = self.__rect.width // 3
    draw.circle(screen, (255, 0, 0), center, radius, width=3)

  def __draw_cross(self, screen):
    padding = 10
    x1, y1 = self.__rect.topleft
    x2, y2 = self.__rect.bottomright
    draw.line(screen, (0, 0, 255), (x1 + padding, y1 + padding), (x2 - padding, y2 - padding), width=3)
    draw.line(screen,(0, 0, 255), (x2 - padding, y1 + padding), (x1 + padding, y2 - padding), width=3)

  def set_state(self, new_state):
    self.__state = new_state

  def __is_clicked(self):
    return self.__rect.collidepoint(mouse.get_pos()) and mouse.get_pressed()[0]

  def on_click(self, callback):
    if self.__is_clicked():
      if not self.__clicked:
        callback(self)
      self.__clicked = True
    else:
      self.__clicked = False
 