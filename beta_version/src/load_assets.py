import os
import arcade
from typing import List


def load_textures(append_to: List, sprites: List[str], flip_hor=False):
    for i in range(len(sprites)):
        append_to.append(arcade.load_texture(sprites[i], flipped_horizontally=flip_hor))

file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sep = os.path.sep

player_path = file_path + sep + "assets" + sep + "sprites" + sep + "player" + sep
mr_bean_path = file_path + sep + "assets" + sep + "sprites" + sep + "mr_bean" + sep
enemies_path = file_path + sep + "assets" + sep + "sprites" + sep + "enemies" + sep
map_path = file_path + sep + "assets" + sep + "tilemaps" + sep
cutscene_path = file_path + sep+ "assets" + sep + "cutscenes" + sep

MR_BEAN_SPRITES = [f"{mr_bean_path}MrBeanCelebrating.png",
                   f"{mr_bean_path}MrBeanOnOneFoot.png",
                   f"{mr_bean_path}MrBeanWaiting.png"]

MR_BEAN_DIALOGUE = [f"{cutscene_path}{sep}mr_bean_dialogue{sep}text_1.png",
                    f"{cutscene_path}{sep}mr_bean_dialogue{sep}text_2.png",
                    f"{cutscene_path}{sep}mr_bean_dialogue{sep}text_3.png",
                    f"{cutscene_path}{sep}mr_bean_dialogue{sep}z_bean.png"]

IDLE_DOWN_SPRITES = [
    f"{player_path}idle_anim{sep}tile000.png",
    f"{player_path}idle_anim{sep}tile001.png",
    f"{player_path}idle_anim{sep}tile002.png",
    f"{player_path}idle_anim{sep}tile003.png",
    f"{player_path}idle_anim{sep}tile004.png",
]

IDLE_UP_SPRITES = [
    f"{player_path}idle_up_anim{sep}tile000.png",
    f"{player_path}idle_up_anim{sep}tile001.png",
    f"{player_path}idle_up_anim{sep}tile002.png",
    f"{player_path}idle_up_anim{sep}tile003.png",
    f"{player_path}idle_up_anim{sep}tile004.png",
]

IDLE_SIDE_SPRITES = [
    f"{player_path}idle_side_anim{sep}tile000.png",
    f"{player_path}idle_side_anim{sep}tile001.png",
    f"{player_path}idle_side_anim{sep}tile002.png",
    f"{player_path}idle_side_anim{sep}tile003.png",
    f"{player_path}idle_side_anim{sep}tile004.png",
]

WALK_DOWN_SPRITES = [
    f"{player_path}walk_down_anim{sep}tile000.png",
    f"{player_path}walk_down_anim{sep}tile001.png",
    f"{player_path}walk_down_anim{sep}tile002.png",
    f"{player_path}walk_down_anim{sep}tile003.png",
    f"{player_path}walk_down_anim{sep}tile004.png",
    f"{player_path}walk_down_anim{sep}tile005.png",
]

WALK_UP_SPRITES = [
    f"{player_path}walk_up_anim{sep}tile000.png",
    f"{player_path}walk_up_anim{sep}tile001.png",
    f"{player_path}walk_up_anim{sep}tile002.png",
    f"{player_path}walk_up_anim{sep}tile003.png",
    f"{player_path}walk_up_anim{sep}tile004.png",
    f"{player_path}walk_up_anim{sep}tile005.png",
]

SIDE_WALK_SPRITES = [
    f"{player_path}side_walk_anim{sep}tile000.png",
    f"{player_path}side_walk_anim{sep}tile001.png",
    f"{player_path}side_walk_anim{sep}tile002.png",
    f"{player_path}side_walk_anim{sep}tile003.png",
    f"{player_path}side_walk_anim{sep}tile004.png",
    f"{player_path}side_walk_anim{sep}tile005.png",
]

ATTACK_DOWN_SPRITES = [
    f"{player_path}attack_down_anim{sep}tile000.png",
    f"{player_path}attack_down_anim{sep}tile001.png",
    f"{player_path}attack_down_anim{sep}tile002.png",
]

ATTACK_UP_SPRITES = [
    f"{player_path}attack_up_anim{sep}tile000.png",
    f"{player_path}attack_up_anim{sep}tile001.png",
    f"{player_path}attack_up_anim{sep}tile002.png",
]

ATTACK_SIDE_SPRITES = [
    f"{player_path}attack_side_anim{sep}tile000.png",
    f"{player_path}attack_side_anim{sep}tile001.png",
    f"{player_path}attack_side_anim{sep}tile002.png",
]

