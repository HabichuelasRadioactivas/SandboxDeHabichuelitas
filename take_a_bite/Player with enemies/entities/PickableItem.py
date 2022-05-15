import arcade
from utils.object_tags import *


class PickableItem(arcade.Sprite):
    """Pick-able item class"""

    def __init__(self, filename, x_pos, y_pos, tag=DEFAULT_CONSUMABLE, sprite_scaling=1):
        super().__init__(filename, center_x=x_pos, center_y=y_pos, scale=sprite_scaling)

        self.tag = tag
