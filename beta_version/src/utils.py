import arcade
from game_parameters import *
from object_tags import *
from load_assets import HEART_ICON, DEFAULT_ABILITY_ICON, PINK_ABILITY_ICON


def normal_or_boosted_speed(is_powered, item_picked):
    if is_powered:
        if item_picked == DEFAULT_CONSUMABLE:
            return MOVEMENT_SPEED_REDUCTION
        return MOVEMENT_SPEED_POWERUP
    else:
        return MOVEMENT_SPEED


def draw_player_health(self):
    icon_pos = [21, SCREEN_HEIGHT - 55]
    for i in range(self.player_sprite.health_points):
        self.health_icon = arcade.Sprite(HEART_ICON, 1.5, center_x=icon_pos[0], center_y=icon_pos[1])
        self.health_icon.draw()
        icon_pos = [21 + self.health_icon.width * (i + 1), SCREEN_HEIGHT - 55]

def set_ability_icon(item_picked):
    icon_pos = [SCREEN_WIDTH - 32, SCREEN_HEIGHT - 32]
    if item_picked == DEFAULT_CONSUMABLE:
        return arcade.Sprite(DEFAULT_ABILITY_ICON, 2, center_x=icon_pos[0], center_y=icon_pos[1])
    if item_picked == PINK_CONSUMABLE:
        return arcade.Sprite(PINK_ABILITY_ICON, 2, center_x=icon_pos[0], center_y=icon_pos[1])