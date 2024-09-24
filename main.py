from kivy.app import App
from kivy.core.window import Window 

from src import Game

class TicTacToeApp(App):
  def build(self):
    Window.size = (400, 600)
    Window.minimum_width = 400
    Window.minimum_height = 600
    return Game()

if __name__ == '__main__':
    TicTacToeApp().run()