PICK_UP_SPRITES = [
    f"{player_path}pick_up_anim{sep}tile000.png",
    f"{player_path}pick_up_anim{sep}tile001.png",
    f"{player_path}pick_up_anim{sep}tile002.png",
    f"{player_path}pick_up_anim{sep}tile003.png",
    f"{player_path}pick_up_anim{sep}tile004.png",
]

IDLE_DOWN_POWERUP_SPRITES = [
    f"{player_path}idle_anim_powerup{sep}tile000.png",
    f"{player_path}idle_anim_powerup{sep}tile001.png",
    f"{player_path}idle_anim_powerup{sep}tile002.png",
    f"{player_path}idle_anim_powerup{sep}tile003.png",
    f"{player_path}idle_anim_powerup{sep}tile004.png",
]

IDLE_UP_POWERUP_SPRITES = [
    f"{player_path}idle_up_anim_powerup{sep}tile000.png",
    f"{player_path}idle_up_anim_powerup{sep}tile001.png",
    f"{player_path}idle_up_animv_powerup{sep}tile002.png",
    f"{player_path}idle_up_anim_powerup{sep}tile003.png",
    f"{player_path}idle_up_anim_powerup{sep}tile004.png",
]

IDLE_SIDE_POWERUP_SPRITES = [
    f"{player_path}idle_side_anim_powerup{sep}tile000.png",
    f"{player_path}idle_side_anim_powerup{sep}tile001.png",
    f"{player_path}idle_side_anim_powerup{sep}tile002.png",
    f"{player_path}idle_side_anim_powerup{sep}tile003.png",
    f"{player_path}idle_side_anim_powerup{sep}tile004.png",
]

WALK_DOWN_POWERUP_SPRITES = [
    f"{player_path}walk_down_anim_powerup{sep}tile000.png",
    f"{player_path}walk_down_anim_powerup{sep}tile001.png",
    f"{player_path}walk_down_anim_powerup{sep}tile002.png",
    f"{player_path}walk_down_anim_powerup{sep}tile003.png",
    f"{player_path}walk_down_anim_powerup{sep}tile004.png",
    f"{player_path}walk_down_anim_powerup{sep}tile005.png",
]

WALK_UP_POWERUP_SPRITES = [
    f"{player_path}walk_up_anim_powerup{sep}tile000.png",
    f"{player_path}walk_up_anim_powerup{sep}tile001.png",
    f"{player_path}walk_up_anim_powerup{sep}tile002.png",
    f"{player_path}walk_up_anim_powerup{sep}tile003.png",
    f"{player_path}walk_up_anim_powerup{sep}tile004.png",
    f"{player_path}walk_up_anim_powerup{sep}tile005.png",
]

SIDE_WALK_POWERUP_SPRITES = [
    f"{player_path}side_walk_anim_powerup{sep}tile000.png",
    f"{player_path}side_walk_anim_powerup{sep}tile001.png",
    f"{player_path}side_walk_anim_powerup{sep}tile002.png",
    f"{player_path}side_walk_anim_powerup{sep}tile003.png",
    f"{player_path}side_walk_anim_powerup{sep}tile004.png",
    f"{player_path}side_walk_anim_powerup{sep}tile005.png",
]

ATTACK_DOWN_POWERUP_SPRITES = [
    f"{player_path}attack_down_anim_powerup{sep}tile000.png",
    f"{player_path}attack_down_anim_powerup{sep}tile001.png",
    f"{player_path}attack_down_anim_powerup{sep}tile002.png",
]

ATTACK_UP_POWERUP_SPRITES = [
    f"{player_path}attack_up_anim_powerup{sep}tile000.png",
    f"{player_path}attack_up_anim_powerup{sep}tile001.png",
    f"{player_path}attack_up_anim_powerup{sep}tile002.png",
]

ATTACK_SIDE_POWERUP_SPRITES = [
    f"{player_path}attack_side_anim_powerup{sep}tile000.png",
    f"{player_path}attack_side_anim_powerup{sep}tile001.png",
    f"{player_path}attack_side_anim_powerup{sep}tile002.png",
]

IDLE_DOWN_POWERUP_PINK_SPRITES = [
    f"{player_path}idle_anim_powerup_pink{sep}tile000.png",
    f"{player_path}idle_anim_powerup_pink{sep}tile001.png",
    f"{player_path}idle_anim_powerup_pink{sep}tile002.png",
    f"{player_path}idle_anim_powerup_pink{sep}tile003.png",
    f"{player_path}idle_anim_powerup_pink{sep}tile004.png",
]

