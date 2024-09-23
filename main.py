from enum import Enum
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


from src.game import Game

class Color(Enum):
  X = (255/255, 51/255, 51/255, 1)
  O = (25/255, 140/255, 255/255, 1)
  N = (255/255, 255/255, 255/255, 1)

class TicTacToeGame(BoxLayout):
  game: Game

  def __init__(self, **kwargs):
    super(TicTacToeGame, self).__init__(**kwargs)

    self.game = Game()

    print(self.game.get_state())

  def render_info_bar(self):
    pass

  def render_field(self):
    pass

  def render_keypad(self):
    pass


class TicTacToeApp(App):
  def build(self):
    Window.size = (400, 600)
    Window.minimum_width = 400
    Window.minimum_height = 600
    return TicTacToeGame()

if __name__ == '__main__':
    TicTacToeApp().run()
