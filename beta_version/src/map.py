import arcade
from load_assets import MAP_PATH


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
