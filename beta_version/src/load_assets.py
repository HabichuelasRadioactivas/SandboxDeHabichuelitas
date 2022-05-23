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

ENEMY_SLIME_IDLE_TOP_SPRITES = [
    f"{enemies_path}slime{sep}SlimeIdle{sep}SlimeIdleTop00.png",
    f"{enemies_path}slime{sep}SlimeIdle{sep}SlimeIdleTop01.png",
    f"{enemies_path}slime{sep}SlimeIdle{sep}SlimeIdleTop02.png",
    f"{enemies_path}slime{sep}SlimeIdle{sep}SlimeIdleTop03.png",
    f"{enemies_path}slime{sep}SlimeIdle{sep}SlimeIdleTop04.png",
    f"{enemies_path}slime{sep}SlimeIdle{sep}SlimeIdleTop05.png",
]

ENEMY_SLIME_IDLE_DOWN_SPRITES = [
    f"{enemies_path}slime{sep}SlimeIdle{sep}SlimeIdleDown00.png",
    f"{enemies_path}slime{sep}SlimeIdle{sep}SlimeIdleDown01.png",
    f"{enemies_path}slime{sep}SlimeIdle{sep}SlimeIdleDown02.png",
    f"{enemies_path}slime{sep}SlimeIdle{sep}SlimeIdleDown03.png",
    f"{enemies_path}slime{sep}SlimeIdle{sep}SlimeIdleDown04.png",
    f"{enemies_path}slime{sep}SlimeIdle{sep}SlimeIdleDown05.png",
]

ENEMY_SLIME_IDLE_LEFT_SPRITES = [
    f"{enemies_path}slime{sep}SlimeIdle{sep}SlimeIdleLeft00.png",
    f"{enemies_path}slime{sep}SlimeIdle{sep}SlimeIdleLeft01.png",
    f"{enemies_path}slime{sep}SlimeIdle{sep}SlimeIdleLeft02.png",
    f"{enemies_path}slime{sep}SlimeIdle{sep}SlimeIdleLeft03.png",
    f"{enemies_path}slime{sep}SlimeIdle{sep}SlimeIdleLeft04.png",
    f"{enemies_path}slime{sep}SlimeIdle{sep}SlimeIdleLeft05.png",
]

ENEMY_SLIME_IDLE_RIGHT_SPRITES = [
    f"{enemies_path}slime{sep}SlimeIdle{sep}SlimeIdleRight00.png",
    f"{enemies_path}slime{sep}SlimeIdle{sep}SlimeIdleRight01.png",
    f"{enemies_path}slime{sep}SlimeIdle{sep}SlimeIdleRight02.png",
    f"{enemies_path}slime{sep}SlimeIdle{sep}SlimeIdleRight03.png",
    f"{enemies_path}slime{sep}SlimeIdle{sep}SlimeIdleRight04.png",
    f"{enemies_path}slime{sep}SlimeIdle{sep}SlimeIdleRight05.png",
]

ENEMY_SLIME_WALK_TOP_SPRITES = [
    f"{enemies_path}slime{sep}SlimeWalk{sep}SlimeWalkTop00.png",
    f"{enemies_path}slime{sep}SlimeWalk{sep}SlimeWalkTop01.png",
    f"{enemies_path}slime{sep}SlimeWalk{sep}SlimeWalkTop02.png",
    f"{enemies_path}slime{sep}SlimeWalk{sep}SlimeWalkTop03.png",
    f"{enemies_path}slime{sep}SlimeWalk{sep}SlimeWalkTop04.png",
    f"{enemies_path}slime{sep}SlimeWalk{sep}SlimeWalkTop05.png",
]

ENEMY_SLIME_WALK_DOWN_SPRITES = [
    f"{enemies_path}slime{sep}SlimeWalk{sep}SlimeWalkDown00.png",
    f"{enemies_path}slime{sep}SlimeWalk{sep}SlimeWalkDown01.png",
    f"{enemies_path}slime{sep}SlimeWalk{sep}SlimeWalkDown02.png",
    f"{enemies_path}slime{sep}SlimeWalk{sep}SlimeWalkDown03.png",
    f"{enemies_path}slime{sep}SlimeWalk{sep}SlimeWalkDown04.png",
    f"{enemies_path}slime{sep}SlimeWalk{sep}SlimeWalkDown05.png",
]

