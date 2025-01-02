import pygame
from game import Game
from ui.board import Board
from ui.keypad import Keypad
from pygame.locals import QUIT
from ui.scorebar import Scorebar
from ui.board_button import BoardButton
from config import PALE_GOLDENROD_COLOR

pygame.init()
screen = pygame.display.set_mode((332, 720))
clock = pygame.time.Clock()

padding = 10
running = True
game = Game()

board_buttons = []

def create_callback(index):
    def callback():
        game.move(index)
        print("click on", index, game.board)
    return callback

for index, state in enumerate(game.board):
    button = BoardButton(state=state, callback=create_callback(index))
    board_buttons.append(button)

scorebar = Scorebar(left=padding, top=0 + padding)
board = Board(left=padding, top=100 + padding, items=board_buttons)
keypad = Keypad()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        for button in board_buttons:
            button.handle_event(event)

    # Update and redraw the screen
    screen.fill((0, 0, 0))  # Clear the screen
    scorebar.draw(screen)
    board.draw(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()