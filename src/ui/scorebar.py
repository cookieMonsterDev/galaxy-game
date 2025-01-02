from enum import Enum
from pygame import Rect, draw
from config import PALE_GOLDENROD_COLOR, CHESTNUT_BROWN_COLOR, COLDEN_OCHRE_COLOR


class Scorebar:
  def __init__(self, score_x=0, score_o=0, player_won=None, left=0, top=0, width=312, height=100, backgroundColor=PALE_GOLDENROD_COLOR, textPrimaryColor=CHESTNUT_BROWN_COLOR, textSecondaryColor=COLDEN_OCHRE_COLOR):
    self.score_x = score_x
    self.score_o = score_o
    self.player_won = player_won
    self.backgroundColor = backgroundColor
    self.textPrimaryColor = textPrimaryColor
    self.textSecondaryColor = textSecondaryColor
    self.__rect = Rect(left, top, width, height)

  def draw(self, screen):
    draw.rect(screen, self.backgroundColor, self.__rect)