from enum import Enum
from pygame import draw
from .button import Button
from config import COLDEN_OCHRE_COLOR

class BoardButtonState(Enum):
    EMPTY = None
    CROSS = "X"
    CIRCLE = "O"

class BoardButton(Button):
    def __init__(
        self, state=BoardButtonState.EMPTY, textColor=COLDEN_OCHRE_COLOR, **kwargs
    ):
        super().__init__(**kwargs)
        self.state = state
        self.textColor = textColor

    def __draw_circle(self, screen):
        center = self.rect.center
        radius = self.rect.width // 2.5
        draw.circle(screen, self.textColor, center, radius, width=6)

    def __draw_cross(self, screen):
        padding = 10
        x1, y1 = self.rect.topleft
        x2, y2 = self.rect.bottomright
        draw.line(
            screen,
            self.textColor,
            (x1 + padding, y1 + padding),
            (x2 - padding, y2 - padding),
            width=8,
        )
        draw.line(
            screen,
            self.textColor,
            (x2 - padding, y1 + padding),
            (x1 + padding, y2 - padding),
            width=8,
        )

    def draw(self, screen, top=None, left=None):
        self.rect.top = top or self.top
        self.rect.left = left or self.left
        super().draw(screen)
        if self.state == BoardButtonState.CIRCLE.value:
            self.__draw_circle(screen)
        elif self.state == BoardButtonState.CROSS.value:
            self.__draw_cross(screen)
