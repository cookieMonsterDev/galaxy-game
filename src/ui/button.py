from pygame import Rect, draw, mouse
from config import PALE_GOLDENROD_COLOR


class Button:
    def __init__(
        self,
        top=0,
        left=0,
        width=100,
        height=100,
        callback=None,
        background_color=PALE_GOLDENROD_COLOR,
    ):
        self.top = top
        self.left = left
        self.clicked = False
        self.callback = callback
        self.background_color = background_color
        self.rect = Rect(left, top, width, height)

    def __handle_click(self):
        if not self.callback:
            return

        mouse_pos = mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                self.callback()

        if mouse.get_pressed()[0] == 0:
            self.clicked = False

    def draw(self, screen):
        self.__handle_click()
        draw.rect(screen, self.background_color, self.rect)
