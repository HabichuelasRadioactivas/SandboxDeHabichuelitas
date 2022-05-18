import arcade
from typing import List


def load_textures(append_to: List, sprites: List[str], flip_hor=False):
    for i in range(len(sprites)):
        append_to.append(arcade.load_texture(sprites[i], flipped_horizontally=flip_hor))