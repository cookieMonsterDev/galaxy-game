from pygame import Rect, draw
from config import CHESTNUT_BROWN_COLOR


class Board:
    def __init__(
        self,
        top=0,
        left=0,
        item_width=100,
        item_height=100,
        columns=3,
        rows=3,
        gap_x=6,
        gap_y=6,
        items=None,
        backgroundColor=CHESTNUT_BROWN_COLOR,
    ):
        self.rows = rows
        self.items = items
        self.gap_y = gap_y
        self.gap_x = gap_x
        self.columns = columns
        self.item_width = item_width
        self.item_height = item_height
        self.backgroundColor = backgroundColor
        self.items = items or [None] * (rows * columns)
        height = rows * item_height + (rows - 1) * gap_y
        width = columns * item_width + (columns - 1) * gap_x
        self.rect = Rect(left, top, width, height)

    def __draw_items(self, screen):
        for column in range(self.columns):
            for row in range(self.rows):
                index = row * self.columns + column

                if index >= len(self.items):
                    break

                top = self.rect.top + row * (self.item_height + self.gap_y)
                left = self.rect.left + column * (self.item_width + self.gap_x)
                item = self.items[index]

                if item:
                    item.draw(screen, top, left)

    def draw(self, screen):
        draw.rect(screen, self.backgroundColor, self.rect)
        self.__draw_items(screen)
