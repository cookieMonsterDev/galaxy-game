from .button import Button
from pygame import font, draw
from config import CHESTNUT_BROWN_COLOR


class KeypadButton(Button):
    def __init__(
        self,
        text="button",
        text_color=CHESTNUT_BROWN_COLOR,
        border_color=CHESTNUT_BROWN_COLOR,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.text = text
        self.text_color = text_color
        self.border_color = border_color
        self.font = font.Font(None, 30)

    def __draw_text(self, screen):
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def draw(self, screen, top=None, left=None):
        self.rect.top = top or self.top
        self.rect.left = left or self.left
        super().draw(screen)
        draw.rect(screen, self.border_color, self.rect, 4)
        self.__draw_text(screen)
