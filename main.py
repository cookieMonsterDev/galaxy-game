from kivy.app import App
from kivy.uix.popup import Popup
from kivy.core.window import Window 
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.label import Label
from kivy.uix.button import Button

from game import Game

class TicTacToeGame(BoxLayout):
  game: Game

  def __init__(self, **kwargs):
    super(TicTacToeGame, self).__init__(**kwargs)
    self.game = Game()

  def update(self):
    state = self.game.get_state()
    pass


class TicTacToeApp(App):
  def build(self):
    Window.size = (400, 600)
    Window.minimum_width = 400
    Window.minimum_height = 600
    return TicTacToeGame()

if __name__ == '__main__':
    TicTacToeApp().run()