IDLE_UP_POWERUP_PINK_SPRITES = [
    f"{player_path}idle_up_anim_powerup_pink{sep}tile000.png",
    f"{player_path}idle_up_anim_powerup_pink{sep}tile001.png",
    f"{player_path}idle_up_animv_powerup_pink{sep}tile002.png",
    f"{player_path}idle_up_anim_powerup_pink{sep}tile003.png",
    f"{player_path}idle_up_anim_powerup_pink{sep}tile004.png",
]

IDLE_SIDE_POWERUP_PINK_SPRITES = [
    f"{player_path}idle_side_anim_powerup_pink{sep}tile000.png",
    f"{player_path}idle_side_anim_powerup_pink{sep}tile001.png",
    f"{player_path}idle_side_anim_powerup_pink{sep}tile002.png",
    f"{player_path}idle_side_anim_powerup_pink{sep}tile003.png",
    f"{player_path}idle_side_anim_powerup_pink{sep}tile004.png",
]

WALK_DOWN_POWERUP_PINK_SPRITES = [
    f"{player_path}walk_down_anim_powerup_pink{sep}tile000.png",
    f"{player_path}walk_down_anim_powerup_pink{sep}tile001.png",
    f"{player_path}walk_down_anim_powerup_pink{sep}tile002.png",
    f"{player_path}walk_down_anim_powerup_pink{sep}tile003.png",
    f"{player_path}walk_down_anim_powerup_pink{sep}tile004.png",
    f"{player_path}walk_down_anim_powerup_pink{sep}tile005.png",
]

WALK_UP_POWERUP_PINK_SPRITES = [
    f"{player_path}walk_up_anim_powerup_pink{sep}tile000.png",
    f"{player_path}walk_up_anim_powerup_pink{sep}tile001.png",
    f"{player_path}walk_up_anim_powerup_pink{sep}tile002.png",
    f"{player_path}walk_up_anim_powerup_pink{sep}tile003.png",
    f"{player_path}walk_up_anim_powerup_pink{sep}tile004.png",
    f"{player_path}walk_up_anim_powerup_pink{sep}tile005.png",
]

SIDE_WALK_POWERUP_PINK_SPRITES = [
    f"{player_path}side_walk_anim_powerup_pink{sep}tile000.png",
    f"{player_path}side_walk_anim_powerup_pink{sep}tile001.png",
    f"{player_path}side_walk_anim_powerup_pink{sep}tile002.png",
    f"{player_path}side_walk_anim_powerup_pink{sep}tile003.png",
    f"{player_path}side_walk_anim_powerup_pink{sep}tile004.png",
    f"{player_path}side_walk_anim_powerup_pink{sep}tile005.png",
]

ATTACK_DOWN_POWERUP_PINK_SPRITES = [
    f"{player_path}attack_down_anim_powerup_pink{sep}tile000.png",
    f"{player_path}attack_down_anim_powerup_pink{sep}tile001.png",
    f"{player_path}attack_down_anim_powerup_pink{sep}tile002.png",
]

ATTACK_UP_POWERUP_PINK_SPRITES = [
    f"{player_path}attack_up_anim_powerup_pink{sep}tile000.png",
    f"{player_path}attack_up_anim_powerup_pink{sep}tile001.png",
    f"{player_path}attack_up_anim_powerup_pink{sep}tile002.png",
]

ATTACK_SIDE_POWERUP_PINK_SPRITES = [
    f"{player_path}attack_side_anim_powerup_pink{sep}tile000.png",
    f"{player_path}attack_side_anim_powerup_pink{sep}tile001.png",
    f"{player_path}attack_side_anim_powerup_pink{sep}tile002.png",
]


MAP_PATH = [map_path + "map_1.tmj",
            map_path + "map_2.tmj",
            map_path + "map_3.tmj",
            map_path + "map_4.tmj",
            map_path + "map_5.tmj"]

ENEMY_SKELETON_IDLE_SPRITES = [
    f"{enemies_path}Skeleton{sep}idle{sep}tile000.png",
    f"{enemies_path}Skeleton{sep}idle{sep}tile001.png",
    f"{enemies_path}Skeleton{sep}idle{sep}tile002.png",
    f"{enemies_path}Skeleton{sep}idle{sep}tile003.png",
]

