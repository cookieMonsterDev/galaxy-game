from pygame import Rect, draw
from .keypad_button import KeypadButton
from config import PALE_GOLDENROD_COLOR

class Keypad:
    def __init__(
        self,
        left=0,
        top=0,
        width=312,
        height=60,
        backgroundColor=PALE_GOLDENROD_COLOR,
        left_text="left_button",
        left_callback=None,
        right_text="right_button",
        right_callback=None,
    ):
        self.left_text = left_text
        self.right_text = right_text
        self.left_callback = left_callback
        self.right_callback = right_callback
        self.backgroundColor = backgroundColor
        self.rect = Rect(left, top, width, height)

    def draw(self, screen):
        draw.rect(screen, self.backgroundColor, self.rect)

        width = 151
        height = 60

        left = self.rect.left
        right = self.rect.width - width + 10
        top = self.rect.top + (self.rect.height - height) // 2

        left_button = KeypadButton(
            text=self.left_text,
            callback=self.left_callback,
            top=top,
            left=left,
            width=width,
            height=height,
        )
        right_button = KeypadButton(
            text=self.right_text,
            callback=self.right_callback,
            top=top,
            left=right,
            width=width,
            height=height,
        )

        left_button.draw(screen)
        right_button.draw(screen)
