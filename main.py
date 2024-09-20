from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from game import Game

class PlayField(GridLayout):
  def __init__(self, game: Game, **kwargs):
    super().__init__(**kwargs)
    self.cols = 3
    self.game = game

    field = self.game.get_state()['field']
 
    for index, item in enumerate(field):
      print(index, item)
      button_text = ""

      if item:
        button_text = item
      
      button = Button(text=button_text)
      self.add_widget(button)


class KeyPad(GridLayout):
  def __init__(self, game: Game, **kwargs):
    super().__init__(**kwargs)
    self.cols = 2
    self.game = game

    reset_game_button = Button(text="Reset Game")
    reset_round_button = Button(text="Reset Round")

    reset_game_button.bind(on_press=self.game.reset_game)
    reset_round_button.bind(on_press=self.game.reset_round)

    self.add_widget(reset_game_button)
    self.add_widget(reset_round_button)


class TicTacToeApp(App):
  def build(self):
    game = Game()
    root_layout = BoxLayout(orientation="vertical")

    root_layout.add_widget(PlayField(game))
    root_layout.add_widget(KeyPad(game))

    return root_layout 

if __name__ == '__main__':
    TicTacToeApp().run()