
from kivy.uix.button import Button
from kivy.graphics import Color, Line
from .colors import MAIN_TEXT_COLOR, BACKGROUND_COLOR


class BoardButton(Button):
  def __init__(self, **kwargs):
    super(BoardButton, self).__init__(**kwargs)
    self.font_size = 32
    self.background_normal = ""
    self.color = MAIN_TEXT_COLOR
    self.background_color = BACKGROUND_COLOR


class KeypadButton(Button):
  def __init__(self, **kwargs):
    super(KeypadButton, self).__init__(**kwargs)
    self.font_size = 20
    self.background_normal = ""
    self.color = MAIN_TEXT_COLOR
    self.background_color = BACKGROUND_COLOR

    self.bind(pos=self.update_canvas, size=self.update_canvas)

  def update_canvas(self, *args):   
    self.canvas.before.clear()

    with self.canvas.before:
      Color(*MAIN_TEXT_COLOR)
      Line(rectangle=(self.x, self.y, self.width, self.height), width=2)