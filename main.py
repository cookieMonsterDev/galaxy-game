from kivy.app import App
from kivy.core.window import Window 
from kivy.uix.boxlayout import BoxLayout

from game import Game

class TicTacToeGame(BoxLayout):
  pass

class TicTacToeApp(App):
  def build(self):
    Window.size = (400, 500)
    Window.minimum_width = 400
    Window.minimum_height = 500
    Window.set_title("Tic Tac Toe Game")
    Window.clearcolor = (10/255, 10/255, 35/255, 1)

    return TicTacToeGame()

if __name__ == '__main__':
    TicTacToeApp().run()
