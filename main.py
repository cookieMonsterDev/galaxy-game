# import pygame

# # pygame setup
# pygame.init()
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((1280, 720))


# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False


#     # RENDER YOUR GAME HERE


#     pygame.display.flip()

#     clock.tick(60)

# pygame.quit()


import pygame
from pygame.locals import QUIT
from src.board_button import BoardButton  # Assuming the class is saved in `board_button.py`

click_count = 0
state = 0  # Start with state 0 (circle)

def button_clicked(button):
    global state
    global click_count
    print("Button was clicked!")
    button.set_state(state)  # Update the button state
    if state == 0:
        state = 1  # Switch to state 1 (cross)
    elif state == 1:
        state = 0  # Switch back to state 0 (circle)
    click_count += 1
    print(click_count)     

pygame.init()
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

button = BoardButton(100, 100)
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Detect click and call the callback
    button.on_click(button_clicked)

    # Update and redraw the screen
    screen.fill((255, 255, 255))  # Clear the screen
    button.draw(screen)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()