ENEMY_SKELETON_RUN_SPRITES = [
    f"{enemies_path}Skeleton{sep}run{sep}tile000.png",
    f"{enemies_path}Skeleton{sep}run{sep}tile001.png",
    f"{enemies_path}Skeleton{sep}run{sep}tile002.png",
    f"{enemies_path}Skeleton{sep}run{sep}tile003.png",
]

ENEMY_SKELETON_HIT_SPRITES = [
    f"{enemies_path}Skeleton{sep}hit{sep}tile000.png",
    f"{enemies_path}Skeleton{sep}hit{sep}tile000.png",
    f"{enemies_path}Skeleton{sep}hit{sep}tile000.png",
    f"{enemies_path}Skeleton{sep}hit{sep}tile000.png",
    f"{enemies_path}Skeleton{sep}hit{sep}tile000.png",
    f"{enemies_path}Skeleton{sep}hit{sep}tile002.png",
    f"{enemies_path}Skeleton{sep}hit{sep}tile002.png",
    f"{enemies_path}Skeleton{sep}hit{sep}tile002.png",
    f"{enemies_path}Skeleton{sep}hit{sep}tile002.png",
    f"{enemies_path}Skeleton{sep}hit{sep}tile002.png",
    f"{enemies_path}Skeleton{sep}hit{sep}tile003.png",
    f"{enemies_path}Skeleton{sep}hit{sep}tile003.png",
    f"{enemies_path}Skeleton{sep}hit{sep}tile003.png",
    f"{enemies_path}Skeleton{sep}hit{sep}tile003.png",
    f"{enemies_path}Skeleton{sep}hit{sep}tile003.png",
]

ENEMY_SKELETON_DEAD_SPRITES = [
    f"{enemies_path}Skeleton{sep}dead{sep}tile000.png",
    f"{enemies_path}Skeleton{sep}dead{sep}tile000.png",
    f"{enemies_path}Skeleton{sep}dead{sep}tile000.png",
    f"{enemies_path}Skeleton{sep}dead{sep}tile000.png",
    f"{enemies_path}Skeleton{sep}dead{sep}tile001.png",
    f"{enemies_path}Skeleton{sep}dead{sep}tile001.png",
    f"{enemies_path}Skeleton{sep}dead{sep}tile001.png",
    f"{enemies_path}Skeleton{sep}dead{sep}tile001.png",
    f"{enemies_path}Skeleton{sep}dead{sep}tile002.png",
    f"{enemies_path}Skeleton{sep}dead{sep}tile002.png",
    f"{enemies_path}Skeleton{sep}dead{sep}tile002.png",
    f"{enemies_path}Skeleton{sep}dead{sep}tile002.png",
    f"{enemies_path}Skeleton{sep}dead{sep}tile003.png",
    f"{enemies_path}Skeleton{sep}dead{sep}tile003.png",
    f"{enemies_path}Skeleton{sep}dead{sep}tile003.png",
    f"{enemies_path}Skeleton{sep}dead{sep}tile003.png",
]

ENEMY_SKELETON_ATTACK_SPRITES = [
    f"{enemies_path}Skeleton{sep}attack{sep}tile000.png",
    f"{enemies_path}Skeleton{sep}attack{sep}tile000.png",
    f"{enemies_path}Skeleton{sep}attack{sep}tile001.png",
    f"{enemies_path}Skeleton{sep}attack{sep}tile001.png",
    f"{enemies_path}Skeleton{sep}attack{sep}tile002.png",
    f"{enemies_path}Skeleton{sep}attack{sep}tile002.png",
    f"{enemies_path}Skeleton{sep}attack{sep}tile003.png",
    f"{enemies_path}Skeleton{sep}attack{sep}tile003.png",
    f"{enemies_path}Skeleton{sep}attack{sep}tile004.png",
    f"{enemies_path}Skeleton{sep}attack{sep}tile004.png",
    f"{enemies_path}Skeleton{sep}attack{sep}tile005.png",
    f"{enemies_path}Skeleton{sep}attack{sep}tile005.png",
    f"{enemies_path}Skeleton{sep}attack{sep}tile006.png",
    f"{enemies_path}Skeleton{sep}attack{sep}tile006.png",
    f"{enemies_path}Skeleton{sep}attack{sep}tile007.png",
    f"{enemies_path}Skeleton{sep}attack{sep}tile007.png",
]

ENEMY_MUSHROOM_IDLE_SPRITES = [
    f"{enemies_path}Mushroom{sep}idle{sep}tile000.png",
    f"{enemies_path}Mushroom{sep}idle{sep}tile001.png",
    f"{enemies_path}Mushroom{sep}idle{sep}tile002.png",
    f"{enemies_path}Mushroom{sep}idle{sep}tile003.png",
]

