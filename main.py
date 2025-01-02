import pygame
from src.board import Board
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

running = True

board = Board(0, 0)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Update and redraw the screen
    screen.fill((0, 0, 0))  # Clear the screen
    board.draw(screen)

    # button.draw(screen)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()