ENEMY_SLIME_WALK_LEFT_SPRITES = [
    f"{enemies_path}slime{sep}SlimeWalk{sep}SlimeWalkLeft00.png",
    f"{enemies_path}slime{sep}SlimeWalk{sep}SlimeWalkLeft01.png",
    f"{enemies_path}slime{sep}SlimeWalk{sep}SlimeWalkLeft02.png",
    f"{enemies_path}slime{sep}SlimeWalk{sep}SlimeWalkLeft03.png",
    f"{enemies_path}slime{sep}SlimeWalk{sep}SlimeWalkLeft04.png",
    f"{enemies_path}slime{sep}SlimeWalk{sep}SlimeWalkLeft05.png",
]

ENEMY_SLIME_WALK_RIGHT_SPRITES = [
    f"{enemies_path}slime{sep}SlimeWalk{sep}SlimeWalkRight00.png",
    f"{enemies_path}slime{sep}SlimeWalk{sep}SlimeWalkRight01.png",
    f"{enemies_path}slime{sep}SlimeWalk{sep}SlimeWalkRight02.png",
    f"{enemies_path}slime{sep}SlimeWalk{sep}SlimeWalkRight03.png",
    f"{enemies_path}slime{sep}SlimeWalk{sep}SlimeWalkRight04.png",
    f"{enemies_path}slime{sep}SlimeWalk{sep}SlimeWalkRight05.png",
]

ENEMY_SLIME_DEAD_SPRITES = [
    f"{enemies_path}slime{sep}SlimeDeath{sep}SlimeDeath00.png",
    f"{enemies_path}slime{sep}SlimeDeath{sep}SlimeDeath00.png",
    f"{enemies_path}slime{sep}SlimeDeath{sep}SlimeDeath01.png",
    f"{enemies_path}slime{sep}SlimeDeath{sep}SlimeDeath01.png",
    f"{enemies_path}slime{sep}SlimeDeath{sep}SlimeDeath02.png",
    f"{enemies_path}slime{sep}SlimeDeath{sep}SlimeDeath02.png",
    f"{enemies_path}slime{sep}SlimeDeath{sep}SlimeDeath03.png",
    f"{enemies_path}slime{sep}SlimeDeath{sep}SlimeDeath03.png",
    f"{enemies_path}slime{sep}SlimeDeath{sep}SlimeDeath04.png",
    f"{enemies_path}slime{sep}SlimeDeath{sep}SlimeDeath04.png",
    f"{enemies_path}slime{sep}SlimeDeath{sep}SlimeDeath05.png",
    f"{enemies_path}slime{sep}SlimeDeath{sep}SlimeDeath05.png",
    f"{enemies_path}slime{sep}SlimeDeath{sep}SlimeDeath06.png",
    f"{enemies_path}slime{sep}SlimeDeath{sep}SlimeDeath06.png",
    f"{enemies_path}slime{sep}SlimeDeath{sep}SlimeDeath07.png",
    f"{enemies_path}slime{sep}SlimeDeath{sep}SlimeDeath07.png",
    f"{enemies_path}slime{sep}SlimeDeath{sep}SlimeDeath08.png",
    f"{enemies_path}slime{sep}SlimeDeath{sep}SlimeDeath08.png",
    f"{enemies_path}slime{sep}SlimeDeath{sep}SlimeDeath09.png",
    f"{enemies_path}slime{sep}SlimeDeath{sep}SlimeDeath09.png",
]

ENEMY_SLIME_ATTACK_TOP_SPRITES = [
    f"{enemies_path}slime{sep}SlimeDamage{sep}SlimeDamageTop00.png",
    f"{enemies_path}slime{sep}SlimeDamage{sep}SlimeDamageTop01.png",
    f"{enemies_path}slime{sep}SlimeDamage{sep}SlimeDamageTop02.png",
    f"{enemies_path}slime{sep}SlimeDamage{sep}SlimeDamageTop03.png",
]

ENEMY_SLIME_ATTACK_DOWN_SPRITES = [
    f"{enemies_path}slime{sep}SlimeDamage{sep}SlimeDamageDown00.png",
    f"{enemies_path}slime{sep}SlimeDamage{sep}SlimeDamageDown01.png",
    f"{enemies_path}slime{sep}SlimeDamage{sep}SlimeDamageDown02.png",
    f"{enemies_path}slime{sep}SlimeDamage{sep}SlimeDamageDown03.png",
]