ENEMY_MUSHROOM_RUN_SPRITES = [
    f"{enemies_path}Mushroom{sep}run{sep}tile000.png",
    f"{enemies_path}Mushroom{sep}run{sep}tile001.png",
    f"{enemies_path}Mushroom{sep}run{sep}tile002.png",
    f"{enemies_path}Mushroom{sep}run{sep}tile003.png",
]

ENEMY_MUSHROOM_HIT_SPRITES = [
    f"{enemies_path}Mushroom{sep}hit{sep}tile000.png",
    f"{enemies_path}Mushroom{sep}hit{sep}tile000.png",
    f"{enemies_path}Mushroom{sep}hit{sep}tile000.png",
    f"{enemies_path}Mushroom{sep}hit{sep}tile000.png",
    f"{enemies_path}Mushroom{sep}hit{sep}tile000.png",
    f"{enemies_path}Mushroom{sep}hit{sep}tile002.png",
    f"{enemies_path}Mushroom{sep}hit{sep}tile002.png",
    f"{enemies_path}Mushroom{sep}hit{sep}tile002.png",
    f"{enemies_path}Mushroom{sep}hit{sep}tile002.png",
    f"{enemies_path}Mushroom{sep}hit{sep}tile002.png",
    f"{enemies_path}Mushroom{sep}hit{sep}tile003.png",
    f"{enemies_path}Mushroom{sep}hit{sep}tile003.png",
    f"{enemies_path}Mushroom{sep}hit{sep}tile003.png",
    f"{enemies_path}Mushroom{sep}hit{sep}tile003.png",
    f"{enemies_path}Mushroom{sep}hit{sep}tile003.png",
]

ENEMY_MUSHROOM_DEAD_SPRITES = [
    f"{enemies_path}Mushroom{sep}dead{sep}tile000.png",
    f"{enemies_path}Mushroom{sep}dead{sep}tile000.png",
    f"{enemies_path}Mushroom{sep}dead{sep}tile000.png",
    f"{enemies_path}Mushroom{sep}dead{sep}tile000.png",
    f"{enemies_path}Mushroom{sep}dead{sep}tile001.png",
    f"{enemies_path}Mushroom{sep}dead{sep}tile001.png",
    f"{enemies_path}Mushroom{sep}dead{sep}tile001.png",
    f"{enemies_path}Mushroom{sep}dead{sep}tile001.png",
    f"{enemies_path}Mushroom{sep}dead{sep}tile002.png",
    f"{enemies_path}Mushroom{sep}dead{sep}tile002.png",
    f"{enemies_path}Mushroom{sep}dead{sep}tile002.png",
    f"{enemies_path}Mushroom{sep}dead{sep}tile002.png",
    f"{enemies_path}Mushroom{sep}dead{sep}tile003.png",
    f"{enemies_path}Mushroom{sep}dead{sep}tile003.png",
    f"{enemies_path}Mushroom{sep}dead{sep}tile003.png",
    f"{enemies_path}Mushroom{sep}dead{sep}tile003.png",
]

ENEMY_MUSHROOM_ATTACK_SPRITES = [
    f"{enemies_path}Mushroom{sep}attack{sep}tile000.png",
    f"{enemies_path}Mushroom{sep}attack{sep}tile000.png",
    f"{enemies_path}Mushroom{sep}attack{sep}tile001.png",
    f"{enemies_path}Mushroom{sep}attack{sep}tile001.png",
    f"{enemies_path}Mushroom{sep}attack{sep}tile002.png",
    f"{enemies_path}Mushroom{sep}attack{sep}tile002.png",
    f"{enemies_path}Mushroom{sep}attack{sep}tile003.png",
    f"{enemies_path}Mushroom{sep}attack{sep}tile003.png",
    f"{enemies_path}Mushroom{sep}attack{sep}tile004.png",
    f"{enemies_path}Mushroom{sep}attack{sep}tile004.png",
    f"{enemies_path}Mushroom{sep}attack{sep}tile005.png",
    f"{enemies_path}Mushroom{sep}attack{sep}tile005.png",
    f"{enemies_path}Mushroom{sep}attack{sep}tile006.png",
    f"{enemies_path}Mushroom{sep}attack{sep}tile006.png",
    f"{enemies_path}Mushroom{sep}attack{sep}tile007.png",
    f"{enemies_path}Mushroom{sep}attack{sep}tile007.png",
]
