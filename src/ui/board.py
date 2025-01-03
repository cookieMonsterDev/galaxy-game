from pygame import Rect, draw
from config import CHESTNUT_BROWN_COLOR, PALE_GOLDENROD_COLOR


class Board:
    def __init__(
        self,
        top=0,
        left=0,
        item_width=100,
        item_height=100,
        gap_x=6,
        gap_y=6,
        items=None,
        win_line=0,
        background_color=CHESTNUT_BROWN_COLOR,
        line_border_color=CHESTNUT_BROWN_COLOR,
        line_background_color=PALE_GOLDENROD_COLOR,
    ):
        self.items = items
        self.gap_y = gap_y
        self.gap_x = gap_x
        self.win_line = win_line
        self.item_width = item_width
        self.item_height = item_height
        self.background_color = background_color
        self.items = items or [None] * 9
        height = 3 * item_height + 2 * gap_y
        width = 3 * item_width + 2 * gap_x
        self.line_border_color = line_border_color
        self.line_background_color = line_background_color
        self.rect = Rect(left, top, width, height)

    def __draw_items(self, screen):
        for column in range(3):
            for row in range(3):
                index = row * 3 + column

                if index >= len(self.items):
                    break

                top = self.rect.top + row * (self.item_height + self.gap_y)
                left = self.rect.left + column * (self.item_width + self.gap_x)
                item = self.items[index]

                if item:
                    item.draw(screen, top, left)

    def __draw_win_line(self, screen):
        if not self.win_line:
            return

        padding = 10
        start_pos, end_pos = None, None

        if self.win_line == 0:
            y = self.rect.top + self.item_height // 2
            start_pos = (self.rect.left + padding, y)
            end_pos = (self.rect.right - padding, y)

        if self.win_line == 1:
            y = self.rect.top + self.item_height + self.gap_y + self.item_height // 2
            start_pos = (self.rect.left + padding, y)
            end_pos = (self.rect.right - padding, y)

        if self.win_line == 2:
            y = self.rect.bottom - self.item_height // 2
            start_pos = (self.rect.left + padding, y)
            end_pos = (self.rect.right - padding, y)

        if self.win_line == 3:
            x = self.rect.left + self.item_width // 2
            start_pos = (x, self.rect.top + padding)
            end_pos = (x, self.rect.bottom - padding)

        if self.win_line == 4:
            x = self.rect.left + self.item_width + self.gap_x + self.item_width // 2
            start_pos = (x, self.rect.top + padding)
            end_pos = (x, self.rect.bottom - padding)

        if self.win_line == 5:
            x = self.rect.right - self.item_width // 2
            start_pos = (x, self.rect.top + padding)
            end_pos = (x, self.rect.bottom - padding)

        if self.win_line == 6:
            start_pos = (self.rect.left + padding, self.rect.top + padding)
            end_pos = (self.rect.right - padding, self.rect.bottom - padding)

        if self.win_line == 7:
            start_pos = (self.rect.right - padding, self.rect.top + padding)
            end_pos = (self.rect.left + padding, self.rect.bottom - padding)

        draw.line(
            screen,
            self.line_border_color,
            start_pos,
            end_pos,
            width=8,
        )

        draw.line(
            screen,
            self.line_background_color,
            start_pos,
            end_pos,
            width=6,
        )

    def draw(self, screen):
        draw.rect(screen, self.background_color, self.rect)
        self.__draw_items(screen)
        self.__draw_win_line(screen)