ENEMY_SLIME_ATTACK_lEFT_SPRITES = [
    f"{enemies_path}slime{sep}SlimeDamage{sep}SlimeDamageLeft00.png",
    f"{enemies_path}slime{sep}SlimeDamage{sep}SlimeDamageLeft01.png",
    f"{enemies_path}slime{sep}SlimeDamage{sep}SlimeDamageLeft02.png",
    f"{enemies_path}slime{sep}SlimeDamage{sep}SlimeDamageLeft03.png",
]

ENEMY_SLIME_ATTACK_RIGHT_SPRITES = [
    f"{enemies_path}slime{sep}SlimeDamage{sep}SlimeDamageRight00.png",
    f"{enemies_path}slime{sep}SlimeDamage{sep}SlimeDamageRight01.png",
    f"{enemies_path}slime{sep}SlimeDamage{sep}SlimeDamageRight02.png",
    f"{enemies_path}slime{sep}SlimeDamage{sep}SlimeDamageRight03.png",
]

ENEMY_SLIME_HIT_SPRITES = [
    f"{enemies_path}slime{sep}SlimeDamage{sep}SlimeDamageTop03.png",
    f"{enemies_path}slime{sep}SlimeDamage{sep}SlimeDamageTop02.png",
    f"{enemies_path}slime{sep}SlimeDamage{sep}SlimeDamageTop03.png",
    f"{enemies_path}slime{sep}SlimeDamage{sep}SlimeDamageTop01.png",
    f"{enemies_path}slime{sep}SlimeDamage{sep}SlimeDamageTop03.png",
]

ENEMY_KNIGHT_IDLE_SPRITES = [
    f"{enemies_path}2_KNIGHT{sep}_IDLE{sep}_IDLE_000.png",
    f"{enemies_path}2_KNIGHT{sep}_IDLE{sep}_IDLE_001.png",
    f"{enemies_path}2_KNIGHT{sep}_IDLE{sep}_IDLE_002.png",
    f"{enemies_path}2_KNIGHT{sep}_IDLE{sep}_IDLE_003.png",
    f"{enemies_path}2_KNIGHT{sep}_IDLE{sep}_IDLE_004.png",
    f"{enemies_path}2_KNIGHT{sep}_IDLE{sep}_IDLE_005.png",
    f"{enemies_path}2_KNIGHT{sep}_IDLE{sep}_IDLE_006.png",
]

ENEMY_KNIGHT_ATTACK_SPRITES = [
    f"{enemies_path}2_KNIGHT{sep}_ATTACK{sep}_ATTACK_000.png",
    f"{enemies_path}2_KNIGHT{sep}_ATTACK{sep}_ATTACK_000.png",
    f"{enemies_path}2_KNIGHT{sep}_ATTACK{sep}_ATTACK_001.png",
    f"{enemies_path}2_KNIGHT{sep}_ATTACK{sep}_ATTACK_001.png",
    f"{enemies_path}2_KNIGHT{sep}_ATTACK{sep}_ATTACK_002.png",
    f"{enemies_path}2_KNIGHT{sep}_ATTACK{sep}_ATTACK_002.png",
    f"{enemies_path}2_KNIGHT{sep}_ATTACK{sep}_ATTACK_003.png",
    f"{enemies_path}2_KNIGHT{sep}_ATTACK{sep}_ATTACK_003.png",
    f"{enemies_path}2_KNIGHT{sep}_ATTACK{sep}_ATTACK_004.png",
    f"{enemies_path}2_KNIGHT{sep}_ATTACK{sep}_ATTACK_004.png",
    f"{enemies_path}2_KNIGHT{sep}_ATTACK{sep}_ATTACK_005.png",
    f"{enemies_path}2_KNIGHT{sep}_ATTACK{sep}_ATTACK_005.png",
    f"{enemies_path}2_KNIGHT{sep}_ATTACK{sep}_ATTACK_006.png",
    f"{enemies_path}2_KNIGHT{sep}_ATTACK{sep}_ATTACK_006.png",
]

