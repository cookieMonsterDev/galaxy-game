from .button import Button
from pygame import font, draw
from config import CHESTNUT_BROWN_COLOR


class KeypadButton(Button):
    def __init__(
        self,
        text="button",
        textColor=CHESTNUT_BROWN_COLOR,
        borderColor=CHESTNUT_BROWN_COLOR,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.text = text
        self.textColor = textColor
        self.borderColor = borderColor
        self.font = font.Font(None, 30)

    def __draw_text(self, screen):
        text_surface = self.font.render(self.text, True, self.textColor)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def draw(self, screen, top=None, left=None):
        self.rect.top = top or self.top
        self.rect.left = left or self.left
        super().draw(screen)
        draw.rect(screen, self.borderColor, self.rect, 4)
        self.__draw_text(screen)
