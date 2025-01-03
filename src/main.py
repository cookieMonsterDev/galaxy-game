import pygame
from game import Game
from ui.board import Board
from ui.keypad import Keypad
from pygame.locals import QUIT
from ui.scorebar import Scorebar
from ui.board_button import BoardButton
from config import PALE_GOLDENROD_COLOR

pygame.init()
screen = pygame.display.set_mode((332, 522))
clock = pygame.time.Clock()

padding = 10
running = True
game = Game()


def create_board_button_callback(index):
    def callback():
        game.move(index)
        update()

    return callback


def create_keypad_button_callback(fn):
    def callback():
        fn()
        update()

    return callback


def create_scorebar_params():
    return {
        "turn": game.turn,
        "is_full": game.is_full,
        "score_x": game.score_x,
        "score_o": game.score_o,
        "move_count": game.move_count,
        "player_won": game.player_won,
    }


def create_board_params():
    buttons = []
    for index, state in enumerate(game.board):
        callback = create_board_button_callback(index)
        button = BoardButton(state=state, callback=callback)
        buttons.append(button)
    return {"items": buttons, "win_line": game.win_line}


def create_keypad_params():
    left_text = "Reset Game"
    left_callback = create_keypad_button_callback(game.rest_game)
    right_text = "New Round" if game.player_won else "Reset Round"
    right_callback = create_keypad_button_callback(game.new_round)

    return {
        "left_text": left_text,
        "right_text": right_text,
        "left_callback": left_callback,
        "right_callback": right_callback,
    }


def update():
    global board
    global keypad
    global scorebar
    scorebar = Scorebar(top=padding, left=padding, **create_scorebar_params())
    board = Board(top=(2 * padding) + 100, left=padding, **create_board_params())
    keypad = Keypad(top=(4 * padding) + 412, left=padding, **create_keypad_params())


update()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(PALE_GOLDENROD_COLOR)

    scorebar.draw(screen)
    board.draw(screen)
    keypad.draw(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
