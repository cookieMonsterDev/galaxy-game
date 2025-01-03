from game import Players
from pygame import Rect, draw, font
from config import CHESTNUT_BROWN_COLOR, PALE_GOLDENROD_COLOR, COLDEN_OCHRE_COLOR


class Scorebar:
    def __init__(
        self,
        score_x=0,
        score_o=0,
        turn=None,
        move_count=0,
        is_full=False,
        player_won=None,
        left=0,
        top=0,
        width=312,
        height=100,
        backgroundColor=PALE_GOLDENROD_COLOR,
        textPrimaryColor=CHESTNUT_BROWN_COLOR,
        textSecondaryColor=COLDEN_OCHRE_COLOR,
    ):
        self.turn = turn
        self.width = width
        self.height = height
        self.is_full = is_full
        self.score_x = score_x
        self.score_o = score_o
        self.move_count = move_count
        self.player_won = player_won
        self.backgroundColor = backgroundColor
        self.textPrimaryColor = textPrimaryColor
        self.textSecondaryColor = textSecondaryColor
        self.rect = Rect(left, top, width, height)

    def __draw_score_x(self, screen):
        label_font = font.Font(None, 24)
        value_font = font.Font(None, 30)
        label_surface = label_font.render("Score-X:", True, self.textPrimaryColor)
        value_surface = value_font.render(f"{self.score_x}", True, self.textSecondaryColor)

        label_left = self.rect.left + 10
        label_top = self.rect.top + 10
        value_left = label_left + label_surface.get_width() + 5
        value_top = label_top - 2

        screen.blit(label_surface, (label_left, label_top))
        screen.blit(value_surface, (value_left, value_top))

    def __draw_score_o(self, screen):
        label_font = font.Font(None, 24)
        value_font = font.Font(None, 30)
        label_surface = label_font.render("Score-O:", True, self.textPrimaryColor)
        value_surface = value_font.render(f"{self.score_o}", True, self.textSecondaryColor)

        value_left = self.rect.right - 10 - value_surface.get_width()
        label_left = value_left - label_surface.get_width() - 5
        label_top = self.rect.top + 10
        value_top = label_top - 2

        screen.blit(label_surface, (label_left, label_top))
        screen.blit(value_surface, (value_left, value_top))

    def __draw_message(self, screen):
        text_container = Rect(self.rect.left, self.rect.top + 30, self.rect.width, 70)
        text_font = font.Font(None, 30)
        line_spacing = -2 
        text = ""

        if self.turn:
            text = f"Player {self.turn}'s turn"

        if self.player_won != None:
            text = f"Player {self.player_won} won"

        if self.is_full and self.player_won == None:
            text = "It seems tie"

        if self.move_count == 0:
            second = (
                Players.PLAYER_O.value
                if self.turn == Players.PLAYER_X
                else Players.PLAYER_X.value
            )
            text = f"Player {self.turn} starts first, followed by Player {second}"

        lines = []
        remaining_text = text
        font_height = text_font.size("Tg")[1]

        while remaining_text:
            i = 1

            while (
                text_font.size(remaining_text[:i])[0] < text_container.width
                and i < len(remaining_text)
            ):
                i += 1

            if i < len(remaining_text):
                i = remaining_text.rfind(" ", 0, i) + 1

            lines.append(remaining_text[:i])
            remaining_text = remaining_text[i:]

        total_text_height = len(lines) * font_height + (len(lines) - 1) * line_spacing

        y = text_container.top + (text_container.height - total_text_height) // 2

        for line in lines:
            line_surface = text_font.render(line, True, self.textPrimaryColor)
            line_rect = line_surface.get_rect(center=(text_container.centerx, y + font_height // 2))
            screen.blit(line_surface, line_rect.topleft)
            y += font_height + line_spacing

    def draw(self, screen):
        draw.rect(screen, self.backgroundColor, self.rect)
        self.__draw_score_x(screen)
        self.__draw_score_o(screen)
        self.__draw_message(screen)
