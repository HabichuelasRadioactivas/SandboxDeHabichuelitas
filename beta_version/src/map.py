import arcade
from load_assets import MAP_PATH
from game_parameters import *


def load_map(map_number):
    if map_number == 1:
        return arcade.Scene.from_tilemap(arcade.load_tilemap(MAP_PATH[0], 1.30))
    if map_number == 2:
        return arcade.Scene.from_tilemap(arcade.load_tilemap(MAP_PATH[1], 1.30))
    if map_number == 3:
        return arcade.Scene.from_tilemap(arcade.load_tilemap(MAP_PATH[2], 1.30))
    if map_number == 4:
        return arcade.Scene.from_tilemap(arcade.load_tilemap(MAP_PATH[3], 1.30))
    raise Exception(f"\n\nError while loading tilemap: There does no map number '{map_number}' exist!")


"""
class Map():
    def __init__(self, path: str, entry_side: str, entry_boundaries: tuple, exit_side: str, exit_boundaries: tuple):
        SIDES = ["LEFT, RIGHT, UP, DOWN"]
        assert entry_side in SIDES, f"Parameter entry_side must have one of the following values:\n" \
                                    f"{SIDES}\n" \
                                    f"Got {entry_side} instead."
        assert exit_side in SIDES, f"Parameter entry_side must have one of the following values:\n" \
                                   f"{SIDES}\n" \
                                   f"Got {exit_side} instead."
        assert isinstance(entry_boundaries, tuple) and len(entry_boundaries) == 2, \
            f"Map class: ERROR in entry_boundaries."
        assert isinstance(entry_boundaries[0], int) and isinstance(entry_boundaries[1], int), \
            f"Map class: ERROR in entry_boundaries."
        assert isinstance(exit_boundaries, tuple) and len(exit_boundaries) == 2, \
            f"Map class: ERROR in exit_boundaries."
        assert isinstance(exit_boundaries[0], int) and isinstance(exit_boundaries[1], int), \
            f"Map class: ERROR in exit_boundaries."

        self._scene = arcade.Scene.from_tilemap(arcade.load_tilemap(path, 1.30))

        self._entry_side = entry_side
        self._entry_boundaries = entry_boundaries

        self._exit_side = exit_side
        self._exit_boundaries = exit_boundaries

        self._threshold = 10  # Threshold of pixel for entering another map

    def get_scene(self):
        return self._scene

    def at_entry(self, x_pos, y_pos):
        if self._entry_side == "LEFT":
            return x_pos <= 0 + self._threshold and \
                   self._entry_boundaries[0] < y_pos < self._entry_boundaries[1]
        if self._entry_side == "RIGHT":
            return x_pos >= SCREEN_WIDTH - self._threshold and \
                   self._entry_boundaries[0] < y_pos < self._entry_boundaries[1]
        
        if self._entry_side == "UP":
            return y_pos >= SCREEN_HEIGHT - self._threshold and \
                   self._entry_boundaries[0] < x_pos < self._entry_boundaries[1]
        if self._entry_side == "DOWN":
            return y_pos >= SCREEN_HEIGHT + self._threshold and \
                   self._entry_boundaries[0] < x_pos < self._entry_boundaries[1]

    def at_exit(self, x_pos, y_pos):
        if self._exit_side == "LEFT":
            return x_pos <= 0 + self._threshold and \
                   self._exit_boundaries[0] < y_pos < self._exit_boundaries[1]
        if self._exit_side == "RIGHT":
            return x_pos >= SCREEN_WIDTH - self._threshold and \
                   self._exit_boundaries[0] < y_pos < self._exit_boundaries[1]

        if self._exit_side == "UP":
            return y_pos >= SCREEN_HEIGHT - self._threshold and \
                   self._exit_boundaries[0] < x_pos < self._exit_boundaries[1]
        if self._exit_side == "DOWN":
            return y_pos >= SCREEN_HEIGHT + self._threshold and \
                   self._exit_boundaries[0] < x_pos < self._exit_boundaries[1]
"""