ENEMY_KNIGHT_DEAD_SPRITES = [
    f"{enemies_path}2_KNIGHT{sep}_DIE{sep}_DIE_000.png",
    f"{enemies_path}2_KNIGHT{sep}_DIE{sep}_DIE_000.png",
    f"{enemies_path}2_KNIGHT{sep}_DIE{sep}_DIE_001.png",
    f"{enemies_path}2_KNIGHT{sep}_DIE{sep}_DIE_001.png",
    f"{enemies_path}2_KNIGHT{sep}_DIE{sep}_DIE_002.png",
    f"{enemies_path}2_KNIGHT{sep}_DIE{sep}_DIE_002.png",
    f"{enemies_path}2_KNIGHT{sep}_DIE{sep}_DIE_003.png",
    f"{enemies_path}2_KNIGHT{sep}_DIE{sep}_DIE_003.png",
    f"{enemies_path}2_KNIGHT{sep}_DIE{sep}_DIE_004.png",
    f"{enemies_path}2_KNIGHT{sep}_DIE{sep}_DIE_004.png",
    f"{enemies_path}2_KNIGHT{sep}_DIE{sep}_DIE_005.png",
    f"{enemies_path}2_KNIGHT{sep}_DIE{sep}_DIE_005.png",
    f"{enemies_path}2_KNIGHT{sep}_DIE{sep}_DIE_006.png",
    f"{enemies_path}2_KNIGHT{sep}_DIE{sep}_DIE_006.png",
]

ENEMY_KNIGHT_HIT_SPRITES = [
    f"{enemies_path}2_KNIGHT{sep}_HURT{sep}_HURT_000.png",
    f"{enemies_path}2_KNIGHT{sep}_HURT{sep}_HURT_000.png",
    f"{enemies_path}2_KNIGHT{sep}_HURT{sep}_HURT_001.png",
    f"{enemies_path}2_KNIGHT{sep}_HURT{sep}_HURT_001.png",
    f"{enemies_path}2_KNIGHT{sep}_HURT{sep}_HURT_002.png",
    f"{enemies_path}2_KNIGHT{sep}_HURT{sep}_HURT_002.png",
    f"{enemies_path}2_KNIGHT{sep}_HURT{sep}_HURT_003.png",
    f"{enemies_path}2_KNIGHT{sep}_HURT{sep}_HURT_003.png",
    f"{enemies_path}2_KNIGHT{sep}_HURT{sep}_HURT_004.png",
    f"{enemies_path}2_KNIGHT{sep}_HURT{sep}_HURT_004.png",
    f"{enemies_path}2_KNIGHT{sep}_HURT{sep}_HURT_005.png",
    f"{enemies_path}2_KNIGHT{sep}_HURT{sep}_HURT_005.png",
    f"{enemies_path}2_KNIGHT{sep}_HURT{sep}_HURT_006.png",
    f"{enemies_path}2_KNIGHT{sep}_HURT{sep}_HURT_006.png",
]

ENEMY_KNIGHT_RUN_SPRITES = [
    f"{enemies_path}2_KNIGHT{sep}_RUN{sep}_RUN_000.png",
    f"{enemies_path}2_KNIGHT{sep}_RUN{sep}_RUN_001.png",
    f"{enemies_path}2_KNIGHT{sep}_RUN{sep}_RUN_002.png",
    f"{enemies_path}2_KNIGHT{sep}_RUN{sep}_RUN_003.png",
    f"{enemies_path}2_KNIGHT{sep}_RUN{sep}_RUN_004.png",
    f"{enemies_path}2_KNIGHT{sep}_RUN{sep}_RUN_005.png",
    f"{enemies_path}2_KNIGHT{sep}_RUN{sep}_RUN_006.png",
]

ENEMY_KNIGHT_WALK_SPRITES = [
    f"{enemies_path}2_KNIGHT{sep}_WALK{sep}_RUN_000.png",
    f"{enemies_path}2_KNIGHT{sep}_WALK{sep}_RUN_001.png",
    f"{enemies_path}2_KNIGHT{sep}_WALK{sep}_RUN_002.png",
    f"{enemies_path}2_KNIGHT{sep}_WALK{sep}_RUN_003.png",
    f"{enemies_path}2_KNIGHT{sep}_WALK{sep}_RUN_004.png",
    f"{enemies_path}2_KNIGHT{sep}_WALK{sep}_RUN_005.png",
    f"{enemies_path}2_KNIGHT{sep}_WALK{sep}_RUN_006.png",
]
